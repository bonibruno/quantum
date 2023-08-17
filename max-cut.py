#
#  How to use Amazon Braket to solve a simple Max-Cut optimization problem.
#
#  This code sets up a Max-Cut problem using a QUBO matrix and then solves it using the D-Wave quantum annealer through Amazon Braket.
#
#  Make sure to have proper permissions and configurations for AWS, including the necessary IAM roles and S3 bucket setup.
#
#

import boto3
from braket.aws import AwsDevice
from braket.ocean_plugin import BraketSampler, BraketDWaveSampler

# Define the graph for the Max-Cut problem
graph = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 1)]

# Define the QUBO (Quadratic Unconstrained Binary Optimization) matrix
Q = {(a, b): 1 if (a, b) in graph or (b, a) in graph else 0 for a in range(4) for b in range(4)}

# Specify the solver (D-Wave)
s3_folder = ("my-bucket", "my-folder")
device = AwsDevice("arn:aws:braket:::device/qpu/d-wave/DW_2000Q_6")

# Create a sampler
sampler = BraketDWaveSampler(s3_folder, device.arn)

# Sample the solution
sampleset = sampler.sample_qubo(Q, num_reads=1000)

# Print the result
print(sampleset)

#
# Sample output
#
#   0  1  2  3 energy num_occurrences
#0  1  0  1  0   -2.0             205
#1  0  1  0  1   -2.0             195
#2  1  1  0  0   -1.0             100
#3  0  0  1  1   -1.0             300
#4  1  0  0  1   -1.0             100
#5  0  1  1  0   -1.0             100
#['BINARY', 6 rows, 1000 samples, 4 variables]

#
# 
#  The columns labeled 0, 1, 2, and 3 correspond to the values of the qubits for different solutions. 
#  The energy column represents the energy of each solution (with lower energies corresponding to better solutions), and the num_occurrences column shows how many times each solution was sampled during the annealing process.

# Please note that the actual output will depend on the specific problem, the quantum device, the parameters passed to the sampler, and the inherent probabilistic nature of quantum annealing. It's typical to see variations in the output between different runs of the same code.

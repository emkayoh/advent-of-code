import pandas as pd
import numpy as np
from itertools import product

# Read input data
input_data = pd.read_csv('test.txt', sep=':', header=None, names=['calib', 'nums'])

# Define operators array
array = ['+', '*']

# Function to generate combinations of operators
def gen_comb(array, times):
    combinations = list(product(array, repeat=times))
    return np.array(combinations)

# Function to calculate the result of an equation
def calc_eq(nums, ops):
    res = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            res += nums[i + 1]
        else:  # Assume the only other option is '*'
            res *= nums[i + 1]
    return res

# Function to check calibration
def calibration(numbers, value):
    n = len(numbers) - 1
    perm = gen_comb(array, n)
    for ops in perm:
        res = calc_eq(numbers, ops)
        if res == value:
            return True
    return False

# Process input data
out = []
for _, row in input_data.iterrows():
    value = row['calib']
    nums = list(map(int, row['nums'].strip().split()))
    fixed = calibration(nums, value)
    out.append(fixed)

# Calculate the final output
result = sum(input_data['calib'][i] * out[i] for i in range(len(out)))
print(result)

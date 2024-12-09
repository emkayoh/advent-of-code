import pandas as pd
import numpy as np
from itertools import product

# Read input data
input_data = pd.read_csv('input.txt', sep=':', header=None, names=['calib', 'nums'])

# Define operators array
array = ['+', '*', '|']

# Function to generate combinations of operators
def gen_comb(array, times):
    combinations = list(product(array, repeat=times))
    return np.array(combinations)

# Function to calculate the result of an equation with the extended set of operations
def calc_eq2(nums, ops):
    res = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            res += nums[i + 1]
        elif ops[i] == '*':
            res *= nums[i + 1]
        elif ops[i] == '|':  # Concatenate numbers as a string and convert back to numeric
            res = int(f"{res}{nums[i + 1]}")
    return res

# Function to check calibration with the extended set of operations
def calibration2(numbers, value):
    n = len(numbers) - 1
    perm = gen_comb(array, n)
    for ops in perm:
        res = calc_eq2(numbers, ops)
        if res == value:
            return True
        if res > value:
            continue  # Skip the remaining calculations if the result exceeds the target
    return False

# Process input data
out = []
for _, row in input_data.iterrows():
    value = row['calib']
    nums = list(map(int, row['nums'].strip().split()))
    fixed = calibration2(nums, value)
    out.append(fixed)

# Calculate the final output
result = sum(input_data['calib'][i] * out[i] for i in range(len(out)))
print(result)

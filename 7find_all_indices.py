# Input list and target value
numbers = [1, 2, 3, 2, 4, 2]
target = 2

# Find all indices where target appears
indices = [i for i, val in enumerate(numbers) if val == target]

# Print the result
print("Indices:", indices)
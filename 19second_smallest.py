# Prompt user for input
input_str = input("Enter numbers separated by commas: ")

# Convert input string to list of integers
numbers = list(map(int, input_str.split(',')))

# Remove duplicates using set, then sort
unique_sorted = sorted(set(numbers))

# Check if there are at least 2 unique values
if len(unique_sorted) >= 2:
    print("Second smallest unique value:", unique_sorted[1])
else:
    print("Not enough unique values to find the second smallest.")
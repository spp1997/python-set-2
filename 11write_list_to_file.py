# Prompt user for comma-separated strings
input_str = input("Enter a list of strings (comma-separated): ")

# Convert input to list of strings
string_list = [s.strip() for s in input_str.split(',')]

# Print each string on a new line
print("Output:")
for item in string_list:
    print(item)
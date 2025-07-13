# Prompt user for comma-separated strings
input_str = input("Enter a list of strings (comma-separated): ")

# Convert input to list of strings
string_list = [s.strip() for s in input_str.split(',')]

# Write each string to a new line in a text file
with open("output.txt", "w") as file:
    for item in string_list:
        file.write(item + "\n")

print("Strings written to output.txt")
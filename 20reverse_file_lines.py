# Open and read all lines from the file
with open("lines.txt", "r") as file:
    lines = file.readlines()

# Strip newlines and reverse the list
reversed_lines = [line.strip() for line in lines][::-1]

# Print each line
for line in reversed_lines:
    print(line)
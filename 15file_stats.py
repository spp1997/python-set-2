# Open and read the file
with open("data.txt", "r") as file:
    lines = file.readlines()

# Count lines
num_lines = len(lines)

# Count words and characters
num_words = 0
num_chars = 0

for line in lines:
    num_words += len(line.split())
    num_chars += len(line)

# Print results
print("Lines:", num_lines)
print("Words:", num_words)
print("Characters:", num_chars)
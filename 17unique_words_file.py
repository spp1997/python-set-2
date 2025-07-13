# Open and read the file
with open("input.txt", "r") as file:
    text = file.read()

# Split text into words
words = text.split()

# Use set to get unique words, then sort
unique_words = sorted(set(words))

# Print the result
print(unique_words)
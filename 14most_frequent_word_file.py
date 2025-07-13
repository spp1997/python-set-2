# Open and read the file
with open("words.txt", "r") as file:
    text = file.read()

# Split text into words
words = text.split()

# Count word frequencies using a dictionary
word_count = {}
for word in words:
    word = word.lower()  # Optional: make it case-insensitive
    word_count[word] = word_count.get(word, 0) + 1

# Find the word with the highest count
most_common = max(word_count.items(), key=lambda item: item[1])

# Print result
print(f"{most_common[0]}: {most_common[1]}")
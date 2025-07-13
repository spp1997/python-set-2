text = "banana"

# Initialize empty dictionary
char_count = {}

# Loop through each character in the string
for char in text:
    if char in char_count:
        char_count[char] += 1  # Increment count
    else:
        char_count[char] = 1   # First occurrence

# Print each character with its count
for char, count in char_count.items():
    print(f"{char}: {count}")
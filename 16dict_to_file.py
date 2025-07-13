# Input dictionary
data = {'a': 1, 'b': 2}

# Open file for writing
with open("output1.txt", "w") as file:
    for key, value in data.items():
        file.write(f"{key}:{value}\n")

print("Dictionary written to output1.txt")
# List of input files
filenames = ["file1.txt", "file2.txt"]

# Open the output file for writing
with open("merged.txt", "w") as output_file:
    # Loop through each input file
    for fname in filenames:
        with open(fname, "r") as input_file:
            # Read and write each line from the input file
            for line in input_file:
                output_file.write(line)

print("Files merged into merged.txt")
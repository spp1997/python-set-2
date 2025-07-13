# Open the file for reading
with open("numbers.txt", "r") as file:
    # Read all lines and convert to numbers
    numbers = [float(line.strip()) for line in file if line.strip()]

# Calculate average
if numbers:
    average = sum(numbers) / len(numbers)
    print("Average:", average)
else:
    print("No numbers found in file.")
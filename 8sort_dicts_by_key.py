# Input list of dictionaries
people = [{'name': 'Anna', 'age': 22}, {'name': 'Bob', 'age': 19}]

# Sort by 'age' using lambda
sorted_people = sorted(people, key=lambda person: person['age'])

# Print the sorted list
print("Sorted by age:", sorted_people)

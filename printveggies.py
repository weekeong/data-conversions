vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "potato"},
 {"name": "carrot"},
 {"name": "kale"},
 {"name": "broccoli"}
]

# Write header file to csv

import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["name", 'length'])
# Loop through each vegetable
	for veggie in vegetables:
# For each vegetable, write a row to the CSV
		name = veggie["name"]
		length = len(name)
		writer.writerow([name, length])


#read vegetables.csv

import csv

with open ('veggies.csv') as f:
#convert to json
	reader = csv.DictReader(f)
	vegetables = list(reader)

# write to JSON file

import json

with open('veggies.json', 'w') as f:
	json.dump(vegetables, f, indent=4)
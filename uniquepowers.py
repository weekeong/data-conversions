#read superhero.json
# get unique list of powers

import json
with open('superheroes.json') as f:
	data = json.load(f)

all_powers = []

# get members
members = data['members']
# loop over the members
for m in members:
	powers = m['powers']
	for p in powers:
# for each member, get their powers
		all_powers.append(p)



# print to terminal
unique_powers = list(set(powers))

print all_powers
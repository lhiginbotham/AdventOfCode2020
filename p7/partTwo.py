import re

inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()

rules = dict()
for i in range(0, len(inp)):
	colorBag, rule = inp[i].split(' contain ')
	colorBag = colorBag.split(' bags')[0]
	rules[colorBag] = dict()

	ruleNumAndColors = rule.split(', ')
	for numAndColor in ruleNumAndColors:
		if 'no other bags' in numAndColor:
			break
		match = re.search(r'([0-9]+) (\w+ \w+)', numAndColor)
		rules[colorBag][match.group(2)] = int(match.group(1))

# part one

# def graph_look_for(currColor, searchColor, alreadyVisited, needToVisit, leadsToSearchColor):
	# alreadyVisited.add(currColor)
	# if 'shiny gold' in rules[currColor].keys():
		# leadsToSearchColor.add(currColor)
		# return True
	# else:
		# for color in rules[currColor].keys():
			# if color in alreadyVisited:
				# if color in leadsToSearchColor:
					# leadsToSearchColor.add(currColor)
			# elif graph_look_for(color, searchColor, alreadyVisited, needToVisit, leadsToSearchColor):
				# leadsToSearchColor.add(currColor)
		# return currColor in leadsToSearchColor

# leadsToSearchColor = set()
# alreadyVisited = set()
# needToVisit = set()
# for color in rules.keys():
	# graph_look_for(color, 'shiny gold', alreadyVisited, needToVisit, leadsToSearchColor)

#print(rules)
#print(len(leadsToSearchColor))

# part two

def count_bags_contained_by(currColor, numBagColorContains):
	if currColor in numBagColorContains:
		return numBagColorContains[currColor]

	currColorContains = 0
	for color in rules[currColor].keys():
		currColorContains += rules[currColor][color] + rules[currColor][color] * count_bags_contained_by(color, numBagColorContains)

	numBagColorContains[currColor] = currColorContains
	return currColorContains

print(count_bags_contained_by('shiny gold', dict()))
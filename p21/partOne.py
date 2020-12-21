import copy

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

food = []
ingredients = set()
allergenToFoodsIdx = dict()

for line in inp:
    _ingredients, allergens = line.split(' (contains ')
    _ingredients = [x for x in _ingredients.split() if len(x) > 0]
    if allergens[-1] == ')':
        allergens = allergens[:-1]
    allergens = [x for x in allergens.split(', ') if len(x) > 0]
    for a in allergens:
        if a not in allergenToFoodsIdx:
            allergenToFoodsIdx[a] = set()
        allergenToFoodsIdx[a].add(len(food))

    for x in _ingredients:
        ingredients.add(x)
    food.append((_ingredients, allergens))

#print(food)
print(ingredients)
ingredientInWhatAllergenFoods = dict()
for ing in ingredients:
    ingredientInWhatAllergenFoods[ing] = set()
    for f in food:
        if ing in f[0]:
            for allergen in f[1]:
                ingredientInWhatAllergenFoods[ing].add(allergen)

#print(ingredientInWhatAllergenFoods)

ingredientToPossibleIdentity = dict()
for ing in ingredientInWhatAllergenFoods:
    ingredientToPossibleIdentity[ing] = copy.deepcopy(ingredientInWhatAllergenFoods[ing])
    for allergen in ingredientInWhatAllergenFoods[ing]:
        for foodIdx in allergenToFoodsIdx[allergen]:
            if ing not in food[foodIdx][0]:
                ingredientToPossibleIdentity[ing].discard(allergen)

nonallergens = []
for ing in ingredientToPossibleIdentity:
    if len(ingredientToPossibleIdentity[ing]) == 0:
        nonallergens.append(ing)
print(nonallergens)
count = 0
for f in food:
    for ing in nonallergens:
        if ing in f[0]:
            count += 1
            
print(count)
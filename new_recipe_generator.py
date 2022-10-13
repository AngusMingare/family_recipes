carb = ["pasta", "rice"]
vegetable = ["carrot", "potato", 'zucchini', "peas", "corn"]
protein = ["beef", "chicken", "pork", "fish", "tofu", "beans"]
sauce = ["ketchup", "mayo", "ragu", "curry"]

num_carbs = len(carb)
num_vegetables = len(vegetable)
num_proteins = len(protein)
num_sauces = len(sauce)

carb_method = ["boil", "cook according to packet instructions"]
vegetable_method = ["roast", "boil", "deep fry"]
protein_method = ["fry", "bake", "boil", "deep fry"] 
sauce_method = ["pour", "infuse", "make"]

num_carb_methods = len(carb_method)
num_vegetable_methods = len(vegetable_method)
num_protein_methods = len(protein_method)
num_sauce_methods = len(sauce_method)

import numpy as np

c = np.random.randint(0,num_carbs)
v = np.random.randint(0,num_vegetables)
p = np.random.randint(0,num_proteins)
s = np.random.randint(0,num_sauces)

cm = np.random.randint(0,num_carb_methods)
vm = np.random.randint(0,num_vegetable_methods)
pm = np.random.randint(0,num_protein_methods)
sm = np.random.randint(0,num_sauce_methods)

print("New Recipe!")
print("Ingredients:")
print(carb[c])
print(vegetable[v])
print(protein[p])
print(sauce[s])

print("Method:")
print("1. " + carb_method[cm] + " the " + carb[c])
print("2. " + vegetable_method[vm] + " the " + vegetable[v])
print("3. " + protein_method[pm] + " the " + protein[p])
print("4. " + sauce_method[sm] + " the " + sauce[s])
print("5. Mix together and serve!")
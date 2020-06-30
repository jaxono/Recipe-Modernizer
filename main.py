# Declare Variables
from math import inf

UNIT_NAMES = ["g", "mg", "kg", "ml", "l", "t", "oz", "lbs", "st", "ton", "c", "tbsp", "dstspn", "tsp"]
UNIT_SIZES = [1, 0.001, 1000, 1, 1000, 1000000, 28.3495, 453.592, 6350.29, 907185, 128, 15, 10, 5]

recipe_name = input("Recipe Name: ").title()  # Get Name

ingrs = []


class Ingr:
    def __init__(self, name, size):
        self.name = name
        self.size = size


ingr_name = ""
ratio = 1

while True:
    try:
        # Get original and new unit scales

        ori_ser_size = input("Original Serving Size: ")
        new_ser_size = input("New Serving Size: ")

        # Calculate Ratio

        ratio = float(new_ser_size) / float(ori_ser_size)
    except ValueError:  # Check if input formatting is correct
        print('Invalid Input, please re-enter and make sure that "Original Serving Size" and "New Serving Size" are valid numbers.')
        continue
    except ZeroDivisionError:  # Make sure a division by 0 does not occur
        print('"Original Serving Size" cannot be 0, please re-enter.')
        continue

    # Warn if ratio is to big/small/ or force re-entry infinite/0/negative

    if ratio <= 0:
        print("That ratio is 0 or less, please re-enter.")
        continue

    if ratio == inf:
        print("That ratio is so large that the computer thinks that it is infinite, please re-enter.")
        continue

    if ratio > 3:
        con = input("That is quite large, you should make smaller batches. Continue? (Y/N): ").lower().strip()
        if con == "yes" or con == "y":
            break
        else:
            continue

    if ratio < .25:
        con = input("That is quite small, you should make larger batches and freeze leftovers. Continue? (Y/N): ").lower().strip()
        if con == "yes" or con == "y":
            break
        else:
            continue
    break

# Print out name and ratio and a blank line for separation

print("Name: {}, Ratio: 1 : {}".format(recipe_name, round(ratio, 3)).rstrip("0").rstrip("."))
print()

# Ask for Ingredients

print("""Enter a list of ingredients that are in your recipe. Syntax: "<Size> <Unit> <Ingredient>" eg.
100 g butter
50 lbs butter
1 kg milk
1 l milk
1 c flower
done
""")

while True:
    ingredient = input('Enter Ingredient, type "done" to end: ')

    # Make sure the user can break the loop

    if ingredient.lower().strip() == "done":
        break

    # Check formatting

    if ingredient.count(" ") < 1:
        print("Syntax Error")
        continue

    try:

        # Separate data

        ingr_size = ingredient[:ingredient.index(" ")]
        ingredient = ingredient[ingredient.index(" ") + 1:]
        unit = ingredient[:ingredient.index(" ")].lower()
        ingr_name = ingredient[ingredient.index(" ") + 1:].title()

        # Process ingr_size

        if ingr_size.count("/") == 0:
            ingr_size = float(ingr_size)
        elif ingr_size.count("/") == 1:
            ingr_size = float(ingr_size[:ingr_size.index("/")]) / float(ingr_size[ingr_size.index("/") + 1:])
        else:
            print("Syntax Error, please re-enter")
            continue

        if ingr_size <= 0:
            print("That size is 0 or less, please re-enter.")
            continue

        if ingr_size == inf:
            print("That size is so large that the computer thinks that it is infinite, please re-enter.")
            continue

        # Convert to the gram

        ingr_size = ingr_size * UNIT_SIZES[UNIT_NAMES.index(unit)]

        # Add the ingredient to the list

        ingrs.append(Ingr(ingr_name, ingr_size))

        print("Added " + str(round(ingr_size, 3)).rstrip("0").rstrip(".") + " g " + ingr_name)

    except ValueError:
        print("Syntax Error, please re-enter")
        continue

    print()

# Print out new recipe

print()
print("Modern Recipe:\n\n{}\n".format(recipe_name))

# Loop though all ingredients

i = 0
while i < len(ingrs):

    # Get ingredient data from list and scale sizes

    ingr_size = ingrs[i].size * ratio
    unit = "g"

    # Convert to mg or kg if appropriate

    if ingr_size < 1:
        ingr_size = ingr_size * 1000
        unit = "mg"

    elif ingr_size >= 1000:
        ingr_size = ingr_size / 1000
        unit = "kg"

        # Print out ingredient

    print(str(round(ingr_size, 3)).rstrip("0").rstrip(".") + " " + unit + " " + ingrs[i].name)
    i += 1

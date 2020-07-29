# Declare Variables
from math import inf

UNIT_NAMES = ["g", "mg", "kg", "ml", "l", "t", "oz", "lbs", "st", "ton", "c", "tbsp", "dstspn", "tsp", "pinch"]
UNIT_SIZES = [1, 0.001, 1000, 1, 1000, 1000000, 28.3495, 453.592, 6350.29, 907185, 128, 15, 10, 5, 0.355625]

USELESS_WORDS = ["the", "of", "a"]

recipe_name = input("Recipe Name: ").title()  # Get Name

origin = input("Place of Origin: ").title()  # Get Location

ingrs = []


class Ingr:
    def __init__(self, name, size, united):
        self.name = name
        self.size = size
        self.united = united


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

    # Warn if ratio is to big/small or force re-entry infinite/0/negative

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

    ingr_size = "1"
    unit = ""
    ingr_name = ""

    while True:
        continue_now = False
        try:
            front_word = ingredient[:ingredient.index(" ")]
        except:
            break

        for useless_word in USELESS_WORDS:
            if front_word.strip().lower() == useless_word:
                ingredient = ingredient[ingredient.index(" ") + 1:]
                continue_now = True
        if continue_now:
            continue

        try:
            if ingr_size.count("/") == 0:
                float(front_word.strip().lower())
                ingr_size = front_word.strip().lower()
            elif ingr_size.count("/") == 1:
                ingr_size = front_word.strip().lower()
            try:
                    ingredient = ingredient[ingredient.index(" ") + 1:]
            except:
                break
            continue
        except:
            pass

        for unit_name in UNIT_NAMES:
            if front_word.strip().lower() == unit_name:
                unit = front_word.strip().lower()
                try:
                    ingredient = ingredient[ingredient.index(" ") + 1:]
                except:
                    break
                continue_now = True
        if continue_now:
            continue

        break

    ingr_name = ingredient.title()

    ingr_united = not unit == ""

    #print()
    #print(ingr_size)
    #print(unit)
    #print(ingr_name)

    try:

        # Separate data

        #ingr_size = ingredient[:ingredient.index(" ")]
        #ingredient = ingredient[ingredient.index(" ") + 1:]
        #unit = ingredient[:ingredient.index(" ")].lower()
        #ingr_name = ingredient[ingredient.index(" ") + 1:].title()

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

        if ingr_united:
            ingr_size = ingr_size * UNIT_SIZES[UNIT_NAMES.index(unit)]

        # Add the ingredient to the list

        ingrs.append(Ingr(ingr_name, ingr_size, ingr_united))

        if ingr_united:
            print("Added " + str(round(ingr_size, 3)).rstrip("0").rstrip(".") + " g of " + ingr_name)
        else:
            print("Added " + str(round(ingr_size, 3)).rstrip("0").rstrip(".") + " " + ingr_name)

    except ValueError:
        print("Syntax Error, please re-enter")
        continue

    print()

# Print out new recipe

print()
print("Modern Recipe:\n\n{}".format(recipe_name))
print("From " + origin + "\n")

# Loop though all ingredients

i = 0
while i < len(ingrs):

    # Get ingredient data from list and scale sizes

    ingr_size = ingrs[i].size * ratio
    unit = "g"

    # Convert to mg or kg if appropriate

    if ingrs[i].united:
        if ingr_size < 1:
            ingr_size = ingr_size * 1000
            unit = "mg"

        elif ingr_size >= 1000:
            ingr_size = ingr_size / 1000
            unit = "kg"

        # Print out ingredient

    if ingrs[i].united:
        print(str(round(ingr_size, 3)).rstrip("0").rstrip(".") + " " + unit + " of " + ingrs[i].name)
    else:
        print(str(round(ingr_size, 3)).rstrip("0").rstrip(".") + " " + ingrs[i].name)
    i += 1

# Declare Variables
from math import inf

UNITS = [[["mg", "milligram", "milligrams"], 0.001],
         [["g", "gram", "grams", "ml", "millilitre", "millilitres", "milliliter", "milliliters"], 1],
         [["kg", "kilogram", "kilograms", "l", "litre", "litres", "liter", "liters"], 1000],
         [["t", "tonne", "tonnes", "metric tonne", "metric tonnes", "megagram", "megagrams"], 1000000],

         [["st", "stone", "stones"], 6350.29],
         [["ton", "tons"], 907185],
         [["pinch"], 0.355625],
         [["dstspn", "dessertspoon", "dessertspoons"], 10],

         [["gr", "grain", "grains"], 0.006479891],
         [["min", "minim", "minims"], 0.061611519921875],
         [["s", "scruple", "scruples"], 1.18387760416],
         [["dwt", "pennyweight", "pennyweights"], 1.55517384],
         [["dr", "dram", "drams", "drachm", "drachms"], 1.7718451953125],
         [["tsp", "teaspoon", "teaspoons"], 4.92892159375],
         [["tbsp", "tablespoon", "tablespoons"], 14.78676478125],
         [["oz", "ounce", "ounces"], 28.349523125],
         [["jig", "shot", "shots"], 44.36029434375],
         [["gi", "gill", "gills"], 118.29411825],
         [["c", "cup", "cups"], 236.5882365],
         [["lbs", "pound", "pounds"], 453.59237],
         [["pt", "pint", "pints"], 473.176473],
         [["qt", "quart", "quarts"], 946.352946],
         [["pot", "pottle", "pottles", "pottel", "pottels"], 1892.70589],
         [["gal", "gallon", "gallons"], 3785.411784],
         [["pk", "peck", "pecks"], 8809.768],
         [["slug", "slugs"], 14593.90294],
         [["bu", "brushel", "brushels"], 35239.07016688],
         [["cwt", "hundredweight", "hundredweights"], 45359.237],
         [["bbl", "barrel", "barrels"], 119240.471196],
         [["hogshead", "hogsheads"], 238480.942392],

         [["si", "sis"], 0.0003125],
         [["hao", "haos"], 0.003125],
         [["li", "lis"], 0.05],
         [["fen", "fens"], 0.5],
         [["qian", "qians"], 5],
         [["liang", "liangs"], 50],
         [["jin", "jins"], 500],
         [["dan", "dans"], 50000],

         [["nothing"], 0]]

USELESS_WORDS = ["the", "of", "a", "an"]

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

    try:

        # Separate data

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

            for x in range(len(UNITS)):
                for y in range(len(UNITS[x][0])):
                    if front_word.strip().lower() == UNITS[x][0][y]:
                        unit = UNITS[x][0][0]
                        ingredient = ingredient[ingredient.index(" ") + 1:]
                        continue_now = True
            if continue_now:
                continue

            break

        ingr_name = ingredient.title()

        ingr_united = not unit == ""

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
            for x in range(len(UNITS)):
                for y in range(len(UNITS[x][0])):
                    if unit == UNITS[x][0][y]:
                        ingr_size = ingr_size * UNITS[x][1]

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

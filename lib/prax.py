spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    #Loop through list of dictionaries and return names
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

print(get_names(spicy_foods))


def get_spiciest_Foods(spicy_foods):
    #loop through list of dictionaries and return foods with heat level greater than 5
    spiciest_food = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_food.append(food)
        return spiciest_food
print(get_spiciest_Foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    spici_foods = []
    for food in spicy_foods:
        spici_foods.append(f"{food["name"]} ({food["cuisine"]}) | Heat level: {'🌶' * food["heat_level"]} ")
    return spici_foods
print(print_spicy_foods(spicy_foods))



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
  for food in spicy_foods:
      if food["cuisine"] == cuisine:
          return food
  return None
      
print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    spiciest_food = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_food.append(f"{food['name']} ({food['cuisine']}) | Heat level: {'🌶' * food['heat_level']}")
    return spiciest_food
print(print_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    #return average by dividing total heat level by number of foods using // to ensure whole number is returned
    return total_heat #// len(spicy_foods)
print(get_average_heat_level(spicy_foods))
print(len(spicy_foods))
# print(total_heat)

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
    #ORR
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(spicy_foods, {"name": "Griot", 
                                      "cuisine": "Haitian", 
                                      "heat_level": 10
                                      }))
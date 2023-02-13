days = int(input())
quantity_food = float(input())
food_eaten_by_dog = 0
food_eaten_by_cat = 0

all_eaten_food = food_eaten_by_cat + food_eaten_by_dog

for every_day in range(1, days+1):
    dog_food = int(input())
    cat_food = int(input())
    food_eaten_by_dog += dog_food
    food_eaten_by_cat += cat_food
    if every_day / 3 == 0:
        pass

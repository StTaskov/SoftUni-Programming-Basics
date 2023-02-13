
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  –  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  –  отстъпка от 25%.

budget = int(input())
season = input()
fishermans = int(input())
price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fishermans <= 6:
    price -= price * 0.10
elif fishermans <= 11:
    price -= price * 0.15
elif fishermans >= 12:
    price -= price * 0.25

if fishermans % 2 == 0 and not season == "Autumn":
        price -= price * 0.05

diff = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

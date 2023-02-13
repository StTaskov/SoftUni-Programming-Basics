# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough save_money, you need {нужната сума} leva more.".

flowers = input()
flowers_count = int(input())
budget = int(input())
price = 0
if flowers == "Roses":
    price = 5
    if flowers_count > 80:
        price -= price * 0.10
if flowers == "Dahlias":
    price = 3.80
    if flowers_count > 90:
        price -= price * 0.15

if flowers == "Tulips":
    price = 2.80
    if flowers_count > 80:
        price -= price * 0.15

if flowers == "Narcissus":
    price = 3
    if flowers_count < 120:
        price += price * 0.15

if flowers == "Gladiolus":
    price = 2.50
    if flowers_count < 80:
        price += price * 0.20
money_needed = flowers_count * price
discount = abs(budget - money_needed)
if budget >= money_needed:
    print(f"Hey, you have a great garden with {flowers_count} {flowers} and {discount:.2f} leva left.")
else:
    print(f"Not enough money, you need {discount:.2f} leva more.")
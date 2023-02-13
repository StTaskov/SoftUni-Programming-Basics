# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв.
# Цена на екскурзията - реално число;
# Брой пъзели - цяло число;
# Брой говорещи кукли - цяло число;
# Брой плюшени мечета - цяло число;
# Брой миньони - цяло число;
# Брой камиончета - цяло число.
# Ако парите са достатъчни се отпечатва:
# Yes! {оставащите пари} lv left.
# Aко парите НЕ са достатъчни се отпечатва:
# Not enough save_money! {недостигащите пари} lv needed.

puzzle_price = 2.60
talking_doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2
holiday_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

toys_sum = puzzle_count * puzzle_price + talking_doll_price * talking_doll_count + bear_count * bear_price + minion_price * minion_count + truck_count * truck_price
toys_count = puzzle_count + talking_doll_count + bear_count + minion_count + truck_count
if toys_count >= 50:
    toys_sum = toys_sum * 0.25
else:
    toys_sum = toys_sum
rent = toys_sum * 0.1
total_income = toys_sum - rent
amount_left = total_income - holiday_price
money_needed = abs(holiday_price - total_income)

if total_income >= holiday_price:
    print(f'Yes! {amount_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_needed:.2f} lv needed. ')

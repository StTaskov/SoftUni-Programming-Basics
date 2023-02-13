# •	Торта - 45 лв.
# •	Гофрета - 5.80 лв.
# •	Палачинка – 3.20 лв.
# 1/8 от крайната сума ще бъде използвана за покриване на разходите за продуктите по време на кампанията. Да се напише програма, която изчислява сумата, която е събрана в края на кампанията.
#1.	Броят на дните, в които тече кампанията – цяло число;
#2.	Броят на сладкарите – цяло число;
#3.	Броят на тортите – цяло число;
#4.	Броят на гофретите – цяло число;
#5.	Броят на палачинките – цяло число.

days_count = int(input())
confectioner_count = int(input())
cake_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

price_for_cake = cake_count * 45
price_for_waffles = waffles_count * 5.8
price_for_pancakes = pancakes_count * 3.2

price_per_day = (price_for_cake + price_for_waffles + price_for_pancakes) * days_count
all_price = price_per_day * confectioner_count

final_price =all_price - all_price/8

print(final_price)


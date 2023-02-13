#•	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
#•	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
#•	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
#•	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
#•	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
#•	Паламуд – 60% по-скъп от скумрията
#•	Сафрид – 80% по-скъп от цацата
#•	Миди – 7.50 лв. за килограм

sku_price = float(input())
caca_price = float(input())
pal_kg = float(input())
saf_kg = float(input())
mid_kg = int(input())

pal_price = sku_price + sku_price * 0.60
pal_sum = pal_kg * pal_price
saf_price = caca_price + caca_price * 0.80
saf_sum = saf_price * saf_kg
sum_mid = mid_kg * 7.5

sum_at_all = pal_sum + saf_sum + sum_mid

print(f'{sum_at_all:.2f}')



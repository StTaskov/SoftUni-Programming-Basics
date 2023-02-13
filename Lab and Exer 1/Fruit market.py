#	Цена на ягодите в лева – реално число;
#   Количество на банани в килограми - реално число;
#	Количество на портокалите в килограми – реално число;
#	Количество на малините в килограми – реално число;
#   Количество на ягодите в килограми – реално число.
# 	цената на  малините е на половина по-ниска от тази на ягодите;
# 	цената на портокалите е с 40% по-ниска от цената на малините;
# 	цената на бананите е с 80% по-ниска от цената на малините

strawberry_price = float(input())
bananas_count= float(input())
oranges_count = float(input())
raspberry_count = float(input())
strawberry_count = float(input())

raspberry_price = strawberry_price / 2
oranges_price = raspberry_price - raspberry_price * 0.4
bananas_price = raspberry_price - raspberry_price * 0.8

sum_raspberry = raspberry_count * raspberry_price
sum_oranges = oranges_count * oranges_price
sum_bananas = bananas_count * bananas_price
sum_strawbeerry = strawberry_count * strawberry_price

Final_sum = sum_raspberry + sum_oranges + sum_bananas + sum_strawbeerry

print(Final_sum)







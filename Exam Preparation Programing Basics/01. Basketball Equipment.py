year_pay = int(input())
basketball_shoes = year_pay - year_pay * 0.4
basketball_clothing = basketball_shoes - basketball_shoes * 0.2
basketball_ball = basketball_clothing / 4
basketball_accessories = basketball_ball / 5

sum = year_pay + basketball_shoes + basketball_clothing + basketball_ball + basketball_accessories

print(f"{sum:.2f}")

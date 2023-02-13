
budget = float(input())
extras = int(input())
price_for_extras = float(input())
decor = budget * 0.1

sum_for_extras = extras * price_for_extras
if extras > 150:
    sum_for_extras = sum_for_extras - sum_for_extras * 0.1

final_price_for_film = decor + sum_for_extras

if final_price_for_film > budget:
    print("Not enough save_money!")
    print(f"Wingard needs {final_price_for_film - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - final_price_for_film:.2f} leva left.")
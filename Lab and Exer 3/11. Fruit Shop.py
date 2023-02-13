fruit = input()
week_day = input()
count = float(input())

price = 0
sell = count * price
if week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday" or week_day == "Thursday" or week_day == "Friday":
    if fruit == "banana":
        price = 2.50
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "apple":
        price = 1.20
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "orange":
        price = 0.85
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "grapefruit":
        price = 1.45
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "kiwi":
        price = 2.70
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "pineapple":
        price = 5.50
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "grapes":
        price = 3.85
        sell = count * price
        print(f"{sell:.2f}")
    else:
        print('error')


elif week_day == "Saturday" or week_day == "Sunday":
    if fruit == "banana":
        price = 2.70
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "apple":
        price = 1.25
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "orange":
        price = 0.90
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "grapefruit":
        price = 1.60
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "kiwi":
        price = 3.00
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "pineapple":
        price = 5.60
        sell = count * price
        print(f"{sell:.2f}")
    elif fruit == "grapes":
        price = 4.20
        sell = count * price
        print(f"{sell:.2f}")
    else:
        print('error')


else:
    print("error")

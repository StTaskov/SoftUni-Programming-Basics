city = (input())
cell = float(input())

if city == 'Sofia':
    if 0 <= cell <= 500:
        print(f'{0.05 * cell:.2f}')
    elif 500 < cell <= 1000:
        print(f"{0.07 * cell:.2f}")
    elif 1000 < cell <= 10000:
        print(f"{0.08 * cell:.2f}")
    elif cell > 10000:
        print(f"{0.12 * cell:.2f}")
    else:
        print("error")

elif city == 'Varna':
    if 0 <= cell <= 500:
        print(f'{0.045 * cell:.2f}')
    elif 500 < cell <= 1000:
        print(f"{0.075 * cell:.2f}")
    elif 1000 < cell <= 10000:
        print(f"{0.10 * cell:.2f}")
    elif cell > 10000:
        print(f"{0.13 * cell:.2f}")
    else:
        print("error")

elif city == 'Plovdiv':
    if 0 <= cell <= 500:
        print(f'{0.055 * cell:.2f}')
    elif 500 < cell <= 1000:
        print(f"{0.08 * cell:.2f}")
    elif 1000 < cell <= 10000:
        print(f"{0.12 * cell:.2f}")
    elif cell > 10000:
        print(f"{0.145 * cell:.2f}")
    else:
        print("error")
else:
    print("error")
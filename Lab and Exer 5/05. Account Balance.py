increase = input()

final_sum = 0

while increase != "NoMoreMoney":
    increase = float(increase)
    if increase < 0:
        print("Invalid operation!")
        break
    else:
        final_sum += increase
        print(f"Increase: {increase:.2f}")
    increase = input()
print(f"Total: {final_sum:.2f} ")

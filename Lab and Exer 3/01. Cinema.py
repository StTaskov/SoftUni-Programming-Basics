type = input()
rows = int(input())
colons = int(input())

if type == "Premiere":
    print(f"{rows * colons * 12:.2f} leva")
elif type == "Normal":
    print(f"{rows * colons * 7.50:.2f} leva")
elif type == "Discount":
    print(f"{rows * colons * 5:.2f} leva")
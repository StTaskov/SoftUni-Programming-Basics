a = int(input())
b = int(input())
if a == b:
    print(a)
else:
    if a > b:
        a = a - b
        print(a)
    else:
        b = b - a
        print(b)

first_number = int(input())
second_number = int(input())
magic_number = int(input())
counter = 0

is_found = False

for first in range(first_number, second_number + 1):
    for second in range(first_number, second_number + 1):
        counter += 1
        if first + second == magic_number:
            is_found = True
            print(f"Combination N:{counter} ({first} + {second} = {magic_number})")
            break
    if is_found:
        break

if not is_found:
            print(f"{counter} combi nations - neither equals {magic_number}")
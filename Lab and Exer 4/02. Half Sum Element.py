import sys

n = int(input())  # 4

max_number = -sys.maxsize
total_sum = 0

for i in range(n):  # 0, 1, 2, 3
    number = int(input())
    if number > max_number:
        max_number = number
    total_sum += number

other_sum = total_sum - max_number
if other_sum == max_number:
    print(f'Yes\nSum = {max_number}')
    # print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number - other_sum)}')
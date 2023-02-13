n = int(input())


left_sum = 0
right_sum = 0

for i in range(n):
    number = int(input())
    left_sum += number

for j in range(n):
    num = int(input())
    right_sum += num

diff = abs(right_sum - left_sum)
if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")

else:
    print(f"No, diff = {diff}")
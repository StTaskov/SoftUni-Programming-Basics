import math
processors = int(input())
employee_count = int(input())
work_days = int(input())

total_hours = employee_count * work_days * 8
worked_processors = math.floor(total_hours / 3)

if worked_processors < processors:
    processors_less = processors - worked_processors
    losses = processors_less * 110.10
    print(f"Losses: -> {losses:.2f} BGN")
else:
    processors_more = worked_processors - processors
    profit = processors_more * 110.10
    print(f"Profit: -> {profit:.2f} BGN")
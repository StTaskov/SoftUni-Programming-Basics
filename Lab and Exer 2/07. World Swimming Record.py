import math
record = float(input())
distance = float(input())
time_for_one_meter = float(input())


all_time = time + delay

if all_time < record:
    print(f" Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
elif all_time > record:
    time_need = all_time - record
    print(f"No, he failed! He was {time_need:.2f} seconds slower.")
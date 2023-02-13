minutes = int(input())
seconds = int(input())
lenght = float(input())
seconds_for_100meters = int(input())

control_in_seconds = minutes * 60 + seconds
time_exist = lenght/120
all_of_time_exist = time_exist * 2.5
time = (lenght/100) * seconds_for_100meters - all_of_time_exist
needed_seconds = abs(control_in_seconds - time)

if time  <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {needed_seconds:.3f} second slower.")
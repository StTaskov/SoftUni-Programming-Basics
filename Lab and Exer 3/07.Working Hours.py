hour = int(input())
day = input()

is_working_hour = 10 <= hour <= 18
is_working_day = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday ' or day == "Saturday"

if is_working_day and is_working_hour:
    print("open")
else:
    print("closed")
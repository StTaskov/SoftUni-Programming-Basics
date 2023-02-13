# •	Първият ред съдържа час на изпита – цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита – цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане – цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане – цяло число от 0 до 59.

exam_hours = int(input())
exam_minutes = int(input())
student_hours = int(input())
student_minutes = int(input())

exam_time = exam_hours * 60 + exam_minutes
student_time = student_hours * 60 + student_minutes
diff = student_time - exam_time

hh = abs(diff) // 60
mm = abs(diff) % 60

if diff < -30:
    print("Early")
    if hh > 0:
        if mm < 10:
            print(f"{hh}:0{mm} hours before the start")
        else:
            print(f"{hh}:{mm} hours before the start")
    else:
        print(f"{mm} minutes before the start")
elif diff <= 0:
    print("On time")
    if not diff == 0:
        if hh > 0:
            print(f"{hh}:{mm:02d} hours before the start")
        else:
            print(f"{mm} minutes before the start")
else:
    print("Late")
    if hh > 0:
        print(f"{hh}:{mm:02d} hours after the start")
    else:
        print(f"{mm} minutes after the start")
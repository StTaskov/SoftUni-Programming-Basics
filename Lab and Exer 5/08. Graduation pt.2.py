name = input()
counter_class = 0
fails = 0
total_grades = 0

while counter_class < 12:
    grade = float(input())
    if grade >= 4:
        counter_class += 1
        fails = 0
        total_grades += grade
    else:
        fails +=1

    if fails == 2:
        print(f"{name} has been excluded at {counter_class + 1} grade")
        break

if counter_class == 12:
    print(f"{name} graduated. Average grade: {total_grades/12:.2f}")

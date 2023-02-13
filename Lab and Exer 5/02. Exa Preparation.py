fails = int(input())


counter = 0
total_grades = 0
grades_count = 0
last_ask_name = ""

name_problem = input()
while name_problem != "Enough":
    grade = int(input())
    total_grades += grade
    grades_count += 1
    last_ask_name = name_problem
    if grade <= 4:
        counter += 1
    if counter == fails:
        break
    name_problem = input()

if name_problem == "Enough":
    print(f"Average score: {total_grades/grades_count:.2f}")
    print(f"Number of problems: {grades_count}")
    print(f"Last problem: {last_ask_name}")
else:
    print(f"You need a break, {fails} poor grades.")


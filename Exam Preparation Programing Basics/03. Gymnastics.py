country = input()
device = input()
grade_for_diff = 0
grade_for_performance = 0
grade = grade_for_diff + grade_for_performance

if country == "Russia" and device == "ribbon":
    grade_for_diff = 9.100
    grade_for_performance = 9.400
elif country == "Russia" and device == "hoop":
    grade_for_diff = 9.300
    grade_for_performance = 9.800
elif country == "Russia" and device == "rope":
    grade_for_diff = 9.600
    grade_for_performance  = 9.000
elif country == "Bulgaria" and device == "ribbon":
    grade_for_diff = 9.600
    grade_for_performance = 9.400
elif country == "Bulgaria" and device == "hoop":
    grade_for_diff = 9.550
    grade_for_performance = 9.750
elif country == "Bulgaria" and device == "rope":
    grade_for_diff = 9.500
    grade_for_performance = 9.400
elif country == "Italy" and device == "ribbon":
    grade_for_diff = 9.200
    grade_for_performance = 9.500
elif country == "Italy" and device == "hoop":
    grade_for_diff = 9.450
    grade_for_performance = 9.350
elif country == "Italy" and device == "rope":
    grade_for_diff = 9.700
    grade_for_performance = 9.150

grade = grade_for_diff + grade_for_performance
percent = ((20 - grade) / 20) * 100

print(f"The team of {country} get {grade:.3f} on {device}.")
print(f"{percent:.2f}%")
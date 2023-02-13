month = input()
nights = int(input())

apartment_cost = 0
studio_cost = 0

if month in ('May', 'October'):
    apartment_cost = nights * 65
    studio_cost = nights * 50
    if nights > 14:
        apartment_cost = apartment_cost * 0.9
        studio_cost = studio_cost * 0.7
    elif nights > 7:
        studio_cost = studio_cost * 0.95
elif month in ('June', 'September'):
    apartment_cost = nights * 68.7
    studio_cost = nights * 75.2
    if nights > 14:
        apartment_cost = apartment_cost * 0.9
        studio_cost = studio_cost * 0.8
elif month in ('July', 'August'):
    apartment_cost = nights * 77
    studio_cost = nights * 76
    if nights > 14:
        apartment_cost = apartment_cost * 0.9

print(f'Apartment: {apartment_cost:.2f} lv.')
print(f'Studio: {studio_cost:.2f} lv.')

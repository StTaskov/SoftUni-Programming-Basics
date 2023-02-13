budget = float(input())
season = input()
place = ''
type = ''

if budget <= 100:
    place = 'Bulgaria'
    if season == "summer":
        type = 'Camp'
        budget = budget * 0.30
    elif season == "winter":
        type = 'Hotel'
        budget = budget * 0.70

elif budget <= 1000:
    place = 'Balkans'
    if season == "summer":
        type = 'Camp'
        budget = budget * 0.40
    elif season == "winter":
        type = 'Hotel'
        budget = budget * 0.80
else:
    place = 'Europe'
    if season == "summer" or season == "winter":
        type = 'Hotel'
        budget = budget * 0.90

print(f"Somewhere in {place}")
print(f"{type}–({budget:2.f})")

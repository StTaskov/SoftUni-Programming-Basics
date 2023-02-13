stage = input()
type_ticket = input()
count_ticket = int(input())
photo = input()
ticket_sell = 0
sell_from_photo = 0

if stage == "Quarter final" and type_ticket == "Standard":
    ticket_sell = 55.50
elif stage == "Quarter final" and type_ticket == "Premium":
    ticket_sell = 105.20
elif stage == "Quarter final" and type_ticket == "VIP":
    ticket_sell = 118.90

elif stage == "Semi final" and type_ticket == "Standard":
    ticket_sell = 75.88
elif stage == "Semi final" and type_ticket == "Premium":
    ticket_sell = 125.22
elif stage == "Semi final" and type_ticket == "VIP":
    ticket_sell = 300.40

elif stage == "Final" and type_ticket == "Standard":
    ticket_sell = 110.10
elif stage == "Final" and type_ticket == "Premium":
    ticket_sell = 160.66
elif stage == "Final" and type_ticket == "VIP":
    ticket_sell = 400

sell = ticket_sell * count_ticket

if photo == "Y":
    sell_from_photo = count_ticket * 40
    if sell > 4000:
        sell_from_photo = 0
        sell -= sell * 0.25
    elif sell > 2500:
        sell -= sell * 0.1

else:
    if sell > 4000:
        sell_from_photo = 0
        sell -= sell * 0.25
    elif sell > 2500:
        sell -= sell * 0.1

print(f"{sell + sell_from_photo:.2f}")

team = input()
type_souvenir = input()
count_souvenirs = int(input())
price = 0

if team == "Argentina":
    if type_souvenir == "flags":
        price = 3.25
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "caps":
        price = 7.20
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "posters":
        price = 5.10
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "stickers":
        price = 1.25
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    else:
        print("Invalid stock!")
elif team == "Brazil":
    if type_souvenir == "flags":
        price = 4.20
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "caps":
        price = 8.50
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "posters":
        price = 5.35
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "stickers":
        price = 1.20
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    else:
        print("Invalid stock!")
elif team == "Croatia":
    if type_souvenir == "flags":
        price = 2.75
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "caps":
        price = 6.90
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "posters":
        price = 4.95
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "stickers":
        price = 1.10
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    else:
        print("Invalid stock!")
elif team == "Denmark":
    if type_souvenir == "flags":
        price = 3.10
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "caps":
        price = 6.50
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "posters":
        price = 4.80
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    elif type_souvenir == "stickers":
        price = 0.90
        total_sum = price * count_souvenirs

        print(f'Pepi bought {count_souvenirs} {type_souvenir} of {team} for {total_sum:.2f} lv.')
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")

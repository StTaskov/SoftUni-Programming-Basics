import math
tennis_racket = float(input())
racket_count = int(input())
shoes_count = int(input())

tennis_shoes = tennis_racket / 6
racket_sell = racket_count * tennis_racket
shoes_sell = tennis_shoes * shoes_count

other_equipment = (racket_sell + shoes_sell) * 0.2

sum_for_all = racket_sell + shoes_sell + other_equipment

print(f"Price to be paid by Djokovic {math.floor(sum_for_all/8)}")
print(f"Price to be paid by sponsors {math.ceil((sum_for_all * 7/8))}")

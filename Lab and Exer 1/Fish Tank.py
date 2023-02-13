#Дължина в см – цяло число
#Широчина в см – цяло число
#Височина в см – цяло число
#Процент зает обем – реално число

a = int(input())
b = int(input())
c = int(input())
percent_of_V = float(input())

V = a * b * c
all_liters = V * 0.001
percent_busy = percent_of_V * 0.01
all_liters_need = all_liters * (1-percent_busy)

print(all_liters_need)





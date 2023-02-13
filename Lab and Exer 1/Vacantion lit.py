#	Брой страници в текущата книга – цяло число;
#	Страници, които може да прочита за 1 час – цяло число;
#	Броя на дните, за които трябва да прочете книгата – цяло числ

pages = float(input())
pages_per_hour = float(input())
days = float(input())

total_pages = pages / pages_per_hour
total_days = total_pages / days

print(total_days)
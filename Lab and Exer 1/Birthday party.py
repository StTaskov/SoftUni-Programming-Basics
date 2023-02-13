#	Торта  – цената ѝ е 20% от наема на залата
#	Напитки – цената им е 45% по-малко от тази на тортата
#	Аниматор – цената му е 1/3 от цената за наема на залата

hall = int(input())
cake = hall*0.2
drinks = cake - cake*0.45
animators = hall/3

sum = hall + cake + drinks + animators

print(sum)



destination = input()


while destination != "End":
    min_budget = float(input())
    budget = 0
    while budget < min_budget:
        sum = float(input())
        budget += sum
    else:
        print(f"Going to {destination}!")
    destination = input()
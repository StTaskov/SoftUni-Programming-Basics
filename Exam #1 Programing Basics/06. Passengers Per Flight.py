import math


count_airline = int(input())
the_most_passangers = 0
the_most_passanger_airlane = ""
for airline in range(1, count_airline+1):
    airline_name = input()
    all_passangers = 0
    average = 0
    count_of_flight = 0
    command = input()
    while command != "Finish":
        count_of_passengers = int(command)
        all_passangers += count_of_passengers
        count_of_flight += 1
        command = input()
    average = all_passangers / count_of_flight
    print(f"{airline_name}: {math.floor(average)} passengers.")
    if average > the_most_passangers:
        the_most_passangers = average
        the_most_passanger_airlane = airline_name
print(f"{the_most_passanger_airlane} has most passengers per flight: {math.floor(the_most_passangers)}")
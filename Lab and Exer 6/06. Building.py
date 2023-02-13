count_of_stairs = int(input())
count_of_rooms = int(input())

for stairs in range(count_of_stairs, 0, -1):
    for room in range(0, count_of_rooms):
        if stairs == count_of_stairs:
            print(f"L{stairs}{room}", end=" ")
        elif stairs % 2 == 0:
            print(f"O{stairs}{room}", end=" ")
        elif stairs % 2 == 1:
            print(f"A{stairs}{room}", end=" ")
    print("")
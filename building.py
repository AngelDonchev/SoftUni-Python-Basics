floors = int(input())
rooms = int(input())
counter = 0

for i in range(floors, 0, -1):
    for j in range(rooms):
        if i == floors:
            print(f"L{i}{j} ", end="")
        else:
            if j == 0:
                print()
            if i % 2 == 0:
                print(f"O{i}{j} ", end="")
            else:
                print(f"A{i}{j} ", end="")

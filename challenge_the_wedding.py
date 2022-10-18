man = int(input())
woman = int(input())
tables = int(input())
counter = 0
flag = False

for men in range(1, man + 1):
    for women in range(1, woman + 1):
        print(f"({men} <-> {women})", end=" ")
        counter += 1
        if tables == counter:
            flag = True
            break
    if flag:
        break

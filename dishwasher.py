bottles = int(input())
dishes = input()
soap_left = bottles * 750
n = 1
pots = 0
dishes_washed = 0
detergent = 0
flag = True

while dishes != "End":
    dishes = int(dishes)
    if n % 3 == 0:
        detergent = 15
        pots += dishes
    else:
        detergent = 5
        dishes_washed += dishes
    if soap_left >= dishes * detergent:
        n += 1
        soap_left -= dishes * detergent
    else:
        print(f"Not enough detergent, {detergent * dishes - soap_left} ml. more necessary!")
        flag = False
        break
    dishes = input()
if flag:
    print("Detergent was enough!")
    print(f"{dishes_washed} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {soap_left} ml.")

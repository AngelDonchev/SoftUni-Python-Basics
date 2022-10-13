junior_cyclist = int(input())
senior_cyclist = int(input())
track_type = input()

junior_tax = 0
senior_tax = 0
flag = False

if track_type == "trail":
    junior_tax = 5.50
    senior_tax = 7
elif track_type == "cross-country":
    junior_tax = 8
    senior_tax = 9.50
    flag = True
elif track_type == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
elif track_type == "road":
    junior_tax = 20
    senior_tax = 21.50

total_tax_collected = junior_tax * junior_cyclist + senior_tax * senior_cyclist
if junior_cyclist + senior_cyclist >= 50 and flag:
    total_tax_collected -= total_tax_collected * 0.25

print(f"{(total_tax_collected - total_tax_collected * 0.05):.2f}")

chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
discount_flower = 0
discount_number = 0
additional_cost = 0

if holiday == "Y":
    additional_cost = 0.15
if tulips > 7 and holiday == "Y" and season == "Spring":
    discount_flower += 0.05
if roses >= 10 and season == "Winter":
    discount_flower += 0.10
if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
if roses + tulips + chrysanthemum > 20:
    discount_number += 0.20

total_price = chrysanthemum * chrysanthemum_price + roses * roses_price + tulips * tulips_price
total_price += total_price * additional_cost
total_price -= total_price * discount_flower
total_price -= total_price * discount_number
print(f"{(total_price + 2):.2f}")

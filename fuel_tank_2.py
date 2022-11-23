fuel_type = input()
fuel_volume = float(input())
club_card = input()
fuel_price = 0

if club_card == "Yes":
    if fuel_type == "Gas":
        fuel_price = fuel_volume * 0.85
    elif fuel_type == "Gasoline":
        fuel_price = fuel_volume * 2.04
    elif fuel_type == "Diesel":
        fuel_price = fuel_volume * 2.21
else:
    if fuel_type == "Gas":
        fuel_price = fuel_volume * 0.93
    elif fuel_type == "Gasoline":
        fuel_price = fuel_volume * 2.22
    elif fuel_type == "Diesel":
        fuel_price = fuel_volume * 2.33

if 20 <= fuel_volume <= 25:
    fuel_price = fuel_price - fuel_price * 0.08
elif fuel_volume > 25:
    fuel_price = fuel_price - fuel_price * 0.1
print(f"{fuel_price:.2f} lv.")

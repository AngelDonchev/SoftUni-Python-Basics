budget = float(input())
season = input()
car = ""
car_class = ""
cost = 0
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        cost = 0.35 * budget
    elif season == "Winter":
        car = "Jeep"
        cost = 0.65 * budget
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        cost = 0.45 * budget
    elif season == "Winter":
        car = "Jeep"
        cost = 0.80 * budget
elif budget > 500:
    car_class = "Luxury class"
    car = "Jeep"
    cost = 0.90 * budget
print(car_class)
print(f"{car} - {cost:.2f}")


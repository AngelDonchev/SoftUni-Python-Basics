months = int(input())

electricity_bill = 0
water_bill = 0
internet_bill = 0
others_bill = 0

for _ in range(months):
    electricity_monthly_bill = float(input())
    electricity_bill += electricity_monthly_bill
    water_bill += 20
    internet_bill += 15
    others_bill += (electricity_monthly_bill + 35) * 1.2

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others_bill:.2f} lv")
print(f"Average: {((electricity_bill + water_bill + internet_bill + others_bill)/ months):.2f} lv")

legacy_money = float(input())
life_expectancy = int(input())
money_spent = 0

for year in range(1800, life_expectancy + 1):
    if year % 2 == 0:
        money_spent += 12000
    else:
        money_spent += (12000 + 50 * (18 + year - 1800))
if legacy_money >= money_spent:
    print(f"Yes! He will live a carefree life and will have {(legacy_money - money_spent):.2f} dollars left.")
else:
    print(f"He will need {(money_spent - legacy_money):.2f} dollars to survive.")

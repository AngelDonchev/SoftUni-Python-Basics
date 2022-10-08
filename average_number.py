n = int(input())
numbers = 0
for _ in range(n):
    numbers += float(input())
print(f"{numbers / n:.2f}")

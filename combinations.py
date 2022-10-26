n = int(input())
counter = 0
for i in range(n + 1):
    for j in range(n + 1):
        for m in range(n + 1):
            if n == i + j + m:
                counter += 1
print(counter)

n = int(input())

sum_1_2 = 0
sum_3_4 = 0
equal_difference = 0
compare_difference = 0

if n != 1:

    for counter in range(n):
        num_1 = int(input())
        num_2 = int(input())

        if counter % 2 == 0:
            sum_1_2 = num_1 + num_2
        else:
            sum_3_4 = num_1 + num_2

        if counter == 0:
            continue

        if sum_1_2 == sum_3_4:
            difference = 0
            equal_difference += 1
        elif sum_1_2 > sum_3_4:
            difference = sum_1_2 - sum_3_4
        else:
            difference = sum_3_4 - sum_1_2

        if compare_difference <= difference:
            compare_difference = difference

    if equal_difference == n - 1:
        print(f"Yes, value={sum_1_2}")
    else:
        print(f"No, maxdiff={compare_difference}")
else:
    num_1 = int(input())
    num_2 = int(input())
    print(f"Yes, value={num_1 + num_2}")

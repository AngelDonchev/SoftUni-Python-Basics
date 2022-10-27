number_1 = int(input())
number_2 = int(input())

for i in range(number_1, number_2 + 1):
    i_to_str = str(i)
    sum_even = 0
    sum_odd = 0

    for j, digit in enumerate(i_to_str):
        if j % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    if sum_even == sum_odd:
        print(i, end=" ")


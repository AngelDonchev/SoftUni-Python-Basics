movie_name = input()
student_seats = 0
standard_seats = 0
kid_seats = 0
total_seats_sold = 0
total_student_seats = 0
total_standard_seats = 0
total_kid_seats = 0
while movie_name != "Finish":
    free_seats = int(input())
    for sold_seats in range(free_seats):
        type_of_seat = input()
        if type_of_seat == "End":
            break
        elif type_of_seat == "student":
            student_seats += 1
        elif type_of_seat == "standard":
            standard_seats += 1
        elif type_of_seat == "kid":
            kid_seats += 1
    total_movie_seats_sold = standard_seats + student_seats + kid_seats
    total_student_seats += student_seats
    total_standard_seats += standard_seats
    total_kid_seats += kid_seats
    total_seats_sold += total_movie_seats_sold
    print(f"{movie_name} - {(total_movie_seats_sold / free_seats * 100):.2f}% full.")
    student_seats = 0
    standard_seats = 0
    kid_seats = 0
    movie_name = input()

print(f"Total tickets: {total_seats_sold}")
print(f"{(total_student_seats / total_seats_sold * 100):.2f}% student tickets.")
print(f"{(total_standard_seats / total_seats_sold * 100):.2f}% standard tickets.")
print(f"{(total_kid_seats / total_seats_sold * 100):.2f}% kids tickets.")

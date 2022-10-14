number_pages = int(input())
reading_speed = int(input())
days_left = int(input())
hours_per_day = number_pages//reading_speed//days_left
print(hours_per_day)
# Match Case - Switch Case
# day_of_the_week
# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# ...
# ...

# day_of_the_week = 4

# if day_of_the_week == 0:
#     print("Monday")
# elif day_of_the_week == 1:
#     print("Tuesday")

# match day_of_the_week:
#     case 0:
#         print("Monday")
#     case 1:
#         print("Tuesday")
#     case 2:
#         print("Wednesday")
#     case 3:
#         print("Thursday")
#     case 4:
#         print("Friday")
#     case 5:
#         print("Saturday")
#     case _:
#         print("Sunday")

# 0, 1, 2, 3, 4 -> Weekday
# 5, 6 -> Weekend

day_of_the_week = 12

match day_of_the_week:
    case 0 | 1 | 2 | 3 | 4:
        print("Weekday")
    case 5 | 6:
        print("Weekend")
    case _:
        print("Invalid day number")
days_dict = {"Monday": 12, "Tuesday": 12, "Wednesday": 14,
             "Thursday": 14, "Friday": 12, "Saturday": 16, "Sunday": 16}
day = input()

if day in days_dict:
    print(days_dict[day])
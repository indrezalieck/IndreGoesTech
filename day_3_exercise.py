import datetime
my_name = input("Hi dear what is your name? ")
my_age = input(f"How old are you {my_name}?")
age_2 = 100 - int(my_age)
print(f"You will be 100 in {age_2} years. ")

print("Current year is", datetime.datetime.now().year)
year_2 = 100 - int(my_age) + datetime.datetime.now().year
print(f"You will be 100 years in {year_2} my love")
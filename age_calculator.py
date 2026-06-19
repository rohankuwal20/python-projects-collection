# age calculator
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))
if birth_year > current_year:
    print("Error: Birth year cannot be greater than current year.")
elif birth_year < 0 or current_year < 0:
    print("Error: Year cannot be negative.")
elif birth_year == current_year:
    print("You are born this year! Your age is 0.")
else:
    age = current_year - birth_year
    print("Your age is:", age)
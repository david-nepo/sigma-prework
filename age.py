from datetime import datetime

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
    current_date = datetime.now()

    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

    return age

birth_date = input("Enter your birthdate (dd-mm-yyy): ")
age = calculate_age(birth_date)

print(f"\nYou are {age} years old.")
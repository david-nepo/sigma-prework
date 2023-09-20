from datetime import datetime

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
    current_date = datetime.now()

    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

    return age

# print(calculate_age('04-12-1972'))

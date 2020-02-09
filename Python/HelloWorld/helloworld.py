from datetime import date, datetime, timedelta

# Collect the user's first name
first_name = input('What is your first name?')
first_name = first_name.capitalize()

# Collect the user's last name
last_name = input('What is your last name?')
last_name = last_name.capitalize()

# Print out a friendly greeting to the user
print(f'Hello, {first_name} {last_name}!')

try:
    # Collect the user's birth
    birth_date = input('When is your birthday? (mm/dd/yyyy) ')
    birth_date = datetime.strptime(birth_date, '%m/%d/%Y')

    # Get the current date
    current_date = date.today()

    next_birthday = date(current_date.year, birth_date.month, birth_date.day)


    if next_birthday < current_date:
        next_birthday.replace(year=current_date.year + 1)

    days_remaining = next_birthday - current_date

    print(f'Today is {current_date.strftime("%m/%d/%Y")}.')
    print(f'Your birthday is in {days_remaining.days} day(s)!')
except Exception as e:
    print('There was an error with your birthday!')
    print(e)




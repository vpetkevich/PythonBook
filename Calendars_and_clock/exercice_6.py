from datetime import date, timedelta
birthday = date(1994, 3, 5)
guess_year = birthday + timedelta(days=10000)
print(guess_year)

from datetime import datetime
my_dates = ['5-Nov-18', '25-Mar-17', '1-Nov-18', '7-Mar-17']
my_dates.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
print(my_dates)

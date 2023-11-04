from datetime import datetime
from collections import defaultdict 


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays_by_day = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year + 1 
        delta_days = (birthday_this_year - today).days
        delta_days < 7
        birthdays_by_day.append(name)
       


    result = []
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#print(user)
users = {"name": "Bill Gates1", "birthday": datetime(1955, 10, 28), 
 "name": "Bill Gates2", "birthday": datetime(1965, 10, 30),
 "name": "Bill Gates3", "birthday": datetime(1975, 11, 2)}    
res = get_birthdays_per_week(users)
print(res)    

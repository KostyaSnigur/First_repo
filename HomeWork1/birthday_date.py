from datetime import datetime
from collections import defaultdict 


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays_by_day = defaultdict(list)
    for user in users:
        print(user)
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year + 1 
        delta_days = (birthday_this_year - today).days
        delta_days < 7
        birthdays_by_day.append(name)
       


    result = []

#print(user)
users = {"name": "Bill Gates1", "birthday": datetime(1955, 10, 28), 
 "name": "Bill Gates2", "birthday": datetime(1965, 10, 30),
 "name": "Bill Gates3", "birthday": datetime(1975, 11, 2)}    
res = get_birthdays_per_week(users)
print(res)    
              # b. Оцінка Дати на Цей Рік : Перевіряємо, чи вже минув день народження цього року 
#    if birthday_this_year < today 
#    Якщо так, то розглядаємо дату на наступний рік, це треба у 
#    birthday_this_year + 1 
       #використовуючи метод replace збільшити рік на одиничку. 
       # c. Порівняння з Поточною Датою: Визначаємо різницю між днем народження та поточним днем, 
       # щоб знайти дні народження на тиждень вперед 
#   delta_days = (birthday_this_year - today).days
       # d. Визначення Дня Тижня: Визначаємо день тижня дня народження. 
       # Якщо це вихідний, переносимо на понеділок. 
       # Тут треба подивитись, щоб delta_days < 7, перед тим як визначити на який день ставимо поздоровлення.

#    delta_days < 7
       #Зберігання Результату : Зберігаємо ім'я користувача в відповідний день тижня, якщо день народження відбувається протягом наступного тижня.
       #Виведення Результату: Виводимо зібрані імена по днях тижня у відповідному форматі.
   #print.
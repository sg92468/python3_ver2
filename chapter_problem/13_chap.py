# # 13.1 うるう年
# import calendar
# print(calendar.isleap(1900))
# print(calendar.isleap(1996))

# # 13.2 datetimeモジュール
# from datetime import date
# halloween = date(2019, 10, 31)
# print(halloween)
# print(halloween.day)
# print(halloween.month)
# print(halloween.year)

# from datetime import date
# now = date.today()
# print(now)

# from datetime import timedelta
# one_day = timedelta(days=1)
# tomorrow = now + one_day
# print(tomorrow)

# from datetime import time
# noon = time(12, 0, 0) # time(hour, minute, second)
# print(noon)
# print(noon.hour)

# from datetime import datetime
# some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
# print(some_day)
# print(datetime.now())
# print(datetime.now().microsecond)

# # 13.3 timeモジュール
# import time
# now = time.time()
# print(now)
# print(time.ctime(now))
# print(time.localtime(now))
# print(time.gmtime(now)[0])

# tm = time.localtime(now)
# print(time.mktime(tm))

# # 13.4 日時の読み書き
# import time
# now = time.time()
# print(time.ctime(now))

# fmt = "It's %A, %B %d, %Y, local time %T:%M:%S%p"
# t = time.localtime()
# print(time.strftime(fmt, t))

# from datetime import date
# some_day = date(2019, 7, 4)
# print(some_day.strftime(fmt))

# import locale
# from datetime import date
# halloween = date(2019, 10, 31)
# for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is']:
#     locale.setlocale(locale.LC_TIME, lang_country)
#     print(halloween.strftime('%A, %B %d'))

# import locale
# names = locale.locale_alias.keys()

# good_names = [name for name in names if len(name) == 5 and name[2] == '_']
# print(good_names[:5])
# de = [name for name in good_names if name.startswith('de')]
# print(de)

# q13.1
from datetime import date, datetime
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'w') as output:
    print(now_str, file=output)

# q13.2
with open('today.txt', 'r') as input:
    today_string = input.read()

print(today_string)

# q13.3
# fmt = '%Y-%m-%d'
# print(datetime.strftime(today_string, fmt))

# q13.4
my_dirth = date(1994, 6, 8)
print(my_dirth)

# q13.5
print(my_dirth.weekday())

# q13.6
from datetime import timedelta
path_day = my_dirth + timedelta(days=10000)
print(path_day)
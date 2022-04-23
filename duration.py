duration = int(input("Введите время в секундах для дальнейшего вычисления: "))
minutes = duration // 60
ost_min = duration - (minutes * 60)
hour = minutes // 60
ost_hour = (duration - (hour * 3600))//60
days = duration // 86400
ost_days = (duration - (days * 24 * 3600))//3600

if duration <= 60:
    print(duration, "сек")
if 60 < duration <= 3600:
    print(minutes, "мин", ost_min, "сек")
if 3600 < duration <= 86400:
    print(hour, "час", ost_hour, "мин", ost_min, "сек")
if 86400 < duration <= 604800:
    print(days, "д", ost_days, "час", ost_hour, "мин", ost_min, "сек")
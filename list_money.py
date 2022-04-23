# добавим магии математики
import math
# наши цены...
my_price = [57.8, 46.51, 97, 91.25, 12.60, 4.48, 11.23, 65.35]

for el in my_price:
    b = el * 100
    a = math.floor(b // 100)
    m = math.floor(b % 100)
    print(a, "руб", m, "коп")

# отобразим самую высокую цену
print("Самая высокая цена в прайсе: ", max(my_price))

# создаим новый список из старого и отсортируем по убыванию
my_price_lower = sorted(my_price)
my_price_lower.sort(reverse = True)
print(my_price_lower)

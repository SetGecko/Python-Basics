# заводим список чисел
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# делаем генератор с выборкой уникальных значений
sorted_list = [src[i] for i in range(len(src)) if i == src.index(src[i])]
print(sorted_list)

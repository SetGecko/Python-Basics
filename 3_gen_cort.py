# создадим списки
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
    ]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

# сделаем кортеж из ранее созданных списков по ключам
my_class_list = tuple(zip(tutors, klasses))
# создадим генератор из ранее созданного общего списка
my_class = (x for x in my_class_list)

# теперь будем вызывать элементы генератора пока не увидим стоп сигнал StopIteration - 8 вызов, т.к. при создании
# кортежа dict обрезал повторяющиеся элементы
print(next(my_class))
print(next(my_class))
print(next(my_class))
print(next(my_class))
print(next(my_class))
print(next(my_class))
print(next(my_class))
print(next(my_class))


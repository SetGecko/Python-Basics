# в наличии
broken_list = ['инженер-конструктор Игорь',
               'главный бухгалтер МАРИНА',
               'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

print(broken_list)


# каждый элемент списка делаем строкой

first_str = ''.join(broken_list[0])
second_str = ''.join(broken_list[1])
third_str = ''.join(broken_list[2])
fourth_str = ''.join(broken_list[3])

# все слова в строках делаем с маленькой буквы

first_str = str.lower(first_str)
second_str = str.lower(second_str)
third_str = str.lower(third_str)
fourth_str = str.lower(fourth_str)

# теперь каждую строку сделаем списком, но с разделением пробелов, длс создания элементов списка

correct_list1 = first_str.split(' ')
correct_list2 = second_str.split(' ')
correct_list3 = third_str.split(' ')
correct_list4 = fourth_str.split(' ')

# приводим каждый элемент списка к большой букве
# сейчас 4:30 утра...я пишу говнокод и понимаю это :))) всё можно было через for, но блин я так хочу спать...

correct_list1 = [x.title() for x in correct_list1]
correct_list2 = [x.title() for x in correct_list2]
correct_list3 = [x.title() for x in correct_list3]
correct_list4 = [x.title() for x in correct_list4]

"""
мы знаем, что каждый поледний элемент списка это имя - кроме 4, 
но нужно поприветствовать по условию..хз может Аэлита тоже имя...
"""

print('Привет, ', correct_list1[-1], '!')
print('Привет, ', correct_list2[-1], '!')
print('Привет, ', correct_list3[-1], '!')
print('Привет, ', correct_list4[-1], '!')

# сделаем проверяшкю полложительности
def add_zero(x):
    if x[0] in '+-':
        return x[0]


# теперь сам злополучный список
super_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# добавим слева 0 и проверим на знак первого символа
i = 0
while i < len(super_list):
    sign = add_zero(super_list[i])
    if super_list[i].isdigit() or (sign and super_list[i][1:].isdigit()):
        if sign:
            super_list[i] = sign + super_list[i][1:].zfill(2)
        else:
            super_list[i] = super_list[i].zfill(2)

        super_list.insert(i, '"')
        super_list.insert(i + 2, '"')
        i += 2
    i += 1

# конвертим всё в строку, с разделителем в 1 пробел
super_string = ' '.join(super_list)
print(super_string)

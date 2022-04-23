proverka = input("Введите вашу переменную: ")
if [i for i in proverka if i in '1234567890']:
    print("В вашей переменной есть цифры :)")
else:
    print("В вашей переменной нет цифр :(")
def summa_chisel(value):
    res = 0
    while value != 0:
        res += value % 10
        value //= 10
    return res

spisok = [i**3 for i in range(1, 1001, 2)]
result_1 = sum(filter(lambda num: summa_chisel(num) % 7 == 0, spisok))
result_2 = sum(filter(lambda num: summa_chisel(num + 17) % 7 == 0, spisok))
print(result_1)
print(result_2)
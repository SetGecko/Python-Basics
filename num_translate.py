one = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
       6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}


def num_translate(s):
    if 0 < s < 11:
        print(one[s])
    else:
        print('None')


num_translate(1)

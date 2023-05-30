from random import randint
wramount = 0
riamount = 0
while wramount < 3:
    a = randint(1, 100)
    b = randint(1, 100)
    res = int(input(str(a) + '+' + str(b) + '='))
    if res != a + b:
        print('ответ неверный')
        wramount += 1
    else:
        print('Правильно!')
        riamount += 1
    if wramount == 3:
        print('игра окончена. Правильных ответов:', riamount)

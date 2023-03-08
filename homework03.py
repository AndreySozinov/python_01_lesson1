# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY_AMOUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, TRY_AMOUNT + 1):
    try_num = int(input(f"Попытка {i}. Какое число я загадал? "))
    if num < try_num and i < 10:
        print("Меньше. ")
    elif num > try_num and i < 10:
        print("Больше. ")
    elif i == 10:
        print("Попытки кончились.")
    else:
        print("Угадал!")
        break

# Задача 3. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

quarterNumber = int(input('Enter the number of quarter (1 / 2 / 3 / 4)\n'))

if (quarterNumber < 1 or 4 < quarterNumber):
    print('Incorrect input')

if (quarterNumber == 1):
    print('1 -> x > 0, y > 0')

if (quarterNumber == 2):
    print('2 -> x < 0, y > 0')

if (quarterNumber == 3):
    print('3 -> x < 0, y < 0')

if (quarterNumber == 4):
    print('4 -> x > 0, y < 0')

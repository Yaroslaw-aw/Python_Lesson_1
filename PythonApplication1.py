# Задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение


n = int(input('Enter the number of day: '))
if (n < 1 or n > 7):
    print('There is no such day')

if (n == 1):
    print('Monday')
        
if (n == 2):
    print('Tuesday')
        
if (n == 3):
    print('Wednesday')
    
if (n == 4):
    print('Thursday')
        
if (n == 5):
    print('Friday')
        
if (n == 6):
    print('Saturday')
        
if (n == 7):
    print('Sunday')
        
   



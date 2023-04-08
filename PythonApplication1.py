# Задача 2. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
        
import math


x1 = int(input('Enter the x coordinate of A point: '))
y1 = int(input('Enter the y coordinate of A point: '))
x2 = int(input('Enter the x coordinate of B point: '))
y2 = int(input('Enter the y coordinate of B point: '))

r = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

print(f'Distance between points A and B: ', round(r, 2))
    
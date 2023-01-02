# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def plane (x,y):

    if (x > 0 and y > 0 ):
        print(f'x={x} и y={y} расположены в 1-й четверти')
    elif (x < 0 and y > 0):
        print(f'x={x} и y={y} расположены во 2-й четверти')
    elif (x < 0 and y < 0):
        print(f'x={x} и y={y} расположены в 3-й четверти')
    elif(x == 0 and y ==0):
        print(f'x={x} и y={y} расположены в центре оси координат')
    else:
        print(f'x={x} и y={y} расположены в 4-й четверти')

print('Введите следующие числа чтобы узнать в какой четверти оси координат они находятся')
x = float(input('Введите значение Х,:'))
y = float(input('Введите значение Y:'))

plane(x, y)
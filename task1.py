# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('введите день недели от 1 до 7: '))

while day > 7 or day < 1:
    print('Такого дня недели не существует')
    break
if day == 6 or day == 7:
    print('Это выходной день')
else:
    print('Это рабочий день')
# не получается сделать так чтобы после break функция не уходила в else/if, но иначе не получается
# чтобы числа дня недели более и менее 1 и 7 выводятся как рабочие (пробовал как у Вас на семинаре изначально)


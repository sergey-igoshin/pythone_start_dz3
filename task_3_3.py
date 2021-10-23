"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
аргументов.
"""


def my_func(num1, num2, num3):
    list_num = [num1, num2, num3]
    list_num.remove(min(list_num))
    return f'Сумма наибольших двух аргументов = {sum(list_num)}'


print(my_func(int(input('Первое число: ')), int(input('Второе число: ')), int(input('Третье число: '))))

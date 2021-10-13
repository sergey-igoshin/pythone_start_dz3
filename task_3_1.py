"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(divisible, divider):
    try:
        return f'Частное: {int(divisible) / int(divider)}'
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


print(my_func(input("Делимое: "), input("Делитель: ")))

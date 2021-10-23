"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


def my_func(**kwargs):
    return ' '.join([kwargs['f'], kwargs['l'], kwargs['y'], kwargs['c'], kwargs['e'], kwargs['p']])


first_name = input('Имя: ')
last_name = input('Фамилия: ')
year = input('Год рождения: ')
city = input('Город проживания: ')
email = input('E-mail: ')
phone = input('Телефон: ')

print(my_func(f=first_name, l=last_name, y=year, c=city, e=email, p=phone))

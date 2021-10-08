# 1.    Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#       Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func_div():
    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))
    try:

    except ZeroDivisionError:
        return
    return number_1 / number_2


print(func_div())

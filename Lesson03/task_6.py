# 6, 7  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
#       прописной первой буквой. Продолжить работу над заданием. В программу должна попадать строка из слов,
#       разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
#       но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее
#       функцию int_func().

def int_func(word):
    lat = "qwertyuiopasdfghjklzxcvbnm"
    return print(word.title()) if not set(word).difference(lat) else False


words = input("Введите строку латинскими буквами ").split()
for i in words:
    result = int_func(i)
    if result:
        print(int_func(i), " ")

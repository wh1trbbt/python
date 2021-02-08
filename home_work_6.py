# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(a):
    code = list(map(ord, a))
    rus = [1040 < x < 1106 for x in code].count(True)
    if a.islower() and rus == 0:
        return a.title()
    else:
        return 'Так не работает!'


print(int_func('text'))
print(int_func('hello python'))
print(int_func('texT'))
print(int_func('hellO pYTHon'))
print(int_func('текст'))
print(int_func('привет python'))
print(int_func('ё'))

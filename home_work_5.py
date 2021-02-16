# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('task_5.txt', 'w', encoding='utf-8') as f:
    try:
        numbers = input("Ввести числа через пробел: ")
        f.write(numbers)
        print(sum(map(float, numbers.split())))
    except ValueError:
        print('Где-то закралось не число')

# 2. Пользователь вводит время в секундах.

a = int(input('Введите время в секундах: '))

# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

h = a // 3600
m = (a - h * 3600) // 60
s = a - h * 3600 - m * 60
time = f'{h:02}:{m:02}:{s:02}'

print(time)

# 3. Узнайте у пользователя число n.

n = input('Введите число: ')

# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

nn = n + n
nnn = n + n + n

result = int(n) + int(nn) + int(nnn)

print(result)

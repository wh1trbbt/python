# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.


from translate import Translator
translator = Translator(from_lang='en', to_lang='ru')

with open('task_4.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    result = translator.translate(content)
    print(result)

with open('task_4_ru.txt', 'w', encoding='utf-8') as f:
    f.write(result)




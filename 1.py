import re
print("Задание 5.1")
text="Предложение с точкой. Предложение с восклицательным знаком! Предложение с вопросительным знаком? Предложение с многоточием …"
a=re.split(r"(?<=[.!?…])", text)
print(a)
print("Задание 5.2")
print("Введите текст:")
text2=input()
b=re.sub(r"[редиск]","давайте жить дружно", text2)
c=re.sub(r"[нехорош человек]", "давайте жить дружно", b)
print(c)

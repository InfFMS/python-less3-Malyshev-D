# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
s = 0
x = int(input())
while True:
    if x == 0: break
    if x % 5 == 0:
        s += x
    x = int(input())
print('Сумма чисел, делящихся на 5:', s)
# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
a = 0
b = 0
x = int(input())
while x != 0:
    k = 0
    for i in range (2, x):
        if x % i == 0:
            k += 1
    if k == 0:
        a += 1
    else:
        b += 1
    x = int(input())
print('Простых чисел:', a, 'и Составных чисел:', b)
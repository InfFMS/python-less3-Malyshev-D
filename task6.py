# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
x = int(input())
mx = x
mn = x
if x == 0: print('Нет чисел для анализа.')
while True:
    if x == 0:
        break
    if x > mx:
        mx = x
    if x < mn:
        mn = x
    x = int(input())
print('Минимальное число:', mn)
print('Максимальное число:', mx)

# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
n = int(input())
p = []
for i in range(n):
    x = int(input())
    a = 0
    for j in range(2, x+1):
        if x % j == 0:
            a += 1
    if a == 1: p.append(x)
if len(p) == 0:
    print('нет')
else:
    print('Минимальное простое число:', min(p))
    print('Максимальное простое число:', max(p))
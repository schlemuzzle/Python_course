"""
print (4)
print (5)
"""
a = 3
b = 1.45
s = "venv"
print(a, b, s)
print(a, "-", b, "-", s)
print("{} - {} - {}".format(a, b, s))
print(f"first - {a} second - {b} third - {s}")
# —------------------------------------
# print('Введите первое число: ')
# a = input() # or turn a to int like: a = int(input())
# print(a)
# b = input('Введите второе число: ') # or turn b to int like: b = int(input('Введите второе число: '))
# print(a + b)
# print(int(a) + int(b))
# —------------------------------------
a = 1.235784
b = 2.465635
print(a * b)
print(round(a * b, 3))
# —------------------------------------
a = 1 > 4
print(a) # False
# —------------------------------------
a = 1 < 4 and 5 > 2
print(a) # True
# —------------------------------------
a = 1 == 2
print(a) # False
# —------------------------------------
a = 1 != 2
print(a) # True
# —------------------------------------
a = 'qwe'
b = 'qwe'
print(a == b) # True
# —------------------------------------
a = 1 < 3 < 5 < 10
print (a) # True
# —------------------------------------

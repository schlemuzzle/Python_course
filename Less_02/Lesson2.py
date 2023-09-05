# # списки
# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка через функцию
# list_1 = [7, 9, 11, 13, 15, 17]
# print(*list_1) # * убирает скобки
# print(list_1[0]) # вывод конкретного элемента списка
# print(len(list_1)) # вывод длины списка

# list_2 = list() # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
#     n = int(input()) # пользователь вводит целое число
#     list_2.append(n) # сохранение элемента в конец списка
# # 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# # 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# # 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# # 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# # 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
# print(list_2) # [12, 7, -1, 21, 0]

# # Метод pop удаляет последний элемент из списка:
# list_3 = [12, 7, -1, 21, 0]
# print(list_3.pop()) # 0
# print(list_3) # [12, 7, -1, 21]
# print(list_3.pop()) # 21
# print(list_3) # [12, 7, -1]
# print(list_3.pop()) # -1
# print(list_3) # [12, 7]

# # Удаление конкретного элемента из списка. Надо указать значение индекса в качестве аргумента функции pop:
# list_4 = [12, 7, -1, 21, 0]
# print(list_4.pop(0)) # 12
# print(list_4) # [7, -1, 21, 0] 

# #Добавление элемента на нужную позицию. Функция insert — указание индекса (позиции) и значения.
# list_5 = [12, 7, -1, 21, 0]
# print(list_5.insert(2, 11))
# print(list_5) # [12, 7, 11, -1, 21, 0]

# # Срез списка. Отрицательное число в индексе — счёт с конца списка
# list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_6[0]) # 1
# print(list_6[1]) # 2
# print(list_6[len(list_6)-1]) # 10
# print(list_6[-5]) # 6
# print(list_6[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_6[:2]) # [1, 2]
# print(list_6[len(list_6)-2:]) #[9, 10]
# print(list_6[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_6[6:-18]) # []
# print(list_6[0:len(list_1):6]) # [1, 7] (*от 0го эл-та до конца с шагом 6)
# print(list_6[::6]) # [1, 7]

# # Кортеж — это неизменяемый список (занимает меньше места в памяти и работают быстрее, по сравнению со списками)
# t = () # создание пустого кортежа
# print(type(t))         # class <'tuple'>
# t = (1,)               
# print(type(t))         # class <'tuple'>
# t = (1)
# print(type(t))         # class <'int'>
# t = (28, 9, 1990)
# print(type(t))         # class <'tuple'>

v = [1, 2, 3]
print(type(v))           # class <'list'>
v = tuple(v)
print(type(v))           # class <'list'>

# Можно распаковать кортеж в независимые переменные:
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).

d = {}
d = dict()
d['q'] = 'qwerty'
print(d)   # {'q': 'qwerty'}

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))      # up: ↑
                                                        # down: ↓
                                                        # right: →
for (k,v) in dictionary.items():
    print(k, v)     # up: ↑
                    # down: ↓
                    # right: →
                                                        
# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
q = set() # пустое множество

colors = {'red', 'green', 'blue'}
print(colors)                        # {'red', 'green', 'blue'}
colors.add('red')
print(colors)                        # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)                        # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)                        # {'green', 'blue','gray'}
colors.remove('red')                 # KeyError: 'red'
colors.discard('red')                # ok

# Операции со множествами в Python:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                                 # c = {1, 2, 3, 5, 8}
u = a.union(b)                               # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)                        # i = {8, 2, 5}
dl = a.difference(b)                         # dl = {1, 3}
dr = b.difference(a)                         # dr = {13, 21}
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

# List comprehension («генератор списка») — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.

# Простая ситуация — список:
# list_1 = [exp for item in iterable]
# Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100] # Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100] # Добавить условие (только чётные числа)

list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)] Или создать пары каждому из чисел (кортежи)
list_1 = [i * 2 for i in range(10) if i % 2 == 0] # Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.

print(list_1) # [0, 4, 8, 12, 16]

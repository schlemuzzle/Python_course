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
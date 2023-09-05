# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

list_1 = [int(input("Введите число: ")) for i in range(6)]
k = int(input("Введите k: "))
list_2 = []
for i in range(0, len(list_1)):
    if i < (len(list_1) - k):
        list_2.append(list_1[k + i])
    else:
        list_2.append(list_1[i - (len(list_1) - k)])
print(list_1)
print(list_2)
# or

list = [1, 2, 3, 4, 5, 6]
print(list)
k = 3
for i in range(k):
    el = list.pop()
    list.insert(0, el)
print(list)
# # or

#          0  1  2  3  4
my_list = [1, 2, 3, 4, 5]
#         -1 -2 -3 -4 -5
k = 3
k = k % len(my_list) # для того чтобы убрать лишние циклы, если k больше длины списка, например:
                     # len(lst) = 5, k = 12 - два полных круга по 5+5 и видимое смещение 2, k % len(lst) = 2
print(my_list[-k:] + my_list[:-k])
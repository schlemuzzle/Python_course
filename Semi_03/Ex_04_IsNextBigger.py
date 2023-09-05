# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list_1 = [int(input("Введите число: ")) for i in range(5)]
counter = 0
for item in range(1, len(list_1)):
    if list_1[item] > list_1[item - 1]:
        counter += 1
print(counter)
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list = [1, 1, 2, 0, -1, 3, 4, 4, 45, 45, 0, 9]
# set = set(list)
# print(set)
# print(len(set))
print (len(set(list)))
# or

list_1 = [int(input("Введите число: ")) for i in range(6)]
print(list_1)
Q = len(set(list_1))
print(Q)
# or

list_with_duplicates = [1, 1, 2, 0, -1, 3, 4, 4]
unique_list = []
for item in list_with_duplicates:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
print(len(unique_list))
# or

str1 = [1, 1, 2, 0, -1, 3, 4, 0]
counter = 0
for i in range(len(str1)):
    if str1[i] not in str1[:i]:
        counter += 1
print(counter)
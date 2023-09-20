# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать 
# циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def reverse(n):
#     s = input()
#     if n != 1:
#         reverse(n - 1)
#     print(s, end = ' ')

# n = int(input())
# reverse(n)

#or

def func(x):
    number = input()
    if x == 1:
        return number
    return func(x - 1) + " " + number

# x = int(input())
print(func(5))
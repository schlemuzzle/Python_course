# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары 
# дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, 
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Input: 300
# Output: 220 284

def sum_del(n):
    summ = 0
    for num in range(1, n):
        if n % num == 0:
            summ += num
    return summ

k = int(input())

for num_1 in range(1, k + 1):
    num_2 = sum_del(num_1)
    sum_del_2 = sum_del(num_2)
    if (num_1 == sum_del_2) and (num_1 != num_2) and (num_1 < num_2):
        print(num_1, num_2) 
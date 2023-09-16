# def sumNumbers(n, y = 'Wassa!'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# n = int(input()) # 5
# print(sumNumbers(n)) # 15
# a = sumNumbers(2, 'Hello')
# print(a)

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'w', 'e',))
# print(sum_str('q', 'w', 'e', 'r', 't', 'y'))

# import modul1
# print(modul1.max1(5, 9))
# from modul1 import * - import ALL functions
# from modul1 import max1
# print(max1(5645, .13219))
# import modul1 as m1
# print(m1.max1(45, 54))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Быстрая сортировка(бинарный поиск)

# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3])) #  [2, 3] + [5] + [10] = [2, 3, 5, 10]

# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)

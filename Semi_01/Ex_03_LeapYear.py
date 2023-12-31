# Дано натуральное число. Требуется определить, является ли год с данным номером 
# високосным. Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016
# Output: YES

print("Введите число: ")
a = int(input())
if (a%4 == 0 and a%100 != 0):
    print("Yes")
elif a%400 == 0:
    print("Yes")
else:
    print("No")
# or
print("YES" if (a % 400 == 0) or (a % 4 == 0 and not a % 100 == 0) else 'NO')
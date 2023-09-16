# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def check_div(n):
    if n < 4:
        return "YES"

    for i in range(2, n//2 + 1):
        if n % i == 0:
            return 'NO'
    return 'YES'


n = int(input())
print(check_div(n))

#or

def prost (n):
    count = 0
    for i in range(2,n):
        if n%i==0:
            count+=1
    return count == 0

a = int(input())
print(prost(a)) 
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

print("Введите номер: ")
n = int(input())
a = n//100000
b = (n//10000)%10
c = (n//1000)%10
d = (n//100)%10
e = (n//10)%10
f = n%10
if (a + b + c == d + e + f):
    print("Yes")
else:
    print("No")

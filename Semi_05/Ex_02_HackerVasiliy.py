# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

n = list(map(int, input().split()))

def xaker(n):
    maxx = max(n)
    minn = min(n)
    for i in range(len(n)):
        if n[i] == maxx:
            n[i] = minn
    return n

print(*xaker(n))

def rec(n):
    return [el if el != max(n) else min(n) for el in n]   

print(*rec(n))
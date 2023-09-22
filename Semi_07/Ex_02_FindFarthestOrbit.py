# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет
# найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды
# таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен
# быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя
# кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в
# два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна.
# Input:    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#           print(*find_farthest_orbit(orbits))
# Output:   2.5 10


def find_farthest_orbit(list_of_orbits):
    squares = [(i[0] * i[1] if i[0] != i[1] else 0) for i in list_of_orbits]
    return list_of_orbits[squares.index(max(squares))]

# or 

def max_orb(list_of_orbits):
    s_orbits = [(x_1*x_2 if x_1 != x_2 else 0) for x_1, x_2 in list_of_orbits]
    # print(s_orbits)
    # print(max(s_orbits))
    # print(s_orbits.index(max(s_orbits)))
    # print(list_of_orbits[s_orbits.index(max(s_orbits))])
    return list_of_orbits[s_orbits.index(max(s_orbits))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
print(*max_orb(orbits))

# or

print(*max([(a, b) for a, b in orbits if a != b], key=lambda x: x[0] * x[1]))


newmax = ()
int = 0

mx = 0
for i in range(0, len(orbits)):
    a = 1
    l = 0
    j = 0
    while j < 2:
        a *= orbits[i][j]
        j = j + 1
    if a > mx and orbits[i][0] != orbits[i][1]:
        mx = a
newmax = orbits[i]
print(*newmax)

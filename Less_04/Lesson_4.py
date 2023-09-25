def f(x):
    return x ** 2

g = f
# print(f(4))                       # 16
# print(g(4))                       # 16

#////////////////////////////////////////////////////////////////////////////////////////////

def calc1(x, y):
    return x + y

def calc2(x, y):
    return x * y

def math(op, x, y):
    print(op, x, y)

# math(calc1, 10, 2)                 # 12
# math(calc2, 10, 2)                 # 20

#////////////////////////////////////////////////////////////////////////////////////////////

sum = lambda x, y: x + y

#print(sum(2, 5))                     # 7
#math(lambda x, y: x + y, 4, 5)       # 9

#////////////////////////////////////////////////////////////////////////////////////////////

def evpow(list):
    result = []
    for i in list:
        if i % 2 == 0:
            result.append((i, i * i))
    return result

list1 = [1, 2, 3, 5, 8, 15, 23, 38]
#print(evpow(list1)) # [(2, 4), (8, 64), (38, 1444)]

# or

def select(f, col):                             # по сути - расписанная функция select является встроенной функцией map
    return [f(x) for x in col]

def where(f, col):                              # по сути - расписанная функция where является встроенной функцией filter
        return [x for x in col if f(x)]

res = select(int, list1)                        # [1, 2, 3, 5, 8, 15, 23, 38]
res = where(lambda x: x % 2 == 0, res)          # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))  # [(2, 4), (8, 64), (38, 1444)]

# or

res = map(int, list1)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))

#/////////////////////////////////////////////////////////////////////////////////////////////////

list_1 = [x for x in range (1,10)]              # [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_1 = list(map(lambda x: x + 10, list_1 ))   # [11, 12, 13, 14, 15, 16, 17, 18, 19]

data = '1 2 3 5 8 15 23 38'                     # 1 2 3 5 8 15 23 38
# data = '1 2 3 5 8 15 23 38'.split()            # ['1', '2', '3', '5', '8', '15', '23', '38']
# data = list(map(int, input().split()))          # ['1', '2', '3', '5', '8', '15', '23', '38']

#/////////////////////////////////////////////////////////////////////////////////////////////////

data_1 = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data_1))
print(res)                                      # [15, 65, 175]

#////////////////////////////////////////////////////////////////////////////////////////////////

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)                                      # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)                                      # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

#///////////////////////////////////////////////////////////////////////////////////////////////

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)                                      # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

#//////////////////////////////////////////////////////////////////////////////////////////////



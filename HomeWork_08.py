# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

m, n, k = int(input("Введите значение m: ")), int(input("Введите значение n: ")), int(input("Введите значение k: "))

if k % m == 0 or k % n == 0:
    print('yes')
else:
    print('no')
N = int(input('Введите число N:'))
while N <= 0:
    print('N должен быть больше 0')

a=[]

for i in range(10, 1000):
 x = i % 10
 y = i % 100 // 10
 z = i // 100
 j = i // 10
 if i>99:
     if (x ** 3 + y ** 3 + z ** 3 == N) and not x in a and not y in a and not z in a:
            print('{}³+{}³+{}³={}'.format(x, y, z, N))
            a.append(x)
            a.append(y)
            a.append(z)
else:
    print("No such combinations!")

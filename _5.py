
N=int(input("Введите N :"))
while N<=0:
    print("N не может быть меньше 0: ")

    a = []
    b = []
  
for s in range(10, 1000):
    x = s % 10
    y = s % 100 // 10
    z = s // 100
    j = s // 10
    if s > 99:
        if (x ** 3 + y ** 3 + z ** 3 == N) and not x in a and not y in a and not z in a:
            print('{}³+{}³+{}³={}'.format(x, y, z, N))
            a.append(x)
            a.append(y)
            a.append(z)
          
        else:
            print("No such combinations!")
    
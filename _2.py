n = int(input("Введите количество слогаемых: "))
pi = 0

for i in range(1, n + 1, 2):
    pi += 4 / i - 4 / (i+2)

print("Приблизительное pi = " + str(pi))

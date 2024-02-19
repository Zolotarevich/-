arr = iter([int(input()) for i in range(int(input("Введите количество строк: ")))])
a, b = int(input("Введите начальный индекс: ")), int(input("Введите конечный индекс: "))
summa = 0
for i in range(a-1):
    next(arr)
for j in range(b-a+1):
    summa += next(arr)

print(summa)
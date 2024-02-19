list_input = [int(input()) for i in range(int(input("Введите количество чисел: ")))]
print(*reversed(sorted(list_input)))
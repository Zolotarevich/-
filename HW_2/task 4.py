def Artek(s, n):
    excellent_students = []
    for puple in s.split(','):
        surname, mark = puple.split()
        if mark == '5':
            excellent_students.append(surname)
    return sorted(excellent_students)[:n]

string = input('Фамилия оценка ')
num = int(input('Кол-во мест '))
print(*Artek(string, num), sep=', ')


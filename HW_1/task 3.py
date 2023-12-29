list_input = []
while 'стоп' not in list_input:
    list_input.append(input().lower())
list_input = sorted(list_input[:-1], key=len)

if set(list_input[0]).intersection(set(list_input[-1])) == set(list_input[0]):
    print('ДА')
else:
    print('НЕТ')


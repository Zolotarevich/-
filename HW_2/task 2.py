import re

n = int(input("Введите количество строк: "))
text = [input() for i in range(n)]
text_output = []

for line in text:
    line_output = re.sub(r'(%%)|(^###.+)', r'', line, flags=re.M|re.I)
    if line_output != '':
        text_output.append(line_output)

print(*text_output, sep='\n')
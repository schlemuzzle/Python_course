# f = open('data.txt', "w", encoding = "utf8")

# f.write('Hello, wolrld!')

# f.close()

from pathlib import Path

file_path = Path('C:', '\Users', '\Админ', '\Desktop', '\ZsYP', 'data.txt')

# file_path = r'Python_course\new.txt'
print(file_path)

with open(file_path, 'w', encoding='utf8') as text_file:
    for line in text_file:
        print(line.strip())
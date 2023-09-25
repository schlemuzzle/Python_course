# f = open('data_1.txt', "w", encoding = "utf8")

# f.write('Hello, wolrld!')

# f.close()

from pathlib import Path

file_path = Path('ZSYP', 'data_1.txt')

# file_path = r'Python_course\new.txt' # r - заставляет читать строку, игнорируя спецсимволы (\n!)
print(file_path)

with open(file_path, 'w', encoding='utf8') as text_file:
    for line in text_file:
        print(line.strip())
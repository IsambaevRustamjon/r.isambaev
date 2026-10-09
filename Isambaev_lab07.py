import re  # подключить модуль для регулярных выражений

print("Task 1 — Clean a student name")
# очистить имя: убрать пробелы по краям и исправить регистр букв
raw = "  aLiCe SMITH  "

clean_name = raw.strip().title()  
# strip() убирает пробелы по краям, 
# title() делает первую букву слова заглавной
print(clean_name)
print(f"[{raw}]")  
# скобки показывают пробелы: raw не изменился
# строки неизменяемые: методы не правят raw, а возвращают НОВУЮ строку,
# поэтому результат нужно сохранять в переменную (clean_name)
print()

print("Task 2 — Extract a filename extension")
# достать расширение файла: текст после последней точки
filename = "final.report.pdf"
print(filename.split(".")[-1])  
# split(".") режет по точкам, [-1] берёт последний кусок -> pdf

filename = "notes.txt"
print(filename.split(".")[-1])  
# txt
print()

print("Task 3 — Split and join words")
# разбить текст на слова и собрать обратно с одним пробелом
text = "  Python   files  are useful  "

words = text.split()  
# split() без аргумента режет по любым пробелам и игнорирует лишние
print(words)  
# ['Python', 'files', 'are', 'useful']
print(" ".join(words))  
# join() склеивает слова, ставя между ними " "
print()

print("Task 4 — Count a substring")
# посчитать, сколько раз "ana" встречается в тексте
text = "banana bandana"

print(text.count("ana"))  
# 2: в "banana" два "ana" перекрываются, count() считает только непересекающиеся
print(text.startswith("ban"))  
# True: начинается с "ban"
print(text.endswith("ana"))  
# True: заканчивается на "ana"
print()

print("Task 5 — Find an optional separator")
# вернуть часть до дефиса, а если дефиса нет, то всю строку
def split_code(value):  
# создать функцию, которая получает строку value
    position = value.find("-")  
    # find() возвращает индекс дефиса или -1, если его нет
    if position == -1:  
    # дефиса нет
        return value  
         # вернуть строку целиком
    return value[:position]  
     # срез: всё до дефиса

print(split_code("NS-205"))  
# NS
print(split_code("NS205"))  
# NS205
print()

print("Task 6 — Normalize a simple record")
# разбить запись по запятым и убрать лишние пробелы у каждого поля
row = "  Anna , 82 , NSU  "

pieces = row.split(",")  
# ['  Anna ', ' 82 ', ' NSU  ']
cleaned_pieces = []  
# пустой список для очищенных полей
for piece in pieces:  
    # по очереди берём каждое поле
    cleaned_pieces.append(piece.strip())  
    # убираем пробелы и добавляем в список

print(" | ".join(cleaned_pieces))  
# склеить через " | " -> Anna | 82 | NSU
print()

print("Task 7 — Find numbers in text")
# найти все числа в тексте и превратить их в int
text = "Rooms B-204, C-17, A-315"

number_strings = re.findall(r"[0-9]+", text)  
# findall() возвращает список всех совпадений; [0-9]+ = одна или больше цифр подряд
numbers = []  
# пустой список для чисел
for number_string in number_strings:  
# по очереди берём каждую строку-число
    numbers.append(int(number_string))  
    # int() превращает '204' в 204

print(number_strings)  
# ['204', '17', '315'] (строки)
print(numbers)  
# [204, 17, 315] (числа)
print()

print("Task 8 — Check a student ID")
# проверить, что вся строка это 2 заглавные буквы, дефис и ровно 4 цифры
def is_valid_id(value):  
# создать функцию, которая получает строку value
    return re.fullmatch(r"[A-Z]{2}-[0-9]{4}", value) is not None  
     # fullmatch требует совпадения ВСЕЙ строки; {2} и {4} задают количество; is not None = совпадение найдено -> True

print(is_valid_id("AB-2047"))  
# True
print(is_valid_id("A-2047"))  
# False: только одна буква
print(is_valid_id("xAB-2047"))  
# False: строчная x и три буквы
print()

print("Task 9 — Compare three regex functions")
# сравнить search, match и fullmatch на одном шаблоне
pattern = r"[0-9]+"  
# одна или больше цифр подряд
text = "Room 204"

print(re.search(pattern, text) is not None)  
# True: search ищет совпадение ГДЕ УГОДНО, нашёл "204"
print(re.match(pattern, text) is not None)  
# False: match ищет только С НАЧАЛА, а текст начинается с "R"
print(re.fullmatch(pattern, text) is not None)  
# False: fullmatch требует, чтобы ВСЯ строка была цифрами
print(re.fullmatch(pattern, "204") is not None)  
# True: вся строка "204" состоит из цифр
print()

print("Task 10 — Extract candidate dates")
# найти всё, что по виду похоже на дату ДД/ММ/ГГГГ
text = "Due 28/09/2026; revised 02/10/2026; invalid 99/99/2026"

dates = re.findall(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", text)  
# две цифры / две цифры / четыре цифры
print(dates)  
# ['28/09/2026', '02/10/2026', '99/99/2026']
# шаблон проверяет только ВИД текста: "99/99/2026" подошёл, хотя такой даты не существует,
# значит совпадение не доказывает, что дата настоящая
print()

print("Task 11 — Find email-like tokens")
# найти то, что похоже на адреса электронной почты
text = "Contact ada@example.com or bob.smith@nsu.ru"

emails = re.findall(r"[A-Za-z0-9._]+@[A-Za-z0-9.]+", text)  
# символы, потом @, потом символы домена
print(emails)  
# ['ada@example.com', 'bob.smith@nsu.ru']
# это учебный шаблон, а не полная проверка почты: настоящие правила гораздо сложнее
print()

print("Task 12 — Clean and select codes")
# очистить коды и оставить только корректные
values = [" ns-205 ", "AB-2047", "invalid", " xy-3001 "]

valid_codes = []  
# пустой список для подходящих кодов
for value in values:  
    # по очереди берём каждое значение
    cleaned = value.strip().upper()  
    # убрать пробелы по краям и сделать буквы заглавными
    if is_valid_id(cleaned):  
        # проверка из Task 8: 2 буквы, дефис, 4 цифры
        valid_codes.append(cleaned)  
        # корректный код добавляем в список

print(valid_codes)  
# ['AB-2047', 'XY-3001']
# "NS-205" отброшен: в нём три цифры вместо четырёх; "INVALID" не похож на код

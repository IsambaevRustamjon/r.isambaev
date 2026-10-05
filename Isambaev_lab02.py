print("Task 1 — Built-in Functions")
#built-in functions = встроенные функции.
#в файле дан список:
values = [12, 7, 19, 5, 14]
count = len(values)
#переменная len спрашивает сколько здесь элементов?
smallest = min(values)
#переменная min спрашивает какое из элементов минимальный?
largest = max(values)
#переменная max спрашивает какое из них максимальный?
total = sum(values)
#переменная sum суммирует все элементы, т.е сумма.
mean = total / count
#и формула для опеределения средний арифметический значение (математика)
print(f"number of values: {count}")
print(f"smallest value: {smallest}")
print(f"largest value: {largest}")
print(f"total: {total}")
print(f"mean: {mean}")
#остальное по стандарту: print(f"...) показывает вместе с значением внутри {}.
print()

print("Task 2 — Absolute Value and Rounding")
#абсольютный значение и округление.
temperature_change = -7.438
measurement = 19.87654
#даны переменные и их значение
print(abs(temperature_change))
#abs возвращает абсолютное значение, то есть модуль числа
print(round(measurement, 1))
print(round(measurement, 2))
print(round(measurement, 3))
#round округляет число до указанного количества знаков после десятичной точки.
#round(число, сколько_знаков) означает: округлить ЧИСЛО до СКОЛЬКО_ЗНАКОВ после точки?
print()

print("Task 3 — Assignment and Augmented Assignment")
#Assignment = присваивание значения переменной.
#Augmented assignment = сокращённая форма присваивания.
balance = 1000.0
#было на балансе 1000
balance += 250
#добавили 250, баланс меняется на новую значение
balance -= 120
#вычитаем из полученный 120, баланс опять меняется на новый
balance *= 1.05
#результат умножаем на 1.05 и баланс принимает финальный вид.
print(f"final balance: {balance:.2f}")
#print(f"...) показывает финульный баланс: итоговую
print()

print("Task 4 — Operator Precedence")
expression_1 = 2 + 3 * 4
expression_2 = (2 + 3) * 4
expression_3 = 20 / 5 + 3
expression_4 = 20 / (5 + 3)
expression_5 = 2 ** 3 ** 2
print(f"2 + 3 * 4 = {expression_1}")
print(f"(2 + 3) * 4 = {expression_2}")
print(f"20 / 5 + 3 = {expression_3}")
print(f"20 / (5 + 3) = {expression_4}")
print(f"2 ** 3 ** 2 = {expression_5}")
print()

print("Task 5 — Time Conversion")
total_seconds = input("enter a number of seconds: ")
total_seconds = int(total_seconds)
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print(f"{total_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")
print()

print("Task 6 — Type Conversion")
#преобразование типа данных.
value = 17.95
integer_value = int(value)
print(integer_value)
float_value = float(integer_value)
print(float_value)
text_value = str(integer_value)
print(f"Value as text: {text_value}")
print(f"Type: {type(text_value)}")
print()

print("Task 7 — Basic String Operations")
#соединить две строки в одну
first_name = input("First name: ")
last_name = input("Last name: ")
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print(f"Number of characters: {len(full_name)}")
print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")
print(f"First three characters: {full_name[:3]}")
print(full_name * 3)
print()

print("Task 8 — Useful print() Options")
language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"
print(language, course, university, sep=" | ")
print("Python", end=" ")
print("Programming")
print()

print("Task 9 — Collections")
student_name = "Anna"
student_age = 22
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"
student = {
    "name": student_name,
    "age": student_age,
    "skills": student_skills,
    "university": student_university,
}
print(student["name"])
print(student["university"])
print(student["skills"][0])
print(len(student["skills"]))
print()

print("Task 10 — Mutable and Immutable Objects")
numbers = [10, 20, 30]
same_numbers = numbers
numbers[0] = 99
print(numbers)
print(same_numbers)
#
text = "Python"
same_text = text
text = text + " Course"
print(text)
print(same_text)
#
print()

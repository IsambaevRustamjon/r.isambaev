print("Task 1 — Positional and keyword arguments")
#позиционные и именованные аргументы
#нужно создать функцию и вызвать её тремя разными способами.
def describe_student(name, age, city):
#создать ф-цию describe_student(name, age, city), которая печатает три строки:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
#показать результаты
#позиционные аргументы. Python смотрит только на место, где стоит значение:
describe_student("Anna", 23, "Novosibirsk")
#именованные аргументы. мы сами пишем имя параметра, знак = и значение:
describe_student(city="Tomsk", name="Boris", age=21)
#смешанный:
describe_student("Mira", age=20, city="Omsk")
#глав. правил. смеш. вызовов: позиционные аргументы должны стоять раньше именованных
print()

print("Task 2 — Default arguments")
#аргументы по умолчанию
#нужно написать ф-цию расчёта стоимости доставки и вызвать её тремя способами.
def shipping_cost(weight, rate=2.5):
#создать ф-цию shipping_cost(weight, rate=2.5).
    return weight * rate
     #она должна вернуть weight * rate, то есть вес, умноженный на тариф.
#вызвать её три раза:
print(shipping_cost(4))             
#только с весом
print(shipping_cost(4, 3))          
#с весом и своим тарифом
print(shipping_cost(4, rate=1.5))   
#с весом и тарифом, переданным как именованный аргумент
print()

print("Task 3 — Early return")
#ранний return
#нужно написать ф-цию безопасного деления и проверить её на двух примерах.
def safe_divide(a, b):
#создать ф-цию safe_divide(a, b)
    if b == 0:
        return None
    #равно ли "b" нулю, если да, то вернуть None
    return a / b
    #если нет, то делим "a" на "b" и вернём результат
 
print(safe_divide(10, 2))
print(safe_divide(10, 0))
#показать результат
print()

print("Task 4 — *args: total score")
# *args: общий балл
#Нужно написать ф-цию суммирования баллов и проверить её на трёх вызовах с разным числом аргументов.
def total_score(*scores):
#создать ф-цию total_score(*scores)
    total = 0
    for score in scores:
        total += score
    return total
     #по очереди берёт из списка "scores" и складывает в total
     # "*" здесь означает, что "scores" может быть любой длины

print(total_score(10, 20, 30))
print(total_score(5))
print(total_score())

print()

print("Task 5 — *args: average score")
# *args: средний балл
#написать ф-цию среднего арифметического и проверить её на двух вызовах.
def average_score(*scores):
    if len(scores) == 0:
        return None
    return total_score(*scores) / len(scores)
     #проверить количесть аргументов, если 0, то вернуть None, 
     #если нет, то вернуть средний балл вычесленный из формулы total_score(*scores) / len(scores)

print(average_score(80, 90, 100))
print(average_score())
#во 2ом вызове список пусть, значить количество аргументов будет 0
#а на ноль делить нельзя, вот так вернется None
print()

print("Task 6 — **kwargs: profile")
# **kwargs: профиль
#написать ф-цию, которая принимает любые именованные аргументы и печатает их.
def show_profile(**details):
# ** означают: "собери все именованные аргументы, которых нет среди обычных параметров, и упакуй их в словарь"
    for key, value in details.items():
        print(f"{key}: {value}")

 
show_profile(name="Anna", city="Novosibirsk", year=1)
 
print()

print("Task 7 — Combining fixed arguments, *args, and **kwargs")
#объединение обычных аргументов, *args и **kwargs
#написать ф-цию с тремя видами параметров и вызвать её.
def course_report(student, *scores, **options):
    print(f"Student: {student}")
    print(f"Scores: {scores}")
    print(f"Options: {options}")
#создать функцию course_report, которая принимает студента student, 
#затем любое количество баллов *scores и любые именованные настройки **options
course_report("Mira", 80, 92, 75, rounded=True, scale=100)

print()

print("Task 8 — Scope")
#область видимости
TAX_RATE = 0.20
#создать глобальную переменную со ставкой налога и ф-цию, которая ею пользуется.
def final_price(price):
    tax = price * TAX_RATE  
    return price + tax
#ф-ция final_price, которая принимает цену price и возвращает её с учетом налога

print(final_price(100))
 
print()

print("Task 9 — Recursive countdown")
#рекурсивный обратный отсчёт
#написать рекурсивную ф-цию отсчёта и вызвать её с числом 3.
def countdown(n):
#создать ф-цию countdown, которая получает число n
    if n == 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)
    #вызвать countdown ещё раз, но с числом на единицу меньше

countdown(3)

print()

print("Task 10 — Recursive factorial")
#рекурсивный факториал
#написать рекурсивную ф-цию факториала и вызвать её с числом 5.
def factorial(n):
#создать ф-цию factorial, которая получает число n
    if n < 0:
        return None
    #если n меньше нуля, вернуть None
    if n == 0:
        return 1
    #если n равно нулю, вернуть единицу
    return n * factorial(n - 1)
     #вернуть произведение "n" на факториал числа "n - 1"
#здесь логика в том что, чтобы посчитать "n!", надо получить "n - 1!" а дальше получить "n-2!" и т.д. 

print(factorial(5))
print(factorial(0))
print(factorial(-2))
 
print()

print("Task 11 — Recursive sum")
#рекурсивная сумма
#написать рекурсивную ф-цию суммы чисел от 1 до n и проверить её на двух примерах.
def sum_to(n):
#создать рекурсивную ф-цию sum_to(n), которая возвращает 1 + 2 + 3 + ... + n.
    if n < 0:
        return None
    if n == 0:
        return 0
    return n + sum_to(n - 1)
     #вернуть сумму числа "n" и результата sum_to для числа "n - 1"
 
 
print(sum_to(4))
print(sum_to(0))
 
print()

print("Task 12 — math module and list methods")
#модуль math и методы списков
print("Part A — math")
radius = float(input("Enter radius: "))
import math 
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
 
print(f"Circumference: {circumference}")
print(f"Area: {area}")
print(f"Area ceil: {math.ceil(area)}")
print(f"Area floor: {math.floor(area)}")
 
#
print("Part B — list methods")
numbers = [10, 20, 20, 30]

numbers.append(40)
numbers.extend([50, 60])
numbers.insert(1, 15)
print(numbers.count(20))
print(numbers.index(30))
numbers.remove(20)
removed = numbers.pop()
print(numbers)
print(removed)

print()

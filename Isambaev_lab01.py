print("Task 1 — Personal Information")
#Название задания: личная информация
name = input("Enter your name: ")
#"input" чтобы получить инорфмацию, в нашем случае ИМЯ.
#После "input" программа подождет ввод значения (текст или число). 
age = int(input("Enter your age: "))
#здесь "input" запрашивает ВОЗРАСТЬ, но получает как ТЕКСТ ответ.
#Чтобы это исправить используется "int" (целое число).
#так как ВОЗРАСТЬ не может быть дробным мы используем целое число.
print(f"Hello, {name}!")
#здесь "print" показывает введенный текст.
#просто добавить значение не получиться, для этого перед текстом используем (f).
#а внутри текст чтобы добавить значение добавляю {значение} (внутри фигурной скобки).
print(f"Next year you will be {age + 1} years old.")
#внутри фигурной скобки {} можно выполнять арифметические операции.
print()

print("Task 2 — Rectangle")
#названия прямоугольник.
width = float(input("Enter width: "))
#здесь "width" и "height" просто ВЫСОТА и ШИРИНА.
#"input" чтобы получить их значение.
height = float(input("Enter height: "))
#"float" для дробных чисел, так как высота и ширина могут быть дробными числами.
area = width * height
#здесь "area" площадь и само формула нахождения площади прямоугольника.
perimeter = 2*(width + height)
#здесь "perimeter" периметр и само формула нахождения периметра прямоугольника.
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
#здесь print(f"... и фигурная скобка {} со значением") чтобы показать нужный текст с значением.  
print()

print("Task 3 — Temperature Converter")
#Конвертер температуры
celsius = float(input("Enter Celsius temperature: "))
#input() запрашивает значение, а float() превращает введённый текст в дробное число.
fahrenheit = celsius * 9 / 5 + 32
#дальше подставить на формулу для получения Фаренгейта.
print(f"{celsius}C = {fahrenheit}F")
#а при помощи (f) показать результаты внутри текста
print()

print("Task 4 — Purchase Calculator")
#калькулятор покупок
quantity = int(input("Enter quantity: "))
#input() запрашивает значение, а int() превращает введённый текст в целое число.
price = float(input("Enter price for one: "))
#input() запрашивает значение, а float() превращает введённый текст в дробное число.
total_price = quantity * price
#после введенных значений, формула сам расчитает итоговую стоимость.
discounted = total_price * 0.10
#скидка 10%, а так как Питон не понимает 10%, то придется написать в десятичных дробях.
discounted_price = total_price - discounted
#цена после скидки это итоговая минус скидка (математика).
print(f"Total price: {total_price}")
print(f"Discounted price: {discounted_price}")
#опять таки при помощи print(f"... и фигурной скобки {} показываю нужный текст с результатами)
print()

print("Task 5 — Arithmetic Operators")
#арифметик операторы
a = 17
b = 5
#даны значение a и b.
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")
#print(f"...) для показа формулы, а фигурная скобка {} для показа решения формулы указанный в тексте.
print()

print("Task 6 — Data Types")
#типы данных
integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
text_value = "Python"
boolean_value = True
#даны определенные типы данных, нужно определить/показать тип каждого значения.
print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(text_value))
print(type(boolean_value))
#print() для показа результата на экране.
#type() для определения типа данных.
print()

print("Task 7 — Comparisons and Boolean Logic")
#сравнение и логическая работа
#даны:
age = 22
is_master_student = True
#нужно показать сравнение и логические операции (True или False):
print(age >= 18)
print(age < 30)
print(age == 22)
print(age != 25)
#здесь внутри print() производиться сравнение, а print() покажет результат на экране.
print(age >= 18 and is_master_student)
print(age < 18 or is_master_student)
print(not is_master_student)
#здесь "and" означает "И" и одновременно должно быть либо True тогда ответ тоже True либо False тогда ответ тоже False.
#здесь "or" означает "ИЛИ" и для or достаточно хотя бы одного True
#здесь "not" означает "НЕТ", т.е переверни логическое значение: было True, стало False.
print()

print("Task 8 — Python Collections")
#даны контейнеры, нужно ввести правильные данные
programming_languages = ["Python", "Kotlin", "C++"]
numbers = (1, 2, 3)
cities = {"Novosibirsk", "Bukhara", "Sankt-Peterburg"}
student = {
    "name": "Rustamjon",
    "age": 29,
    "university": "NSU"
}
#готова, теперь чтобы показать на экране эти значения внутри контейнера использую print().
print(programming_languages)
print(numbers)
print(cities)
print(student)
#а также для определения типов данных использую type()
print(type(programming_languages))
print(type(numbers))
print(type(cities))
print(type(student))
print()

print("Task 9 — Indexing and Slicing")
#Indexing → обращение к отдельному элементу.
#Slicing → взятие части коллекции.
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
#даны индекс/срез [], не перепутать с обычной скобкой ().
print(numbers[0])
#означает: дай мне элемент numbers с индексом 0.
#здесь пояснение: питон начинает считать элементы с НУЛЯ, а не 1. Поэтому начало имеет индекс 0.
#т.е: у 1го элемента индекс 0, а у 2ой индекс 1, у 3ий индекс 2 и тд до 8ой индекс 7.
print(numbers[-1])
#-1 означает: возьми последний элемент с конца, т.е 7 ку.
print(numbers[1:4])
#ну типа от индекса 1 до индекса 4, не включая 4, ну питон не берет последний, не как в математике.
print(numbers[::2])
#здесь нужно взять каждую вторую, поэтому использую вот это:
#numbers[начало:конец:шаг] последняя часть — шаг
word = "Python"
#дано слово Python, нужно как наверху опеределять.
print(word[0])
#первая буква
print(word[-1])
#последняя буква
print(word[:3])
#надо получить Pyt, поэтому нужно взять первые три символа.
print()

print("Task 10 — Dictionaries and Membership")
#Dictionaries → словари
#Membership → проверка, есть ли что-то внутри.
student = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}
#для получения значения(имя, возрасть или город) мы используем КЛЮЧИ.
#здесь ключами яв-ся: "name", "age" и "city", а их значение: Анна, 22 и Новосибирск.
print(student["name"])
print(student["age"])
#при помощи print(student["ключ"]) я обращаюсь к контейнеру student и указываю показать значение нужного ключа.
print("age" in student)
print("email" in student)
#in означает: находится ли это внутри?
#ну типа "age" или "email" есть ли внутри контейнера student?
numbers = [10, 20, 30, 40]
#примерно тоже самое, дано список с числами.
print(20 in numbers)
print(50 in numbers)
#in справшивает есть ли значение 20 или 50 внутри списка numbers? а print() показывает на экране.
print()

print("Task 11 — Formatted Output")
#форматированный, то есть красиво оформленный вывод
radius = float(input("Enter radius: "))
#всё стандартно, input() для получения значения Радиуса, а float() для десятичных дробей.
area = 3.14159 * radius ** 2
#print(f"...) для показа резуьтата.
print(f"radius: {radius}", f"area: {area:.2f}")
#в указании меня просили получить 314.16, ну означает округлить до сотых, т.е оставить две цифры после десятичной точки
#в моем случае {area:.2f} пункт .2f даёт такую возможность.
print()

print("Task 12 — Trip Cost Calculator")
#калькулятор поездки
distance = float(input("Enter distance in kilometers: "))
#distance переменная для запроса дистанции
fuel_consumption = float(input("Enter fuel consumption per 100 km: "))
#fuel_consumption переменная для запроса необходимого топлиго на 100км
fuel_price = float(input("Enter fuel price per liter: "))
#fuel_price переменная для запроса цены топлива за литр
liters_needed = distance / 100 * fuel_consumption
#liters_needed формула для определения необходимого объема топлива за весь путь маршрута.
trip_cost = fuel_price * liters_needed
#trip_cost формула для опеределения общий стоимости заправки топлива за нужный объем топлива.
print(f"Distance: {distance} km")
print(f"Fuel required: {liters_needed:.2f} liters")
print(f"Trip cost: {trip_cost:.2f}")
#напоминаю что пункт .2f нужен для округления до сотых или же оставить две цифры после десятичной точки
print()


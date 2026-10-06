print("Task 1 — Countdown with while")
#выполняемость пока (до тех пор) "while"
n = int(input("Enter a positive integer: "))
#запрос набрать число, а int() чтобы оно было целым.
while n >= 1:
    print(n)
    n -= 1
#пока (до тех пор) "while" выполняется условие n >= 1
#будет выполняться задача n -= 1, т.е уменьшить значение на 1.
print("Go!")
#в конце просто показать слова Go!
print()

print("Task 2 — Repeat until zero")
#повторять до 0
count = 0
#количества не нулевых чисед (по заданию)
total = 0
#сумма этих самых чисел (по заданию проситься сумма)
n = int(input("Enter an integer (0 for stop): "))
#запрашиваем user набрать любое число
while n != 0:
    count += 1
    total += n
    n = int(input("Enter an integer (0 for stop): "))
#пока (до тех пор) "n" не равно нулю, выполняется условие задание
#количества "count" чисел "n" увеличивается на 1
#к сумме "total" прибавляется очередное число "n"
print(f"Count: {count}")
print(f"Total: {total}")
#показать результаты когда user набирает 0 и оставить программу.
print()

print("Task 3 — Valid input with while True")
#Корректный ввод с параметром while True
while True:
    value = int(input("Enter an integer from 1 to 10: "))
    if value < 1 or value > 10:
        print("Invalid value")
        continue
    print("Accepted")
    break
#пока (до тех пор) "while True" выполняется условие "value < 1 or value > 10"
#если "value" меньше 1 или больше 10, то выполняется команда "continue"
#и показать сообщение "Invalid value"
#и продолжается цикл, т.е. выводится сообщение "Accepted"
print()

print("Task 4 — continue in a while loop")
#программа печатает числа от 1 до 20, пропуская те, что делятся на 3
number = 1
while number <= 20:
    if number % 3 == 0:
        number += 1
        continue
    print(number)
    number += 1
#пока (до тех пор) while повторяется, пока number <= 20.
#if проверяет: делится ли number на 3 без остатка?
#да -> увеличиваем number и continue (print пропускаем)
#нет -> печатаем number и увеличиваем его
print()

print("Task 5 — Search with loop else")
#программа ищет ПЕРВОЕ НЕЧЁТНОЕ число в списке.
numbers = [4, 8, 12, 16, 21, 24]
#список чисел
for value in numbers:
    if value % 2 != 0:
        print(f"First odd number: {value}")
        break
#for берёт числа по очереди.
#(если) if: value % 2 != 0 -> остаток не 0 -> число нечётное, 
#тогда печатаем его и break (остальные числа не проверяем)
else:
    print("All values are even")
#else у for сработает, только если break НЕ было,
#то есть нечётных чисел нет -> показать сообщение "All values are even"
print()

print("Task 6 — Multiplication table with nested loops")
#программа выводит таблицу умножения
#таблица умножения 5x5.
for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end=" ")
    print()
#внешний цикл: row = 1..5 (каждая итерация это одна строка таблицы).
#внутренний цикл: column = 1..5, для каждого печатаем row * column и end=" " оставляет результат в той же строке.
#print() после внутреннего цикла переводит на новую строку.
#range(1, 6) даёт 1, 2, 3, 4, 5 (число 6 не входит)
print()

print("Task 7 — Dynamic typing")
#динамическая типизация
value = 42
#cоздать переменную value и присвоить ей 42
print(value, type(value))
#напечатать значение и его тип.
value = 3.14
print(value, type(value))
#присвоить ей 3.14, напечатать значение и тип.
value = "Python"
print(value, type(value))
#присвоить ей "Python", напечатать значение и тип.
value = [1, 2, 3]
print(value, type(value))
#присвоить ей [1, 2, 3], напечатать значение и тип.
print()

print("Task 8 — Equality, identity, and references")
#работы с равнавенство, идентичность и ссылки
a = [10, 20]
b = [10, 20]
c = a
#дано три имени и два разных списка. нужно разобратся, кто на что указывает
print(a == b)
print(a is b)
print(a == c)
print(a is c)
#== спрашивает: "содержимое одинаковое?" это сравнение равенства.
#is спрашивает: "это один и тот же объект?" это сравнение идентичности.
print(id(a))
print(id(b))
print(id(c))
#ф-ция id() возвращает "номер" объекта: число, по которому python различает объекты в памяти.
c.append(30)
#метод .append() изменяет сам список, добавляя элемент в конец.
#т.е. было [10, 20] а станет [10, 20, 30], так как "c=a", то список "a" тоже изменится
print(a)
print(b)
print(c)
#печать a, b, c
#"a" изменился, хотя я с ним ничего не делал напрямую, потому что "a" и "c" это один список
#"b" остался прежним, потому что он указывает на другой объект.
print()

print("Task 9 — Function: is_even")
#функция: is_even
#ничего заранее не дано. нужно самим создать функцию и проверить её на трёх числах.
def is_even(number):
#def это «запомнить новую функцию с таким именем "is_even" и таким параметрам "number"».
    if number % 2 == 0:
    #number % 2 == 0 проверяет остаток от деления на 2 равен ли нулю?
        return True
    else:
        return False
#is_even это имя функции. "является ли чётным" (из англ. слова is even). так принято называть ф-ии, которые отвечают "да" или "нет".
#строка с def ничего не выполняет. она только записывает рецепт. ф-ция сработает, когда мы её вызовем
print(is_even(4))
print(is_even(7))
print(is_even(0))
#печатать результат: True или False
print()

print("Task 10 — Function: calculate_discount")
#ф-ция: calculate_discount
#нужно написать ф-цию, которая считает цену после скидки, и проверяет её на двух примерах.
def calculate_discount(price, percent):
#создать ф-цию "calculate_discount" и которая получает цену price и скидку percent.
    return price - price * percent / 100
#ф-ция должна отдать результат наружу, как return
#подставляет значение percent в цену price и вычисляет скидку
print(calculate_discount(1000, 15))
print(calculate_discount(250, 20))
#показать результат когда скидка 15% и 20% и цена 1000 и 250 соответственно
print()

print("Task 11 — return versus print")
#return против print
#переписать функцию так, чтобы она возвращала площадь.
def rectangle_area(width, height):
#создать ф-цию "rectangle_area" и которая получает ширину width и высоту height.
    return width * height
#вернуть значение умножение по формуле "площадь = ширина * высота"
result = rectangle_area(5, 4)
#эта строка делает сразу две вещи: вызывает ф-цию с width = 5 и height = 4
#внутри считается 5 * 4 = 20, и return отдаёт 20.
#результат 20 попадает в переменную result.
print(result)
print(result * 2)
#показать результат result и result * 2
print()

print("Task 12 — Function returning multiple values")
#ф-ция, возвращающая несколько значений
#написать ф-цию min_max(numbers), которая получает список чисел.
def min_max(numbers):
#создать ф-цию "min_max" и которая получает список чисел.
    smallest = numbers[0]
    largest = numbers[0]
#пока что smallest и largest значение равно первому элементу [0] списка.
    for value in numbers:
    #цикл for: берём числа по очереди и кладём в value.
        if value < smallest:
            smallest = value
        #если число меньше текущего минимума, оно становится новым минимумом.
        if value > largest:
            largest = value
        #если число больше текущего максимума, оно становится новым максимумом.
    return smallest, largest
#ф-ция return возвращает два значения: минимальное и максимальное
values = [7, 2, 9, -1, 5, 12, 3]
smallest, largest = min_max(values)
print(smallest)
print(largest)
#показать минимум и максимум
print()

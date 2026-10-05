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
 
print()

print("Task 4 — continue in a while loop")
 
number = 1
while number <= 20:
    if number % 3 == 0:
        number += 1
        continue
    print(number)
    number += 1
 
print()

print("Task 5 — Search with loop else")
 
numbers = [4, 8, 12, 16, 21, 24]
 
for value in numbers:
    if value % 2 != 0:
        print(f"First odd number: {value}")
        break
else:
    print("All values are even")
 
print()

print("Task 6 — Multiplication table with nested loops")
 
for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end=" ")
    print()
 
print()

print("Task 7 — Dynamic typing")
 
value = 42
print(value, type(value))
 
value = 3.14
print(value, type(value))
 
value = "Python"
print(value, type(value))
 
value = [1, 2, 3]
print(value, type(value))
 
print()

print("Task 8 — Equality, identity, and references")
 
a = [10, 20]
b = [10, 20]
c = a
 
print(a == b)
print(a is b)
print(a == c)
print(a is c)
 
print(id(a))
print(id(b))
print(id(c))
 
c.append(30)
print(a)
print(b)
print(c)
print()

print("Task 9 — Function: is_even")
 
 
def is_even(number):
    return number % 2 == 0
 
 
print(is_even(4))
print(is_even(7))
print(is_even(0))
 
print()

print("Task 10 — Function: calculate_discount")
 
 
def calculate_discount(price, percent):
    return price - price * percent / 100
 
 
print(calculate_discount(1000, 15))
print(calculate_discount(250, 20))
 
print()

print("Task 11 — return versus print")
 
 
def rectangle_area(width, height):
    return width * height
 
 
result = rectangle_area(5, 4)
print(result)
print(result * 2)
 
print()

print("Task 12 — Function returning multiple values")
 
 
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    return smallest, largest
 
 
values = [7, 2, 9, -1, 5, 12, 3]
smallest, largest = min_max(values)
print(smallest)
print(largest)
 
print()
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


print("Task 1 — Positive, negative, or zero")
#положительный, отрицательный или ноль
number = int(input("Enter an integer: "))
if number > 0:
    print("Positive")
#Если number, то покажи Positive
elif number < 0:
    print("Negative")
#иначе, если number, то покажи Negative
else:
    print("Zero")
#else = «иначе» покажи Zero
print()

print("Task 2 — Age category")
#категория возраста
age = int(input("Enter your age: "))
#пользователь набирает свой возрасть
if age < 13:
    print("Child")
#если age меньше 13, показать Child
elif age <= 17:
    print("Teenager")
#иначе, если age меньше или равно 17 (автоматом будет больше 13), то покать Teenager.
elif age <= 64:
    print("Adult")
#иначе, если age меньше или равно 64 (автоматом будет больше 17), то показать Adult.
else:
    print("Senior")
#иначе (автоматом больше 64) показать Senior
print()

print("Task 3 — Grade classifier")
#классификация класса
score = int(input("Enter a score: "))
if score < 60:
    print("Fail")
#если score меньше 60, то покзать Fail
elif score <= 74:
    print("C")
#иначе, если score меньше или равно 74, то показать C
elif score <= 89:
    print("B")
#иначе, если score меньше или равно 89, то показать B
elif score <= 100:
    print("A")
#иначе, если score меньше или равно 100, то показать A
else:
    print("Invalid score")
#иначе показать Invalid score
print()

print("Task 4 — Access decision")
#решение о доступе
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")
#user набирает свой возрасть и наличие билета при помощи yes/no
if age >= 18 and has_ticket == "yes":
    print("Access granted")
#если age больше или равно 18 и на вопрос о билете ответ yes, то показать Access granted
elif age < 18:
    print("Must be 18 or older")
#иначе, если age меньше 18, то показать Must be 18 or older
else:
    print("Ticket required")
#иначе показать Ticket required
print()

print("Task 5 — Even numbers with range()")
#четные numbers из диапазона
for number in range(2, 31, 2):
    print(number)
#for для повторения действия для каждого значения
#начать с 2, остановиться перед 31 при этом идти с шагом 2
#нам нужно чтобы 2 до 30 было, но если указать 30, то Python не возмет 30, поэтому указал 31.
#взять по очереди числа из указанного диапазона и каждый раз печатать их
print()

print("Task 6 — Sum of multiples of 3")
#нужно посчитать сумму чисел кратных на 3 с 3 до 99. 
total = 0
#начало 0, потом будем прибавлять числа кратные на 3, до самого 99.
for number in range(3, 100, 3):
    total += number
#for для повторения действия для каждого значения
#начать брать 3 до 100 (чтобы Python взял 99 указываю 100), с шагом 3.
print(total)
#total меняется каждый раз, и в конце print(total) показать результат
print()

print("Task 7 — Count number categories")
#дан готовый список:
numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]
#нужно посчитать, сколько в нём положительных, отрицательных чисел и нулей
positive_count = 0
#количиства положительных
negative_count = 0
#количества отрицательных
zero_count = 0
#и количества нулей
for value in numbers:
    if value > 0:
        positive_count += 1
    elif value < 0:
        negative_count += 1
    else:
        zero_count += 1
#for для повторения действия для каждого значения
#если находить значение относящиеся к одному из типов, то прибавить +1 к количеству
print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")
#показать результат каждого из них
print()

print("Task 8 — Count vowels")
#Попросить пользователя ввести слово или небольшой текст и посчитать, сколько в нём гласных букв.
text = input("Enter a word or short text: ")
#user набирает слова или короткий текст
vowels = "aeiouAEIOU"
vowel_count = 0
#5 гласных букв, маленькие и заглавные этих же букв соотвественно
for character in text:
    if character in vowels:
        vowel_count += 1
#если найдется гласные буквы из aeiouAEIOU, то прибавить +1 к количеству
#for для повторения действия для каждого значения
print(vowel_count)
#показать конечный результат
print()

print("Task 9 — Student results")
#даны список результатов студента:
scores = [85, 42, 67, 91, 58, 73, 100, 39]
#посчитать сколько сдано
passed = 0
#сдал
failed = 0
#провал
total = 0
#итоговый балл (сумма)
for score in scores:
    total += score
    if score >= 60:
        passed += 1
    else:
        failed += 1
#взять каждый балл по очереди
#каждый балл нужно добавить к total при этом
#если балл больше или равно 60, то сдал и +1 к passed, иначе провал и +1 к failed
average = total / len(scores)
#посчитать средний балл: весь балл total поделить на количества len()
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {average:.2f}")
#показать результаты
print()

print("Task 10 — Search and stop")
#поиск и стоп
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]
#даны список имен:
target_name = input("Enter a name to search for: ")
#запрос имени user для поиска
found = False
#изначально пока имена не найдены значение found беру как false
for name in names:
    if name == target_name:
        found = True
        break
#for проверяет совпадение в списке по очереди, если найдет то значение found измениться на true
if found:
    print("Found")
else:
    print("Not found")
#если найдется, то показать Found, иначе показать Not found.
print()

print("Task 11 — Skip invalid scores")
#пропустить неверные оценки
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]
#дано список не провернных оценок
valid_scores = []
#создаю пустой список [] для оценок прощедщих проверку
total = 0
#total здесь как 
for score in raw_scores:
    if score < 0 or score > 100:
        continue
    print(score)
    valid_scores.append(score)
    total += score
 
average = total / len(valid_scores)
 
print(f"Valid scores: {valid_scores}")
print(f"Average: {average:.2f}")
 
print()
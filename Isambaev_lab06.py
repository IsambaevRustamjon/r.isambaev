print("Task 1 — Functions as values")
#ф-ции как значения
def square(number):
    return number ** 2

 
operation = square

print(square(5))
print(operation(5))
print(operation is square)
#is здесь спрашивает "это один и тот же объект?"
print()

print("Task 2 — Passing a function as an argument")
 
 
def double(number):
    return number * 2
 
 
def triple(number):
    return number * 3
 
 
def apply(operation, value):
    return operation(value)
 
 
print(apply(double, 5))
print(apply(triple, 5))
 
print()

print("Task 3 — Higher-order function")
 
 
def transform(values, operation):
    result = []
    for value in values:
        result.append(operation(value))
    return result
 
 
def square(number):
    return number ** 2
 
 
print(transform([1, 2, 3, 4], square))
 
print()

print("Task 4 — Lambda expressions")
 
double = lambda number: number * 2
add = lambda a, b: a + b
is_even = lambda number: number % 2 == 0
 
print(double(5))
print(add(3, 4))
print(is_even(8))
print(is_even(7))
 
print()

print("Task 5 — sorted() versus list.sort()")
 
numbers = [8, 3, 10, 1, 6]
 
# Part A
ordered = sorted(numbers)
print(numbers)
print(ordered)
 
# Part B
result = numbers.sort()
print(numbers)
print(result)

print()

print("Task 6 — Descending order")
 
scores = [82, 95, 73, 88, 61]
 
high_to_low = sorted(scores, reverse=True)
 
print(high_to_low)
print(scores)
 
print()

print("Task 7 — Sorting with key")
 
words = ["pear", "watermelon", "fig", "banana", "kiwi"]
 
shortest_first = sorted(words, key=len)
longest_first = sorted(words, key=len, reverse=True)
 
print(shortest_first)
print(longest_first)
 
print()

print("Task 8 — Case-insensitive sorting")
 
cities = [
    "berlin",
    "Algiers",
    "cairo",
    "Amsterdam",
    "zurich"
]
 
ordered_cities = sorted(cities, key=str.lower)
 
print(ordered_cities)
 
print()

print("Task 9 — Sorting tuples with lambda")
 
students = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
    ("Daniel", 73)
]
 
by_score = sorted(students, key=lambda student: student[1], reverse=True)
 
print(by_score)
print(by_score[0])
 
print()

print("Task 10 — Filtering values")
 
scores = [45, 70, 82, 39, 91, 60, 58]
 
passed = list(filter(lambda score: score >= 60, scores))
 
print(passed)
 
print()

print("Task 11 — Transforming values with map()")
 
prices = [100, 250, 80, 40]
 
# price + 10% of price (written this way to avoid 110.00000000000001)
increased = list(map(lambda price: price + price * 10 / 100, prices))
 
print(increased)
 
print()

print("Task 12 — Filter, sort, and map together")
 
students = [
    {"name": "Anna", "score": 82},
    {"name": "Boris", "score": 55},
    {"name": "Mira", "score": 91},
    {"name": "Daniel", "score": 67},
    {"name": "Sara", "score": 48}
]

# Step 1
passing_students = filter(lambda s: s["score"] >= 60, students)
 
# Step 2
ranked_students = sorted(passing_students,
                         key=lambda s: s["score"],
                         reverse=True)
 
# Step 3
names = list(map(lambda s: s["name"], ranked_students))
 
print(names)
 
print()
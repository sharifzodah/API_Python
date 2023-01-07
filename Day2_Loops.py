# using range() function
print(list(range(0, 5)))
name = 'Abduhamid'
chars = list(name)  # list() function converts string to a list of chars like split()
print(chars)

numbers = [45, 6, 8, -5, 23]
for i in range(0, len(numbers)):
    number = numbers[i]
    print(f"At index {i} => {number}")

# List Comprehension syntax -> [expression for element in sequence]
[print(value) for value in chars]

nums = [1, 2, 3, 4]
squared_nums = [num ** 2 for num in nums]
print(squared_nums)
print(sum(nums))

ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = [num for num in ints if num % 2 == 0]
print(even_nums)
odd_nums = [num for num in ints if num % 2 != 0]
print(odd_nums)

# using enumerate() function:
queue = ["Ann", "Sofia", "Jack"]
print(list(enumerate(queue)))

for index, name in enumerate(queue):
    print(f"{name} is at position {index}")

for index, name in enumerate(queue, start=10):
    print(f"{name} is at position {index}")

# Lambda expression
sqr_n = (lambda x: x ** 2)(3)
print(sqr_n)

# Map() function:
squares = map(lambda x: x ** 2, ints)
print(type(squares))
print(list(squares))

# Filter() function:
evens = filter(lambda x: x % 2 == 0, ints)
print(type(evens))
print(list(evens))

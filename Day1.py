a = 12
txt = "hello"
name = 'Abduhamid'
print(f"{a} {txt} {name}")
print("{} {} {}".format("output is", a, txt))
print(txt + ' ' + name)

# declaring list
values = [1, 2, 3, 4, 'test', 'api', 9]

# foreach loop
for value in values:
    print(value)

# for loop using index
for index, value in enumerate(values):
    print(index, values[index])

# printing last element of the list
print(f"last element: {values[-1]}")

# Colon usage in python:

# slicing(substring) string with specific range [inc_index, exc_index)
print(name[2:6])

# right side colon will display everything after that index [inc_index:]
print(name[4:])

# left side colon will display everything before that index [:exc_index)
print(name[:4])

# negative indexing with colons will slice from the end of the string
print(name[-5:-2])

# double colons
pyth = "What's up Ask Python"[::2]  # prints every second character starting with char at 0 index
print(pyth)

s = "What's up Ask Python"[3::2]  # prints every second character starting with char at 3 index
print(s)

languages = ["Python", "C", "Java", "Mysql", "PHP", "Ruby", "HTML"]
print(languages[2:6])  # prints values starting from second index till sixth value [2 : 6)
print(languages[:5])  # prints values from index 0 till fifth element [0:5)
print(languages[2:])  # prints all values from index 2

print(languages)
languages[2:4] = ["C#", "Kotlin"]  # replaces elements on index 2 and 3 with new values
print(languages)
languages[2:5] = ["C#", "Kotlin"]  # replaces elements on index 2, 3 with new values and removes index 4 value
print(languages)
languages.insert(3, "C++")
print(languages)
languages.append("CSS")
print(languages)
del languages[-1]
print(languages)

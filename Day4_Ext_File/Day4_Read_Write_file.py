file = open("test.txt")
# Read all content of the file
# print(file.read())
# Read n number of characters by passing parameter
# print(file.read(2))

# Read one single line at a time
# print(file.readline())

# Read all lines using While loop
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# Read all lines using For loop
# for line in file.readlines():
#     print(line)
# file.close()

# no need to close method "r" -> read mode "w" -> write mode
with open("test.txt", "r") as file:
    content = file.readlines()  # holds all contents as list
    print(content)
    with open("test.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)


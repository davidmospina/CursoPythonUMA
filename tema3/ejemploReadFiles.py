with open('ejemplo.txt') as file_object:
    contents = file_object.read()
print(contents)

print(contents.rstrip())

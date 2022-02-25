with open('ejemplo.txt') as file_object:
    lines = file_object.readlines()

for line in lines: 
    print(line.rstrip())
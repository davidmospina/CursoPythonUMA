import random
with open('numeros.txt','w') as file_object:
    file_object.write(str(list(range(0,100))))

with open('numeros.txt') as file_object:
    contents = file_object.read()
print(contents)


with open('numeros.txt','a') as file_object:
    file_object.write("\n")
    for i  in random.sample(list(range(1,100)), 10):
        file_object.write(str(i) + "\n")

with open('numeros.txt') as file_object:
    contents = file_object.read()
print(contents)
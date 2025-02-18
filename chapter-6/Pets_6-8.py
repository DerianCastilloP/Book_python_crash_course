#Description of exercise 'People 6-7'
from random import randint

"""
#Creando los nombre de las variables para no crearlas manualmente
variable_pets = {}
x = 3
for i in range(x):
    var_pets = f'pets_{i}'
    variable_pets[var_pets] = {}

print(variable_pets) # comprobando las variables

##Variables creadas
"""
pets_kinds = ['loro', 'perro', 'cotorra']
pets_names = ['perensejo', 'sutanejo', 'aquel']

number_pets = 4

animals = list()
for _ in range(number_pets):
    pets_kind = pets_kinds[randint(0, len(pets_kinds)-1)]
    pets_name = pets_names[randint(0, len(pets_names)-1)]

    pets_info = {'kind' : pets_kind, "name" : pets_name}

    animals.append(pets_info)


for animal in animals:
    print(f"\n{animal}")
    for data in animal:
        if type(animal[data]) == str:
                print(f"\t\t{data.title()} : {animal[data].title()}")
        else:
            print(f"\t\t{data.title()} : {animal[data]}")

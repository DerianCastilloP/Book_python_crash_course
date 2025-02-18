#Description of exercise 'Pets 6-8'
from random import randint, choice

#listas de mascotas
pets_kinds = ["Dog", "Cat", "Rabbit", "Parrot", "Hamster", "Turtle", "Fish",
    "Guinea Pig", "Lizard", "Ferret"]

#listas de nombres
pets_names = ['perensejo', 'sutanejo', "Firulais", "Pelusa", "Max", "Luna", "Rocky", "Simba", "Nala", "Toby",
    "Coco", "Milo", "Bobby", "Daisy", "Tom", "Jerry", "Chispa", "Bruno",
    "Kira", "Zeus", "Pandaty", "Snowball"]

number_pets = 17 #Poner la cantidad de mascotas que quieres generar

animals = list()
for _ in range(number_pets):

    #valores (caracteristicas) de las mascotas
    pets_kind = pets_kinds[randint(0, len(pets_kinds) - 1)]
    pets_name = pets_names[randint(0, len(pets_names) - 1)]
    pets_age = randint(1, 12)

    #diccionario para agragar caracteristicas de las mascotas
    pets_info = {'kind' : pets_kind, "name" : pets_name, 'age' : pets_age}

    #lista para almacenar cada mascota
    animals.append(pets_info)

i = 1

if number_pets == 0:
    print("You don't have any Pets")
else:
    for animal in animals:

        print(f"\nPets_{i}")
        i += 1

        for p_kind, p_pet in animal.items():
            if type(p_pet) == str:
                print(f"\t\t{p_kind.title()} : {p_pet.title()}")
            else:
                print(f"\t\t{p_kind.title()} : {p_pet}")

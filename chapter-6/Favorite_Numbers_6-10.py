#Description of exercise 'Favorite_Numbers 6-2'
from random import randint

names = ['Martgu', 'hutolpu', 'filreTac', 'petriSco']
person_numbers = []
favorite_numbers = dict()
#number = 0

for name in names:

    for _ in range(randint(1, 4)):
        number = randint(0, 100)
        person_numbers.append(number)

    print(f"Hello {name.title()}, What is your favorite number?: \n\t{person_numbers}")
    favorite_numbers[name] = person_numbers[:]
    person_numbers.clear()
print(f"\n{favorite_numbers}")

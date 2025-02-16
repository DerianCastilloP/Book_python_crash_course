#Description of exercise 'Favorite_Numbers 6-2'
from random import randint

names = ['Martgu'.lower(), 'hutolpu'.lower(), 'filreTac'.lower(), 'petriSco'.lower()]
favorite_numbers = dict()
number = 0

for name in names:
    number = randint(0, 100)
    print(f"Hello {name.title()}, What is your favorite number?: {number}")
    favorite_numbers[name] = number

print(f"\n{favorite_numbers}")

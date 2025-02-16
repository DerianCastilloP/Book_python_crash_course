#Description of exercise 'Polling 6-6'
from random import randint

names = ['Martgu'.lower(), 'hutolpu'.lower(), 'filreTac'.lower(), 'petriSco'.lower()]
favorite_numbers = dict()
number = 0
pollig = ['histure'.lower(), 'hutolpu'.lower(), 'ticutter'.lower(), 'petriSco'.lower()]

for name in names:
    number = randint(0, 100)
    #print(f"Hello {name.title()}, What is your favorite number?: {number}")
    favorite_numbers[name] = number
print(f"\n{favorite_numbers}\n")

for poll in pollig:
    if poll not in favorite_numbers.keys():
        print(f"{poll} you need to do the poll\n")
    else:
        print(f"{poll} Thanks for do the poll\n")
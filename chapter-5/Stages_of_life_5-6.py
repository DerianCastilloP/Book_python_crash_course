######### Stages of life 5-6 ######
from random import random, randint

age_person = randint(0, 100)

if age_person < 2:
    print(f"The person is a Baby their age is {age_person}")
elif 2 <= age_person < 4:
    print(f"The person is a Toddler their age is {age_person}")
elif 4 <= age_person < 13:
    print(f"The person is a kid their age is {age_person}")
elif 13 <= age_person < 20:
    print(f"The person is a Teenager their age is {age_person}")
elif 20 <= age_person < 65:
    print(f"The person is a Adult their age is {age_person}")
else:
    print(f"The person is a Elder their age is {age_person}")
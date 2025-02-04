#foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f"\nMy favorite food are: ")
for food in my_foods:
    print(food)

print(f"\nMy friend's favorite food are: ")
for food in friend_foods:
    print(food)
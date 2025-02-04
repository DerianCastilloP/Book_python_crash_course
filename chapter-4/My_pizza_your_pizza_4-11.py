#Description of project unit 4-11

my_pizzas = ['peperoni', 'cheese', 'bacon']
your_pizzas  = my_pizzas[:]

my_pizzas.append('vegetable')

your_pizzas.append('pineapple')

print(f'\nMy favorite Pizza are: ')
for pizza in my_pizzas:
    print(f'{pizza.title()}')

print(f"\nMy friend's favorite Pizza are: ")
for pizza in your_pizzas:
    print(f'{pizza.title()}')

print("\nWe really like Pizzas!")


#exercise 5-2

#First Tests for equality and with string

me_string = 'This is a String'
print("\nIs me_string == 'this is a string'?, I predict False")
if me_string != "this is a String":
    print("me_string != this is a string")

print("\nIs me_string == 'This is a String'?, I predict True")
if me_string == "This is a String":
    print("me_string == This is a String")

#Second Tests using the lower() method
me_string = 'This is a String'
print("\nIs me_string == 'this is a string'?, I predict True")
if me_string.lower() == "this is a string":
    print("me_string == this is a string")

#Third Numeral Test
print("\nNumeral Tests involving equality and inequality\n")
##Example 1
num_base = 7
if num_base >= 7:
    print('True')
else:
    print('False')

#Example 2
num_base = 7
if num_base > 7:
    print('True')
else:
    print('False')

#Example 3
num_base = 17
if num_base <= 16:
    print('True')
else:
    print('False')

#Example 4
num_base = 17
if num_base < 17:
    print('True')
else:
    print('False')

#fourth Test using and / or
print("\nfourth Test using and / or\n")

dog = 'perro'
horse = 'cabal'

if dog == 'perro' and horse == 'caballo':
    print("True")
else:
    print("False")
#####################
if dog == 'perro' or horse == 'caballo':
    print("True")
else:
    print("False")


#fifth and sixth Test
print("\nfourth Test using and / or\n")

my_pizzas = ['peperoni', 'cheese', 'bacon']

if 'peperoni' in my_pizzas:
    print('True')
else:
    print('False')
#######################
if not 'pepe' in my_pizzas:
    print('True')
else:
    print('False')

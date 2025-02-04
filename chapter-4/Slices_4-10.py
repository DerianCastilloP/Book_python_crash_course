#Using one of the programs you wrote in this chapter, add several
# lines to end of the program that do the following

animals = ['dog','cat','horse', 'bird', "sheep", "turtle"]

for animal in animals:
    print(f"A {animal.title()} would make a great pet")

print('\nAlmost all of these animals are mammals')

print('\n###################################################################')#################################
#new code
print(f"\nThe first three items in the list are: {animals[:3]}")

print(f"\nThree items from the middle of list are: {animals[1:4]}")

print(f"\nThe last three items in the list are: {animals[-3:]}")



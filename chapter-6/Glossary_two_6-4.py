#Description of exercise 'Glossary_2 6-4'

glossary = {
    'python' : 'Is a language of programming',
    'data_types' : 'Are how programming languages store the data',
    'string' : "Is a data type",
    'int' : "Is a data type",
    'list' : 'Is a structure of data',
    'tuple' : "Is a structure of data",
    'for' : 'Is a bucle',
    'while' : "Is a bucle",
    'if-else' : "Is a chain (conditional)"
    }
for key, value in glossary.items():
    print(f"{key.title()} : \n{value.title()}")
    print("\n")
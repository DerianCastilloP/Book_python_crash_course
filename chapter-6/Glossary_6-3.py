#Description of exercise 'Glossary 6-3'

glossary = {
    'python' : 'Is a language of programming',
    'data_types' : 'Are how programming languages store the data',
    'string' : "Is a data type",
    'list' : 'Is a structure of data',
    'for' : 'Is a bucle',
    }
for item in glossary:
    print(f"{item.title()} : \n{glossary[item].title()}")
    print("\n")
#Description of exercise 'Person 6-1'

#Data
first_name = 'gulted'
last_name = 'pistinet'
age = 26
city = 'cusco'

person = {'first_name' : first_name, 'last_name' : last_name, 'age' : age, 'city' : city}

for data in person:

    if type(person[data]) == str:
        print(f"{data.title()} : {person[data].title()}")
    else:
        print(f"{data.title()} : {person[data]}")

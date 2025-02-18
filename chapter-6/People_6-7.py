#Description of exercise 'People 6-7'

#Data
city = 'cusco'

person_0 = {'first_name' : 'gulted', 'last_name' : 'pistinet', 'age' : 27, 'city' : city}

person_1 = {'first_name' : 'Tricaste', 'last_name' : 'tistaen', 'age' : 37, 'city' : city}

person_2 = {'first_name' : 'budgat', 'last_name' : 'bitpo', 'age' : 73, 'city' : city}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\n{person}")
    for data in person:
        if data == 'first_name':
            print(f"\t#{person[data].title()}")
        else:
            if type(person[data]) == str:
                    print(f"\t\t{data.title()} : {person[data].title()}")
            else:
                print(f"\t\t{data.title()} : {person[data]}")

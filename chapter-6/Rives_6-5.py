#Description of exercise 'Rivers 6-5'

rivers = {'amazon': 'brazil-colombia-peru', 'ganges' : 'India', 'mississippi' : 'United states'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}")

print('\n')
for river in rivers.keys():
    print(f"The {river.title()}")

print('\n')
for country in rivers.values():
    print(country.title())
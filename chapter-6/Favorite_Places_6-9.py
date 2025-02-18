#Description of exercise 'Favorite Places 6-9'

favorite_places = {'Daniel' : ["Grand Canyon", "Yellowstone National Park"],
                    'yole' : ["Paris"],
                    "Kuro" : ["Bora Bora", "Maldives", "Waikiki Beach"],
                    "Larry": [],
                   }

for n_person, f_places in favorite_places.items():

    if len(f_places) > 1:
        print(f"\n{n_person.title()}'s Favorite Places are:")
    elif len(f_places) == 1:
        print(f"\n{n_person.title()}'s Favorite Place is:")
    else:
        print(f"\n{n_person.title()} doesn't have Favorite Places")

    for f_place in f_places:
        print(f"\t{f_place.title()}")

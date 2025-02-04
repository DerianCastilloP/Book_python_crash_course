#Here Description of exersice Guest_List_3-6

guests = ['Ra','Cu','to','le']
print(guests)


def guest_set():
    print(f"Hello {guests[0].title()}, I want to come to my dinner party at Carol's restaurant")
    print(f"Hello {guests[1].title()}, I want to come to my dinner party at Carol's restaurant")
    print(f"Hello {guests[2].title()}, I want to come to my dinner party at Carol's restaurant")
    print(f"Hello {guests[3].title()}, I want to come to my dinner party at Carol's restaurant")

print('\nGuests Messages')
guest_set()

not_guest = guests.pop()
print(f"\n{not_guest.title()} don't come at the dinner\n")

guests.append('Ki')
print(guests)
################################################################################################################
print('\nNew Guests Messages')
guest_set()

print('\nNotice: I found a bigger table, and I will add 3 more people')

guests.insert(0, 'Al')
guests.insert(3, 'He')
guests.append('Xo')
print(guests)

print('\nChanging New Guests Messages')
guest_set()
print(f"Hello {guests[4].title()}, I want to come to my dinner party at Carol's restaurant")
print(f"Hello {guests[5].title()}, I want to come to my dinner party at Carol's restaurant")
print(f"Hello {guests[6].title()}, I want to come to my dinner party at Carol's restaurant")
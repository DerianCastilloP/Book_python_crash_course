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
print(f'Guest people {len(guests)}')
not_guest = guests.pop()
print(f"\n{not_guest.title()} don't come at the dinner\n")

guests.append('Ki')
print(guests)

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
print(f'Guest people {len(guests)}')
########################################################################################################

print('\nNotice: I can invite only two people for dinner')

def guest_shrinking():
    not_guests_shrinking = guests.pop()

    print(f"\nHello {not_guests_shrinking}, Sorry but I don't invite you for the dinner")
    print("\n*************************************************************************************************")
    print("People in the List")
    print(guests)
    print("*************************************************************************************************")

guest_shrinking()
guest_shrinking()
guest_shrinking()
guest_shrinking()
guest_shrinking()


print('\nNew Guests Messages Finally')
print(f"Hello {guests[0].title()}, I want to come to my dinner party at Carol's restaurant")
print(f"Hello {guests[1].title()}, I want to come to my dinner party at Carol's restaurant")
print(f'Guest people {len(guests)}')
print("*************************************************************************************************")

del guests[-1]
del guests[-1]

print("\n*************************************************************************************************")
print(guests)
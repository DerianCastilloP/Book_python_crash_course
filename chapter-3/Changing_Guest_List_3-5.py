#Here Description of exersice Guest_List_3-5

guests = ['Ra','Cu','to','le']
print(guests)

def guest_set():
    print(f"Hello {guests[0].title()}, I want to come to my dinner party at Carol's restaurant")
    print(f"Hello {guests[1].title()}, I want to come to my dinner party at Carol's restaurant")
    print(f"Hello {guests[2].title()}, I want to come to my dinner party at Carol's restaurant")
    print(f"Hello {guests[3].title()}, I want to come to my dinner party at Carol's restaurant")

guest_set()

not_guest = guests.pop()
print(f"\n{not_guest.title()} don't come at the dinner\n")

guests.append('Ki')
print(guests)

guest_set()
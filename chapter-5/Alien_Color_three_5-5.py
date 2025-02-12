######## Alien Colors #3 ##########

colors = ["green", "red", "yellow"]
alien_color = colors[0] #Change the value for evaluate each form

if alien_color == colors[0]:
    print(f"Alien down's color is {alien_color}")
    print('You earn 5 points')
elif alien_color == colors[2]:
    print(f"\nAlien down's color is {alien_color}")
    print('You earn 10 point')
else:
    print(f"\nAlien down's color is {alien_color}")
    print('You earn 15 point')
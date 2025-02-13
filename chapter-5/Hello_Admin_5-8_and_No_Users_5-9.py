######## Hello Admin 5-8 and No users 5-9 #####

usernames = ['lora', 'admin', 'arol', 'durel', 'lerud']
#usernames = []

if usernames:
    for username in usernames:
        if username.lower() == 'admin':
            print(f"\nHello {username.title()}, Would you like to see a status report?")
        else:
            print(f"\nHello {username.title()}, thank you for logging!")
else:
    print("We need to find some users!")
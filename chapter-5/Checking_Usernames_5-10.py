######## Checking Usernames 5-10 #####

current_users = ['lora', 'admin', 'arol', 'durel', 'lerUD'] # Main list
new_users = ['kurtop', 'lerud', "arret"]

copy_current_list = list() #copy list for case-insensitive

#list for a lower version
for current_user in current_users:
    copy_current_list.append(current_user.lower())

#continue the program

for new_user in new_users:
    if new_user.lower() in copy_current_list:
        print(f"\nSorry, but the username {new_user.title()} is not available, you need to change it")
    else:
        print(f"\nThanks for your register, the username {new_user.title()} is available")

'''
5-8. Hello Admin: Make a list of five or more usernames, including the name 
'admin'. Imagine you are writing code that will print a greeting to each user 
after they log in to a website. Loop through the list, and print a greeting to 
each user. 

If the username is 'admin', print a special greeting, such as Hello 
admin, wouldyou like to see a status report? 

Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging 
in again.
'''
users=['anna','caleb','admin','mousy','charlie']

for user in users:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status repot?")
    else:
        print(f"Hello {user.title()}, thank you for logging in.")    

'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users 
is not empty.

If the list is empty, print the message 'We need to find some users!

Remove all of the usernames from your list ad make sure the correct message is 
printed.
'''

users=[]

if users:
    for user in users:
        print(f"Hello {user.title()}, welcome back!")
else:
    print("We need to find some users!")

'''
5-10. Checking Usernames: Do the following to create a program that simulates 
how websites ensure that everyone has a unique username. 

Make a list of five or more usernames called current_users.

Make another list of five usernames called new_users. Make sure one or two of 
the new usernames are also in the current_users list.

Loop through the new_users list to see if each new username has already been 
used. If it has, print a message that the person will need to enter a new 
username. If a username has not been used, print a message saying that the 
username is available.

Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' 
should not be accepted. (To do this, you’ll need to make a copy of current_users 
containing the lowercase versions of all existing users.)
'''
current_users=['anna','Caleb','mousy','charlie','bean']

new_users=['Anna','ben','dean','sadie','kole']


current_users_lower=[user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is unavailable")
    else:
        print(f"The username '{new_user}' is available")    
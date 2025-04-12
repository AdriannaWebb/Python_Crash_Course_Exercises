'''
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner. 
'''
guest_list = ['caleb', 'mom', 'dad', 'kellie']

for i in guest_list:
    print(f'{i.title()}, You are formally invited to dinner on 12/1/2025. Please let me know if you can attend.')

''' 
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. 
  - Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it. 
  - Modify your list, replacing the name of the guest who can’t make it with the name of the new   person you are inviting. 
  - Print a second set of invitation messages, one for each person who is still in your list.
'''
print(guest_list[3])

guest_list[3]='kait'

for i in guest_list:
    print(f'{i.title()}, You are formally invited to finner on 12/1/2025. Please let me know if you can attend')
  
'''
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. 
  - Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your   program,   informing people that you found a bigger table. 
  - Use insert() to add one new guest to the beginning of your list. Use insert() to add one new guest to the middle of your list. 
  - Use append() to add one new guest to the end of your list. Print a new set of invitation messages, one for each person in your list.
'''
print('I have found a bigger table! I will be inviting more guests soon')

guest_list.insert(0,'liv')
guest_list.insert(2,'sadie')
guest_list.append('kole')

for i in guest_list:
    print(f'{i.title()}, You are formally invited to finner on 12/1/2025. Please let me know if you can attend')

'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests. Start with your program from Exercise 3-6. 
Add a new line that prints a message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop() a name, print a message to that person leeting them know you are sorry you cant invite them to dinner.
Print a message to each of the two people still on your list, letting them know they're still invited
Use del to remove the last two names from your list so it is empty.
print the empty list
'''

print("My table won't arrive on time so I can now only invite two people for dinner")

uninvited = guest_list.pop(0)
print(f'{uninvited.title()}, I am sorry to inform you that you can no longer attend the dinner.')

uninvited = guest_list.pop(0)
print(f'{uninvited.title()}, I am sorry to inform you that you can no longer attend the dinner.')

uninvited = guest_list.pop(0)
print(f'{uninvited.title()}, I am sorry to inform you that you can no longer attend the dinner.')

uninvited = guest_list.pop(2)
print(f'{uninvited.title()},I am sorry to inform you that you can no longer attend the dinner.')

uninvited = guest_list.pop(2)
print(f'{uninvited.title()}, I am sorry to inform you that you can no longer attend the dinner.')

print(f'I am inviting {len(guest_list)} people for dinner')

for i in guest_list:
    print(f'{i.title()}, You are still formally invited to finner on 12/1/2025. Please let me know if you can attend')

del guest_list[0]
del guest_list[0]

print(guest_list)


    

'''
3-8. Seeing the World: Think of five places you'd like to visit
- Store the locations in a list
- Print the list in it's original order
- Use sorted() to print your list in alphabetical order without modifying the actual list
- Show that your list is still in its original order by printing it 
- Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. 
- Show that your list is still in its original order by printing it again. 
- Use reverse() to change the order of your list. 
- Print the list to show that its order has changed. 
- Use reverse() to change the order of your list again. 
- Print the list to show it’s back to its original order. 
'''
print('Here is a list of five places I would like to visit')
visit=['italy','france','uk','spain','greece']
print(visit)

print('\nHere is my temorarily sorted list:')
print(sorted(visit))

print('\nHere is proof that the sorted() function is temporary:')
print(visit)

print('\nHere is my temorarily reverse sorted list:')
print(sorted(visit,reverse=True))

print('\nHere is proof that the sorted() function is temporary:')
print(visit)

print('\nHere I am permanently reversing my list:')
visit.reverse()
print(visit)

print('\nHere is proof that the reverse() method is permanent:')
print(visit)

print('\nHere I am permanently re-reversing my list:')
visit.reverse()
print(visit)





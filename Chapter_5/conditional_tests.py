'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
describing each test and your prediction for the results of each test. Your code 
should look something like this:
car = 'subaru' 
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru') 
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi')
'''

# Test 1
my_cat='mousy'
cat_last_name='webb'
cat_personality=['sassy','cute','playful','cuddly']
cat_can=['meow','eat','play']
cat_cant=['talk','clean','drive']

print("is my cat == 'mousy'? I predict True")
print(my_cat=='mousy')

print(f"\nIs cleaning within my cat's capabilities? I predit: False")
print('clean' in cat_can)

if 'play' in cat_can and 'clean' in cat_cant:
    print('\nI think this will evaluate to True')
    print(f'My cat, {my_cat}, can play but not clean!')

print(f"""\nIs my cat's full name == {my_cat.title()} { cat_last_name.title()}? 
I preditct: True""" )
print(my_cat=='mousy' and cat_last_name=='webb')

'''
5-2. More Conditional Tests: Have at least one True and one False result for 
each of the following:
- Tests for equality and inequality with strings
- Tests using the lower() method
- Numerical tests involving equality and inequality, greater than and less than, 
  greater than or equal to, and less than or equal to
- Tests using the and keyword and the or keyword
- Test whether an item is in a list
- Test whether an item is not in a list
'''

# Tests for equality and inequality with strings
print("\nIs my cat's name not 'mousy'? I predict False")
print(my_cat != 'mousy')
print("\nIs my cat's name 'bean'? I predict False")
print(my_cat == 'bean')

# Tests using the lower() method
hair='Blonde'
print("""Is the hair color 'blonde' in the list regaurdless of capitalization?
I predict True.""")
print(hair.lower() == 'blonde')

# Numerical tests involving equality and inequality, greater than and less than, 
# greater than or equal to, and less than or equal to
hours=24
minutes=1440
seconds=866400

print('\nAre there more than 24 hours in a day? I predict False.')
print(hours>24)

print('\nAre there greater than or equal to 1440 minutes in a day? I predict True.')
print(minutes>=1440)

print('\nAre there less than 24 hours in a day? I predict False')
print(hours<24)

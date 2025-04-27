# If Statements
We use if statements to examine a set of conditons and decide which action to 
take based on those conditoins. 
The following statement loops through a list and evaluates the if statement to 
decide if the letters should be printed in all caps or just title case based on
 which part evaluates to true
```
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else :
        print(car.title())
```        
## Conditional Tests
At the core of every `if` statement is an expression that can be evaluated as 
`True` or `False` The *equality operator* is the double equal signs because the 
single equal sign is an assignment of a variable to a value. 

### Ignoring Case When Checking for Equality
Python is case sensitive so it will not return `True` if you have the same word 
in title case and lowercase. To check for equality while ignoring case, use the 
`.lower()` string method to temporarily convert a string to lowercase.
```
car = 'Audi'

car=='audi' # Results in False
car.lower()=='audi'#Results in True
```
This test will return True no matter how the value 'Audi' is formatted because 
the test is now case insensitive.

A good example of when this is needed is with website usernames. A website may 
want to make sure that a username is truely unique by compraing it agianst other
usernames in all lowercase.

### Checking for Inequality
When you want to determine whether two values are not equal, you can use the 
*inequality* *operator* `!=`.

```
requested_topping='mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies')
else:
    print('We got another one!')
```

### Numerical Comparisons
Very similar to checking for text equality or inequality but you can also check
for >,<, =<,>=

```
answer = 17 
if answer != 42:
     print("That is not the correct answer. Please  try again!")
```
## Checking Multiple Conditions
You may need two conditions to be `True` to take an action (like both username 
and password are correct to unlock a device). Or that one thing is true while 
the other is not (Maybe that someone passes a background check and does not have
any firings in their past). 

### Using and to Check Multiple Conditions
To check whether two conditions are both `True`, simultaneously use the keyword
`and` to combine two conditonal tests. If each test passes, the overall 
expression evaluates to `True`. If either condition is not met, the expression 
evaluates to `False`. 

To improve readability, you can use parentheses around the individual tests, 
but they are not required.
```
(age_0 >= 21) and (age_1 >= 21)
```
### Using or to Check Multiple Conditions
The keyword `or` allows you to check multiple conditions as well, but if either 
or both conditions pass the test, the expression evaluates to `True`. 

### Checking Whether a Value Is in a List
You may want to check if a value is in a list before taking an action, like in
the unique username example. 
In that case you can use the `in` keyword.
```
requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_toppings
``` 
this will output `True` or `False` depending on if the value is in the list or 
not. 

### Checking Whether a Value is Not in a List
Other times, it's important to know if a vlaue does *not* appear in a list. In 
that case, use the keyword `not in`
```
banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')
```
## Boolean Expressions
A **Boolean expression** is just another name for a conditionaltest. A 
**Boolean value** is what the conditional test evaluates to and is either `True` 
or `False`.

Boolean values are often used to keep track of certain conditons, such as 
whether a game is running or whether a user can edit certain content on a 
website:
```
game_active=True
can_edit=False
```
Boolean values provide an efficient way to track the state of a program or a 
particular condition that is important in the behavior of the program.

## if Statements
Several kinds of `if` statements exist and which one to use depends on the 
number of conditions you need to test.

### Simple if Statements
The simplest kind of `if` statement has one test and one action:
```
if conditional_test:
    do something
```
You can put any conditional test in the first line and just about any action
in the indented block following the test. If the test evaluates to `True`, Python
executes the code following the `if` statement     
### if-else Statements
These are used when you want an action to be taken when the if statement
evaluates to `False`. 
```
print('Please enter your age:')
age=input()
age_int = int(age)

if age_int >= 18:
    print('You are eligable to vote!')
else:
    years = 18 - age_int
    print(f'You can vote in {years} years!')
```    
This code works because it has only two possible situations to evaluate: a 
person is either old enough to vote or not old enough
### The if-elif-else Chain
In the event that you need to test more than two possible situations and 
evaluate these you can use this. Python executes only *one* block in the 
chain. It executes the block of code following the first condition that 
evaluates to `True` and then exits the chain. 
```
age=12
if age <= 4:
    price=0
elif age <= 18:
    price=25
else:
    price=40

print(f"Your admission cost is ${price}.")       
```
### Omitting the else Block
An `else` is not required to complete an if-elif chain. The else block is a 
catchall statement. It matches any condition that wasn’t matched by a specific 
if or elif test, and that can sometimes include invalid or even malicious data. 
By not finishing the code with an `else`, you can be confident that your code 
will only work in the correct conditons and be alerted to any variables you may 
not have accounted for.

### Testing Multiple Conditions
The if-elif-else chain is powerful, but it's only appropriate to use when you 
just need one test to pass. As soon as one test evaluates to `True`, Python will 
execute the block associated with that test and then exit the test without 
evaluating the tests that follow. 

However, sometimes it's important to check all conditions of interest. If so, 
you should use a series of simple `if` statements with no elif or else blocks. 
It's best used when you want to act on every instance that a test evaluates to 
`True`, not just the first one. 

Example: If someone requests a two-topping pizza, you need to include both: 
```
requested_toppings=['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")    
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")    

print("\nFinished making your pizza!")
```
## Using if Statements with Lists
Combining lists and if statements can come in handy. You can watch for special 
values that need to be treated differently than other values in a list. 

### Checking for Special Items
Continuing with pizza examples:
```
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 

for requested_topping in requested_toppings:
     print(f"Adding {requested_topping}.") 
 
print("\nFinished making your pizza!")
```
But what if the pizzeria runs out of green peppers? An if statement inside the 
for loop can handle this situation appropriately:
```
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 

for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry, we're out of green pepers right now.")
    else:
        print(f"Adding {requested_topping}.")  

print("\nFinished making your pizza!")
```
### Checking That a List Is Not Empty
So far, we've assumed that all of our lists have content. Soon we'll want to let
 users provide the information that's stored in a list so we won't be able to 
 assume that a list has any items in it each time a loop is run. You can check 
 if a list is empyt **before** running a `for` loop. 

```
requested_toppings:[] #empty list

if requested_toppings:    #returns True if not empty and False if empty
    for requested_topping in requested_toppings:         
        print(f"Adding {requested_topping}.")
             print("\nFinished making your pizza!")
else:     
    print("Are you sure you want a plain pizza?")
```
When the name of a list is used in an `if` statement, Python return `True` 
if the list contains at least one item. If the list had an item, it would result in 'True' and continue onto the `for` loop. Because it is empty and returns `False` it goes to the else statement. 
### Using Multiple Lists
The following example defines two lists. The first is a list of available toppings at the pizzeria. The second is a list of toppings that the user has requested. We check each item in requested_toppings against the list, available_toppings.
```
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppins:
    if requested_topping in available_toppings:
        print(f"Adding{requested_topping}" )
    else:
        print(f"Sorry, we don't have {requested_topping}.") 

print("\nFinished making your pizza!")        
```


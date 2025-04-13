# Working with Lists 
Loops are great because they allow you to work on each item on a list with just 
a few lines of code rather than repetative lines.

## Looping through an Entire List
When you want to do the **same action** with every item in a list, you can use 
Python’s for loop. 
```
# Define list
magicians = ['alice', 'david', 'carolina'] 

# Define for loop
for magician in magicians:     
    print(magician)
```
The line `for magician in magicians:` tells Python to pull a name from the list magicians and associate it with the **variable** magician. 

## Adding More Lines to a for Loop
You can write as many lines of code in the for loop as you want as long as they 
are indented. For each line added, the action will be performed on the list 
element that has been assigned to the variable before moving to the next list 
element.
```
# Define list
magicians = ['alice', 'david', 'carolina'] 

# Define for loop
for magician in magicians:     
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```    
Because we have indented both calls to `print()`, each line will be executed 
once for every magician in the list. The newline `("\n")` in the second 
`print()` call inserts a blank line after each pass through the loop. This 
creates a set of messages that are neatly grouped for each person in the list, 
here is the output:
```
Alice, that was a great trick! 
I can't wait to see your next trick, Alice. 

David, that was a great trick! 
I can't wait to see your next trick, David. 

Carolina, that was a great trick! 
I can't wait to see your next trick, Carolina.
```
In practice, you’ll often find it useful to do a number of different operations 
with each item in a list when you use a for loop.

## Doing Something After a for Loop
To move on from the for loop, simply decrease the indent to 0 and write a new 
line of code. Any lines not indented after the for loop are executed once 
without repetition. It's good practice to to summarize an operation that was 
performed on the entire data set in the first line after the exited for loop
```
magicians = ['alice', 'david', 'carolina'] 

for magician in magicians:     
    print(f"{magician.title()}, that was a great trick!")     
    print(f"I can't wait to see your next trick, {magician.title()}.\n") 
    
print("Thank you, everyone. That was a great magic show!")
```
## Avoiding Indentation Errors
Python uses indentation to determine how lines of code are related to the rest 
of the program. Indentation can be done on many levels, especially in larger 
programs. 

### Forgetting to Indent:
```
magicians = ['alice', 'david', 'carolina'] 

for magician in magicians:     
    print(f"{magician.title()}, that was a great trick!")     
print(f"I can't wait to see your next trick, {magician.title()}.\n") 
```
This will result in output like this:
```
   File "magicians.py", line 3     
  print(magician)     
  ^ 
IndentationError: expected an indented block after 'for' statement on line 2
```
### Forgetting to Indent Additional Lines:
This is a *logical* error. The syntax is valid Python code, but the code does 
not produce the desired result because a problem occurs in its logic.
```
magicians = ['alice', 'david', 'carolina'] 

for magician in magicians:     
    print(f"{magician.title()}, that was a great trick!")     
print(f"I can't wait to see your next trick, {magician.title()}.\n") 
```
Will output like this: 
```
Alice, that was a great trick! 
David, that was a great trick! 
Carolina, that was a great trick! 
I can't wait to see your next trick, Carolina.
``` 
The program will still run because there is at least one indented line of code 
after the defenition of the for loop but when it sees the second print call 
using the magicians variable, it only performs it once on the name that was last stored in the variable. 
### Indenting Unnecessarily 
If you accidentally indent a line that doesn't need to be like this: 
```
message = "Hello Python world!"     
    print(message)
```
Python will give you an error message like this:
```
   File "hello_world.py", line 2
  print(message)    
  ^ 
IndentationError: unexpected indent
```
### Forgetting the Colon
The colon at the end of a for statement tells Python to interpret the next line 
as the start of a loop.
```
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians     
    print(magician)
```
You'll get an error similar to this:
```
   File "magicians.py", line 2     
  for magician in magicians                              
            ^ 
SyntaxError: expected ':'
```
## Making Numerical Lists
Lists are ideal for storing sets of numbers. Python’s range() function makes it 
easy to generate a series of numbers. For example, you can use the range() 
function to print a series of numbers like this:
```
for value in range(1, 5):     
    print(value)
```
This will print the numbers 1-4 because Python will go up to but not include 
the number that completes the range. This is because you're listing the stop 
value so when it sees that it has reached 5, i will stop the loop rather than continue. 

## Using range() to Make a List of Numbers
You can make a list from a range of numbers by using the `lis()` function
When you wrap `list()` around a call to the `range()` function, the output 
will be a list of numbers. 
```
numbers = list(range(1, 6)) 
print(numbers)
```
You can also ask Python to skip numbers in a given range by using a third 
argument after the first two that define a range:
```
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)
```
### Using range() and list() to Make Any List of Numebrs
You can get a list of numbers in many ways with this, you can user operators 
on the values in a range to get a more advanced list like this:
```
squares=[]

for value in range(1,11):
    square=value**2
    squares.append(square)

print(squares)
```
You can simplify this function by performing the opperation on the list elements
and adding them to the lsit at the same time:
```
squares=[]

for value in range(1,11):
    squares.append(value**2)

print(squares)
```    
### Simple Statistics with a List of Numbers
```
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

min(digits)
max(digits)
sum(digits)
```
## List Comprehensions
A **list comprehension** allows you to create the example above (using the 
squares) in just one line of code. It combines the `for` loop and the creation 
of new elements into one line and automatically appends each new element. 
```
squares = [value**2 for value in range(1, 11)] 
print(squares)
```
after creating the list name, the square brackerts tell Python it will be a 
list, then the expression for the values you want to store in the new list is 
defined. Then the for loop is created with the for statement and followed by 
`value in range(1,11).
This code does the exact same thing as the other ones, it is just more concise. 

## Working with Part of a List
You can also work with a specific group of items in a list, called a **slice** 
in Python.
### Slicing a List
To make a slice, you specify the index of the first and last elements you want 
to work with. As with the `range()` function, Python stops one item before the 
second index you specify.
```
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
```
If you omit the first index in a slice, Python automatically starts your slice 
at the beginning of the list:
```
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[:4])
```
Similarly, if you don't add a number to the right of the colon, it will slice 
from your starting index and go to the end of the list as it's default setting. 

Also, You can include a third value in the brackets indicating a slice. If a 
third value is included, this tells Python how many items to skip between items 
in the specified range.

### Looping Through a Slice
You can use a slice in a for loop after the list name if you want to loop 
through a subset of the elements in a list.
```
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 

print("Here are the first three players on my team:")
for player in players[:3]:     
    print(player.title())
```
## Copying a List
To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index `[:]`. This tells Python to make 
a slice that starts at the first item and ends with the last item, producing a 
copy of the entire list.
```
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 

print("My favorite foods are:") 
print(my_foods) 

print("\nMy friend's favorite foods are:") 
print(friend_foods)
```

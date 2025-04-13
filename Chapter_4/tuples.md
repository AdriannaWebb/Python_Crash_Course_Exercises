# Tuples
Lists work well for storing collections of items that can change throughout the 
life of a program but if you need to make a "list" that cannot change, use a 
Tuple

In Python, values that cannot change are called **immutable**. An immutable list
 is called a **tuple**. 

## Defining a Tuple
A tuple looks just like a list, but We define the tuple **dimensions**, using **parentheses** instead of square brackets. 
Just like a list, you can access elements in the tuple by using each items index 
and square brackets.
```
userID=(1246,1887,9933,8965)
```

Tuples are technically defined by the presence of a comma; the parentheses make 
them look neater and more readable. If you want to define a tuple with one 
element, you need to include a trailing comma:
```
my_tuple=(3,)
```
## Looping Through All Values in a Tuple

This works just like it does for lists:
```
dimensions=(200,50)

for dimension in dimensions:
    print(dimension)
```
## Writing Over a Tuple    
While you can't modify a tuple, you can assign a new value to a variable that represents a tuple, similar to changing the value assinged to a variable. 
```
dimensions = (200, 50) 
print("Original dimensions:") 
for dimension in dimensions:
     print(dimension) 
 
dimensions = (400, 100) 
print("\nModified dimensions:") 
for dimension in dimensions:
     print(dimension)
```

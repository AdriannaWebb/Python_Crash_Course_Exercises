# Lists
A list allows you to store sets of information in one place. Lists tie together many importatn concepts in programming as well.

## About Lists 
-A list is a collection of items in a particular order. 
-Lists can contain any information.
-Because lists contain many elements, the name of a list should be plural

### Formatting a list
Square brackets `[]` indicate the start and end of a list and the individual list elements are spearated by commas `,`

```
cat_colors = ['black', 'organge', 'tabby', 'white']
print(cat_colors)
```
### Acessing Elements in a list
You can access the elements of a list by telling Python the position, or index, of the element you want to access.

List indexes always start at 0, so it is important to account for this when trying to access an element

To quickly access an element at the end of a list without counting, it is also possible to ask for a negative indexed position. If 0 is the first element in a list, then -1 is the last, -2 is the second to last ect.

```
print(cat_colors[0])
```

### String Methods on Lists and List Elements

You can also use the string methods (in the event your list is made up of strings) on the elements in a list

```
print(cat_colors[0].title())
```

### using Individual Values from a List
You can use any individual value from a list as if it were a variable. 
Here is how you can do this with f strings:
```
message= f'My first cat was a {cat_colors[0].title()} cat!'
print(message)
```

## Modifying, Adding, and Removing List Elements

Most lists are ment to change throughout the course of a program. 

### Modifying List Elements
To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have

```
cat_colors=['black','orange','tabby','white]
print(cat_colors)

cat_colors[1]='brown'
print(cat_colors)
```

### Appending Elements to a List

**Appending** an element to the end of a list is the easiest way to add a new list element. You can use the .append() method after the list name to do this
```
cat_colors.append('orange')
```
The `.append()` method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of `.append()` calls.
```
motorcycles=[] #Empty list to start

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
```
### Inserting Elements into a list
 You can add a new element at any positon in your list by using the `.insert()` method. You do this by specifying the index of the new element and the new value
```
 motorcycles = ['honda', 'yamaha', 'suzuki'] 
 
 motorcycles.insert(0, 'ducati') 
 print(motorcycles)
```
Doing this shifts all of the other values to the left and inserts the value at the index specified 

### Deleting Elements from a List
The **del** statement
If you know the index position of the item you want to remove you can use the `del` statement. Doing it this way deletes the list element entirely and you cannot access it after.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```
The **pop()** method
If you want to work with an item after it's removed from the list, you can use the `pop()` method
The `pop()` method removes the last item in the list and then lets you work with it.
The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```



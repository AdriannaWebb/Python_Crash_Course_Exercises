'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 
'yellow', or 'red'.
- Write an if statement to test whether the alien’s color is green. If it is, 
  print a message that the player just earned 5 points.
- Write one version of this program that passes the if test and another that fails.
  (the version that fails will have no output.)
'''
# Passes
alien_color='green'

if alien_color=='green':
    print("You've earned 5 points!")

# Fails
alien_color='red'

if alien_color=='green':
    print("You've earned 5 points!")

'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, 
and write an if-else chain.
- If the alien’s color is green, print a statement that the player just eared
  5 points
- If the alien's color isn't green, print a statement that the player just earned
  10 points.
- Write one version of this program that runs the if block and another that runs 
  the else block    
'''
# Runs if block
alien_color='green'

if alien_color=='green':
    print("You've earned 5 points!")
else:
    print("You've earned 10 points!")    

# Runs else block
alien_color='red'

if alien_color=='green':
    print("You've earned 5 points!")
else:
    print("You've earned 10 points!")    
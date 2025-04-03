
# Strings
# Always incased in '' or ""


# String methods
# Side note: a method is an action that python can perform on a piece of data
# every method is followed by a set of parentheses because they can include special instructions called arguments

# Title method

'''
name = "ada lovelace"
print(name.title())

# the string 'ada lovelace' is stored in the name variable. the title() method makes the first letters capitalize
# the dot after the name variable and before title() tells python to use the title method on the name variable
# similarly, you can use .upper() and .lower()

print(name.upper())
print(name.lower())
'''


# String Concatenation
# Combines seperate strings into one. You can do this using the + sign between two strings or
# two variables containing strings.
# To include a space btween strings, create and empty string in between the strings/variables
# you are concatenating

'''
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #Automatically includes space btween strings in the variables
full_name_title = full_name.title()
full_name_upper = full_name.upper()
full_name_lower = full_name.lower()
message = f"Hello, {full_name.title()}!" # creates a variable named message that uses an f string to greet the user in title case using .title() on the full_name variable

print(first_name)
print(last_name)
print(full_name)
print(full_name_title)
print(full_name_upper)
print(full_name_lower)
print(message)
'''

# To trim strings of extra white space, use .rstrip() or .lstrip() or .strip() method with a string/string variable

'''
favorite_language = 'python '
print(favorite_language.strip())
'''

# You can also permanently strip the white space from the variable by re-assigning the variable and attatching .strip()

'''
favorite_language = favorite_language.strip
print(favorite_language)
'''
#To trim a prefix, like the begining of a URL, you can use the .removeprefix('') method

'''
nostarch_url='https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://') #Uses the .removeprefix on the varaible to reassign the varable to the url without the prefix
print(nostarch_url)
'''

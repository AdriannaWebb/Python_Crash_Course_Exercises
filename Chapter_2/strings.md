# Strings

Strings are always encased in `''` or `""`.

# String Methods

A method is an action that Python can perform on a piece of data. Every method is followed by a set of parentheses because they can include special instructions called arguments.

## Title Method

```python
name = "ada lovelace"
print(name.title())
```
The string 'ada lovelace' is stored in the name variable. The title() method makes the first letters capitalize. The dot after the name variable and before title() tells Python to use the title method on the name variable. Similarly, you can use .upper() and .lower().

print(name.upper())
print(name.lower())

## String Concatenation
Combines separate strings into one. You can do this using the + sign between two strings or two variables containing strings. To include a space between strings, create an empty string in between the strings/variables you are concatenating.

```
pythonCopyfirst_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # Automatically includes space between strings in the variables
full_name_title = full_name.title()
full_name_upper = full_name.upper()
full_name_lower = full_name.lower()
message = f"Hello, {full_name.title()}!" # Creates a variable named message that uses an f string to greet the user in title case using .title() on the full_name variable

print(first_name)
print(last_name)
print(full_name)
print(full_name_title)
print(full_name_upper)
print(full_name_lower)
print(message)
```

## Trimming Whitespace
To trim strings of extra white space, use .rstrip() or .lstrip() or .strip() method with a string/string variable.
```
pythonCopyfavorite_language = 'python '
print(favorite_language.strip())
```
You can also permanently strip the white space from the variable by re-assigning the variable and attaching .strip().
```
pythonCopyfavorite_language = favorite_language.strip()
print(favorite_language)
```
## Removing Prefixes
To trim a prefix, like the beginning of a URL, you can use the .removeprefix('') method.
```
pythonCopynostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://') # Uses the .removeprefix on the variable to reassign the variable to the URL without the prefix
print(nostarch_url)
```
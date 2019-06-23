# Palindrome Example
# Palindrome String - dad, mom, madam, 121, 1120211

myString = "Madam"
myString = myString.casefold()
revString = reversed(myString)

if list(revString) == list(myString) :
    print( "String is Palindrome")
else:
    print( "String is not Palindrome")

#Strings

print("Football Club")

# To print in another line use \n
print("Football\nClub") 

#To print quotation mark
print("Football\"Club")

#Using String variables

word = "Football"
print(word)
print(word + " is fun.")

#To change it to lower/uppercase
print(word.lower())
print(word.upper())

#To check is all the letters are in lower/uppercase
print(word.islower())
print(word.isupper())


print(word.upper().isupper()) # Now it will return true as we have converted all letters to capitals
print(word.lower().islower()) # Now it will return true as we have converted all letters to lowercase

#To find the length of the string
word = "football"
print(len(word)) #8

# It will count the spaces as well

word = " football"
print(len(word)) #9

#To access each character
print(word.index("a"))
print(word[0]) #chatacter index start from 0

print(word.index("a")) #to find the index of the character

word = "football is fun"
print(word.replace("fun", "thrilling")) # To replace a word












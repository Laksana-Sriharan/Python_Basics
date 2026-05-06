#Lists uses square brackets
countries = ["Italy", "France", "Denmark","Ireland", "Singapore", "Sweden"]
print(countries)

#Lists can have multiple data type as its elements
list1 = ["Italy", 9, False,"Ireland"]
print(list1)

#To access the elements of the list
print(countries[0]) #Elements from left to right starts from 0 
print(countries[2])

#Negative indexing
print(countries[-1]) #Elements from right to left starts from -1

#Slicing the list
print(countries[2:4]) # Denmark and Ireland only will be displayed (position 4 is ignored)
print(countries[1:])

#Modifying the elements in the list
countries[1] = "USA"
print(countries)

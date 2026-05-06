number = [1,6,9,3,8,2]
countries = ["Italy", "France", "Denmark","Ireland", "Singapore", "Sweden"]

print(countries)
#To add both the list
countries.extend(number)
print(countries)

countries = ["Italy", "France", "Denmark","Ireland", "Singapore", "Sweden"]

#To add an element at the end
countries.append("USA")
print(countries)

#To insert an element in the module
countries.insert(2,"South Korea")
print(countries)

#To remove an element in the module
countries.remove("Denmark")
print(countries)

#To remove/clear the entire list elements
countries.clear()
print(countries)

#To remove the last element
countries = ["Italy", "France", "Denmark","Ireland", "Singapore", "Sweden"]
print(countries)
countries.pop()
print(countries)

#To find the index of an element
print(countries.index("Singapore"))

#To count how many times an element exist in a list
countries = ["Italy", "France", "Denmark","Denmark","Denmark","Denmark","Ireland", "Singapore", "Sweden"]
print(countries.count("Denmark"))

#To copy a list
countries2 = countries.copy()
print(countries2)

#To have the elements in ascending order
print(number)
number.sort()
print(number)

#To reverse the elements in the list
print(countries)
countries.reverse()
print(countries)

#FOR Loop in Python

#Task 1
for words in "Light House":
    print(words)

#Task 2
mates = ["Adam", "John", "Richard", "Rosy"]
for mate in mates:
    print(mate)

#Task 3
for number in range(12):
    print(number) #prints 0-11

#Task 4
for number in range(5,12):
    print(number) #prints 5-11

#Task 5
for index in range(len(mates)):
    print(index)

#Task 6
for index in range(len(mates)):
    print(mates[index])

#Task 7
for index in range(5):
    if index == 0:
        print("First Number")
    else:
        print("Second Number")

#IF Statements in Python

#Task 1

is_doctor = True


if is_doctor:
    print("You are a doctor!")
else:
    print("You are not a doctor!")

#Task 2
    
is_tall = True

if is_doctor or is_tall:
    print("You are a doctor otherwise you are tall or both")
else:
    print("You are not a doctor neither tall")

#Task 3

if is_doctor and is_tall:
    print("You are a tall doctor")
else:
    print("You are not a doctor or not tall or both")

#Task 4

is_doctor = True
is_tall = False

if is_doctor and is_tall:
    print("You are a tall doctor")
elif is_doctor and not(is_tall):
    print("You are a short doctor")
elif not(is_doctor) and is_tall:
    print("You are tall")
else:
    print("You are not a doctor neither tall")

dayconverter = {
    "Sun": "Sunday",
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thurs": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday"
}

print(dayconverter.get("Mon"))
print(dayconverter.get("Hat"))  #Will show None
print(dayconverter.get("Hat", "This is an invalid code")) # Now it will show the message given instead of None


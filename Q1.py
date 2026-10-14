username = input("Enter your username: ")

if len(username) < 5:
    print("Invalid username: Must contain at least 5 characters.")
elif username.isspace():
    print("Invalid username: Username cannot contain only spaces.")
elif username.lower() == "admin":
    print("Invalid username: 'admin' is not allowed.")
else:
    print("Valid username.")

#validate username entered by user
#1.Username is no more than 12 characters
#2.Username must not contain spaces
#3.Username must not contain digits

username = input("Enter your username: ")
if len(username) > 12:
    print(f"{username} is invalid because it has more than 12 characters")
elif username.count(" ") != 0:
    print(f"{username} is invalid becuase it contains space")
elif not username.isalpha():
    print(f"{username} is invalid because it contains numbers")
else:
    print(f"Welcome {username}")
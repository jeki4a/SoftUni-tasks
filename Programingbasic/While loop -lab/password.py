username = input()
passwordDB = input()

password = input()

while password != passwordDB:
    password = input()
    if password == passwordDB:
        break

print(f"Welcome {username}!")


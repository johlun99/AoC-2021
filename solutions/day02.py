data = open("../inputs/day02.txt", "r")
lines = [line.strip() for line in data.readlines()]

valid_passwords = []

for line in lines:
    key, value = line.split(": ")
    
    v1, v2 = key.split(" ")[0].split("-")
    password = key.split(" ")[1]
    print("Password " + password)

    if (int(v1) <= value.count(password) <= int(v2)):
        valid_passwords.append(value)


print(len(valid_passwords))
final_string = ""

while True:
    string = input()
    if string == "End":
        exit()
    elif string == "SoftUni":
        continue
    else:
        for char in string:
            final_string += char*2
        print(final_string)
        final_string = ""

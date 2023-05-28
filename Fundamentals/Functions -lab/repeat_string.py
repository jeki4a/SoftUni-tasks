string = input()
repeats = int(input())

repeated_string = ""

def repeat(string, repeats, repeated_string):
    for _ in range(repeats):
        repeated_string += string
    return repeated_string
print(repeat(string, repeats, repeated_string))

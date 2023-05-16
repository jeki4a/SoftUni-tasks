string_1 = input()
string_2 = input()

last_printed_string = ""

for i in range(len(string_1)):
    if string_1[i] != string_2[i]:
        left_part = string_2[: i + 1]
        right_part = string_1[i + 1:]
        new_string = left_part + right_part
        if new_string == last_printed_string:
            continue
        print(new_string)
        last_printed_string = new_string

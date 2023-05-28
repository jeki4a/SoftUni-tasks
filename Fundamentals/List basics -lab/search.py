n = int(input())
keyword = input()

list = []

for _ in range(n):
    words = input()
    list.append(words)

print(list)

filtered_list = []

for i in list:
    if keyword in i:
        filtered_list.append(i)

print(filtered_list)

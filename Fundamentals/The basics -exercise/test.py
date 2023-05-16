str1 = input().strip()
str2 = input().strip()

for i in range(len(str1)):
    if str1[i] != str2[i]:
        str1 = str1[:i] + str2[i] + str1[i+1:]
        if str1 not in [str2[:j+1] for j in range(i)]:
            print(str1)

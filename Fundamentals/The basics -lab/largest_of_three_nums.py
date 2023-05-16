num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

num = 0

if num_1 > num_2:
    num = num_1
elif num_2 > num_1:
    num = num_2

if num_3 > num:
    print(num_3)
else:
    print(num)

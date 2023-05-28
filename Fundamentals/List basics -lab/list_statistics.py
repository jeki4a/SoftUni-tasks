n = int(input())

negative_list = []
positive_list = []

sum_negative = 0

for i in range(n):
    numbers = int(input())
    if numbers < 0:
        negative_list.append(numbers)
        sum_negative += numbers
    else:
        positive_list.append(numbers)

positive_count = len(positive_list)

print(f"{positive_list}\n{negative_list}\nCount of positives: {positive_count}\nSum of negatives: {sum_negative}")

string_int = input().split(", ")
amount_of_beggars = int(input())

money = []

for digits in string_int:
    money.append(int(digits))
final_money = []
start_index = 0
while start_index < amount_of_beggars:
    sum_beggar = 0
    for i in range(start_index, len(money), amount_of_beggars):
        sum_beggar += money[i]
    final_money.append(sum_beggar)
    start_index += 1

print(final_money)

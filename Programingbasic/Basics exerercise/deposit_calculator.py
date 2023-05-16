deposit_sum = float(input())
months = int(input())
yearly_interest_rate = float(input()) / 100
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
sum = deposit_sum + months * ((deposit_sum * yearly_interest_rate) / 12)

print(sum)
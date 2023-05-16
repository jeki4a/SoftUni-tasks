yearly_tax = int(input())

sneakers = yearly_tax - (yearly_tax * (40 / 100))
outfit = sneakers - (sneakers * (20 / 100))
ball = (1/4) * outfit
accessories = (1/5) * ball

total_price = yearly_tax + sneakers + outfit + ball + accessories

print(total_price)

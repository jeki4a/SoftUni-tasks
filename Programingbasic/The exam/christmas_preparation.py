rolls_paper = int(input())
rolls_fabric = int(input())
glue_liters = float(input())
discount = int(input()) / 100

paper_price = rolls_paper * 5.80
fabric_price = rolls_fabric * 7.20
glue_price = glue_liters * 1.20


price = paper_price + fabric_price + glue_price
final_price = price - (price * discount)

print(f"{final_price:.3f}")
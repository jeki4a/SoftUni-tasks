pack_of_pens = int(input())
pack_of_markers = int(input())
l_of_detergent = int(input())
percent_off = int(input()) / 100

price = (pack_of_pens * 5.8) + (pack_of_markers * 7.2) + (l_of_detergent * 1.2)
discount = price * percent_off
final_price = price - discount

print(final_price)

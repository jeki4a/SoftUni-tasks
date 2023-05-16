tshirt_price = float(input())
ball_price = float(input())

shorts_price = 0.75 * tshirt_price
socks_price = 0.2 * shorts_price
buttons_price = 2 * (tshirt_price + shorts_price)

total_price = tshirt_price + shorts_price + socks_price + buttons_price

total_price *= 0.85

if total_price >= ball_price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {ball_price - total_price:.2f} lv. more.")

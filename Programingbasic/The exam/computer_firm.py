n = int(input())

sales = 0
total_rating = 0

for i in range(n):
    computer = int(input())

    rating = computer % 10
    possible_sales = computer // 10

    if rating == 2:
        sales_made = 0
    elif rating == 3:
        sales_made = 0.5 * possible_sales
    elif rating == 4:
        sales_made = 0.7 * possible_sales
    elif rating == 5:
        sales_made = 0.85 * possible_sales
    elif rating == 6:
        sales_made = possible_sales

    sales += sales_made
    total_rating += rating

average_rating = total_rating / n

print(f"{sales:.2f}")
print(f"{average_rating:.2f}")

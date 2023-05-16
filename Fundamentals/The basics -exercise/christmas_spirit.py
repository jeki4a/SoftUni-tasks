quantity_decorations = int(input())
days_left = int(input())

cost = 0
spirit = 0

ornament_set_price = 2
ornament_set_spirit = 5

tree_skirt_price = 5
tree_skirt_spirit = 3

tree_garland_price = 3
tree_garland_spirit = 10

tree_lights_price = 15
tree_lights_spirit = 17

decorations_bought = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_decorations += 2

    if day % 2 == 0:
        cost += quantity_decorations * ornament_set_price
        spirit += ornament_set_spirit

    if day % 3 == 0:
        cost += quantity_decorations * (tree_skirt_price + tree_garland_price)
        spirit += tree_skirt_spirit + tree_garland_spirit

    if day % 5 == 0:
        cost += quantity_decorations * tree_lights_price
        spirit += tree_lights_spirit

        if day % 3 == 0:
            spirit += 30

    if day % 10 == 0:
        spirit -= 20
        cost += tree_skirt_price + tree_garland_price + tree_lights_price

    if day == days_left and day % 10 == 0:
        spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")

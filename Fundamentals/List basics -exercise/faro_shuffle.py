cards = input().split()
count = int(input())

half_size = len(cards) // 2

for shuffle in range(count):
    final_deck = []

    left_part = cards[:half_size]
    right_part = cards[half_size:]

    for i in range(half_size):
        final_deck.append(left_part[i])
        final_deck.append(right_part[i])

    if len(cards) % 2 != 0:
        final_deck.append(right_part[-1])

    cards = final_deck

print(final_deck)

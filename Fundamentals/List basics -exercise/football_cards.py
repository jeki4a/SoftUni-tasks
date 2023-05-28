A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

cards = input().split()

match_terminated = False

for player in cards:
    if player in A:
        A.remove(player)
    elif player in B:
        B.remove(player)
    if len(A) <= 6 or len(B) <= 6:
        match_terminated = True
        break

print(f"Team A - {len(A)}; Team B - {len(B)}.")

if match_terminated:
    print("Game was terminated")

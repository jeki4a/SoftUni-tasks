lenght = int(input())
wide = int(input())
height = int(input())
percent = float(input()) / 100

volume = lenght * wide * height
volume_liters = volume * 0.001
liter_needed = volume_liters * (1 - percent)

print(liter_needed)

month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month in ['May', 'October']:
    studio_price = 50 * nights
    apartment_price = 65 * nights
    if nights > 14:
        studio_price *= 0.7
        apartment_price *= 0.9
    elif nights > 7:
        studio_price *= 0.95
elif month in ['June', 'September']:
    studio_price = 75.2 * nights
    apartment_price = 68.7 * nights
    if nights > 14:
        studio_price *= 0.8
        apartment_price *= 0.9
else:
    studio_price = 76 * nights
    apartment_price = 77 * nights
    if nights > 14:
        apartment_price *= 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")

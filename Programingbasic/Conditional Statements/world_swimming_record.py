record = float(input())
distance = float(input())
time_per_m = float(input())

time = distance * time_per_m
slowed_down = (distance // 15) * 12.5
total_time = time + slowed_down

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    missing_seconds = total_time - record
    print(f"No, he failed! He was {missing_seconds:.2f} seconds slower.")

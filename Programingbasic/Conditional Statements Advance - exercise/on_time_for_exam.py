exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrival_time = arrival_hour * 60 + arrival_min

diff = arrival_time - exam_time

if diff > 0:
    print("Late")
elif diff >= -30:
    print("On time")
else:
    print("Early")

abs_diff = abs(diff)

hours = abs_diff // 60
minutes = abs_diff % 60

if diff > 0 and hours == 0:
    print(f"{minutes} minutes after the start")
elif diff > 0:
    print(f"{hours}:{minutes:02d} hours after the start")
elif diff < 0 and hours == 0:
    print(f"{minutes} minutes before the start")
else:
    print(f"{hours}:{minutes:02d} hours before the start")

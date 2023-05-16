from math import ceil

series_name = str(input())
episode_duration = int(input())
rest_duration = int(input())

time_for_lunch = 1/8 * rest_duration
time_for_chill = 1/4 * rest_duration
time_activities = rest_duration - time_for_lunch - time_for_chill
time_remaining = rest_duration - time_for_lunch - time_for_chill - episode_duration

if time_remaining >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_remaining)} minutes free time.")
else:
    time_necessary = (ceil(episode_duration - time_activities))
    print(f"You don't have enough time to watch {series_name}, you need {time_necessary} more minutes.")

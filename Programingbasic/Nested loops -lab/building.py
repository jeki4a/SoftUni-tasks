# read the number of floors and rooms per floor from the user
num_floors = int(input())
num_rooms = int(input())

# iterate over each floor in reverse order
for floor in range(num_floors, 0, -1):
    # determine the type of rooms on this floor
    if floor % 2 == 0:
        room_type = "O"
    else:
        if floor == num_floors:
            room_type = "L"
        else:
            room_type = "A"

    # iterate over each room on this floor in reverse order
    room_list = []
    for room in range(num_rooms - 1, -1, -1):
        # build the room number using the room type and floor number
        room_num = room_type + str(floor) + str(room)
        # add the room number to the list
        room_list.append(room_num)

    # join the room numbers and print them
    print(" ".join(room_list))

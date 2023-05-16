destinations = []
while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    savings = []
    while sum(savings) < budget:
        savings.append(float(input()))
    destinations.append(destination)

for i, destination in enumerate(destinations):
    print(f"Going to {destination}!")

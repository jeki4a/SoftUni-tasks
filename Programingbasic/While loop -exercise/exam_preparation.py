unsatisfactory_grades = int(input())
task_count = 0
score_sum = 0
unsatisfactory_count = 0
last_task = ""

while True:
    task_name = input()
    if task_name == "Enough":
        break
    score = int(input())
    task_count += 1
    score_sum += score
    last_task = task_name
    if score <= 4:
        unsatisfactory_count += 1
        if unsatisfactory_count == unsatisfactory_grades:
            print(f"You need a break, {unsatisfactory_grades} poor grades.")
            exit()

average_score = score_sum / task_count
print(f"Average score: {average_score:.2f}")
print(f"Number of problems: {task_count}")
print(f"Last problem: {last_task}")

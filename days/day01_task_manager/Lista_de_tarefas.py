# FIRST STEP
print("---")
print("Welcome to the task manager!")
tasks = []
print("Current tasks:")
print(tasks)
print("---")

# SECOND STEP
tasks = ["Study Python", "Train jiu-jitsu", "Buy groceries"]
print("Current tasks:")
for task in tasks:
    print("-", task)

tasks = ["Study Python", "Train jiu-jitsu", "Buy groceries"]
new_task = input("Enter a new task: ")
tasks.append(new_task)

print("\nUpdated tasks:")
for task in tasks:
    print("-", task)
print("---")

# THIRD STEP
print("\nCurrent tasks:")
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")
task_index = int(
    input("\nEnter the number of the task you want to remove: ")) - 1
if 0 <= task_index < len(tasks):
    tasks.pop(task_index)
    print("\nTask successfully removed!")
else:
    print("\nInvalid number!")

print("\nFinal task list:")
for task in tasks:
    print("-", task)
print("---")

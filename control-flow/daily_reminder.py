#Prompt for a Single Task
task = input("Enter your task ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

#Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        reminder = f"The task '{task}' is of high priority."
    case 'medium':
        reminder = f"The task '{task}' is of medium priority."
    case 'low':
        reminder = f"The task '{task}' is of low priority."
    case _:
        reminder = f"The task '{task}' has an invalid priority. Please enter 'high', 'medium', or 'low'."

# Modify the reminder if the task is time-sensitive
if time_bound == 'yes':
    reminder += f"'{task}' is a high priority task that requires immediate attention today!"
elif time_bound == 'no':
    reminder += f"'{task}' is a low priority task. Consider completing it when you have free time."
else:
    reminder += " Please specify 'yes' or 'no' for time sensitivity."

# Print the final reminder
print(reminder)
        
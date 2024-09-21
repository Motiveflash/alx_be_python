# Prompt for a Single Task
task = input("Enter your task: ")

# Prompt for priority
priority = input("Priority (high/medium/low): ").lower()
while priority not in ['high', 'medium', 'low']:
    priority = input("Priority must be (high/medium/low): ").lower()

# Prompt for time bound     
time_bound = input("Is it time-bound? (yes/no): ").lower()
while time_bound not in ['yes', 'no']:  
    time_bound = input("Is it time-bound? Enter (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case _ if priority == "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high-priority task, but not time-bound. Complete it as soon as possible.")
            
    case _ if priority == "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium-priority task that should be completed soon, preferably today.")
        else:
            print(f"Note: '{task}' is a medium-priority task. Try to complete it in a timely manner.")
            
    case _ if priority == "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low-priority task, but it is time-sensitive and should be done today.")
        else:
            print(f"Note: '{task}' is a low-priority task. You can complete it when you have free time.")
            
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")

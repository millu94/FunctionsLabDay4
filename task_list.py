tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks
# 2. Print a list of completed tasks
# 3. Print a list of all task descriptions
# 4. Print a list of tasks where time_taken is at least a given time
# 5. Print any task with a given description
# ### Extension
# 6. Given a description update that task to mark it as complete.
# 7. Add a task to the list
# ### Further Extensions
# 8. Use a while loop to display the following menu and allow the use to enter an option.


# 1
def uncompleted_tasks(list):
    jobs = []
    for task in tasks:
        if task["completed"] == False:
            jobs.append(task["description"])
    return jobs
print(uncompleted_tasks(tasks))

# 2
def completed_tasks(list):
    jobs = []
    for task in tasks:
        if task["completed"] == True:
            jobs.append(task["description"])
    return jobs
print(completed_tasks(tasks))

# 3
def all_tasks(list):
    jobs = []
    for task in tasks:
        jobs.append(task["description"])
    return jobs
print(all_tasks(tasks))

# 4
def time_taken_over_20(list):
    time = []
    for task in tasks:
        if task["time_taken"] >= 20:
            time.append(task["description"])
    return time
print(time_taken_over_20(tasks))

# 5
def print_task(list, job):
    for task in tasks:
        if task["description"] == job:
            return job
print(print_task(tasks, "Clean Windows"))

# 6
def update_task(list, job):
    update = {"completed":True}
    for task in tasks:
        if task["description"] == job:
            return task.update(update)
print(update_task(tasks, "Clean Windows"))

# 7
# def str2bool(x):
#     return x.lower() in ("yes")

def add_to_list():
    new_description = input('Please enter a task you must complete ')
    bool_new_completed = False
    new_completed = (input('Have you already completed this task? Yes or No? '))
    if new_completed == 'Yes':
        bool_new_completed = True
    new_time_taken = input('How long does it take you to do this in minutes? ')
    new_dict_entry = {"description": new_description, "completed": new_completed, "time_taken": new_time_taken}
    tasks.append(new_dict_entry)

add_to_list()
print(tasks)

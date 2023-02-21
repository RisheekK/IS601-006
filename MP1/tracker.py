from datetime import datetime
import json
import os
#from typing import Self

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # update lastActivity with the current datetime value
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    # make sure save() is still called last in this function
    task["lastActivity"] = f'{datetime.now()}'
    task["name"] = name
    task["description"] = description

    format = ("%m/%d/%y %H:%M:%S","%Y-%m-%d %H:%M:%S")
        
    try:
        task["due"] = f'{str_to_datetime(due)}'
        fields_not_available = []
        for i in task:
            if task[i] is None or task[i] == '':
                fields_not_available.append(i) 

        if not fields_not_available:
            tasks.append(task)
            output = f'\nThe new task was added successfully\n\nname: {task["name"]}\n\
Description: {task["description"]}\nDue: {task["due"]}\n\
Lastactivity: {task["lastActivity"]}\nDone:{task["done"]}'
            print(output)
        else:
            output = f'The new task has not been added due to misssing fields {fields_not_available}'
            print(output)

    except:
        print(f"The due date does not match the required format : {format}\n No tasks were added")

    save()

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    ''' rr284 feb 19
        used Try and Except to handle the format error of 'due'. 
        If the format does not match then the Print statement in the except will run.

        i have used for loop to check if a field is missing a value and store in fields_not_available 
        then if the fields_not_available is empty success message is shown 
        if its not "not added" message is shown along with the missing fields
    '''

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)

    
    if index < 0:
        print(f'Provided index number {index + 1} is zero or negative')
    elif index >= len(tasks):
        print(f'Provided index number {index + 1} is greater than the available number of tasks {len(tasks)}')
    else:
        task = tasks[index]
        n = task["name"]
        d = task["description"]
        t = task["due"]

        name = input(f"What's the name of this task? ({n})) \n").strip()
        desc = input(f"What's a brief descriptions of this task? ({d}) \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) ({t}) \n").strip()
        update_task(index, name=name, description=desc, due=due)

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        if the index is out of bounds an appropriate message is given.
        when an available index is given we proceed with the code where the current values for 
        the fields are displayed next to the question
    '''

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    
    task = tasks[index]
    fields_changed = []

    if name != '' and name != task["name"]:
        task["name"] = name
        fields_changed.append("name")
    if description != '' and description != task["description"]:
        task["description"] = description
        fields_changed.append("description")
    if due != '' and due != task["due"]:
        try:
            task["due"] = f'{str_to_datetime(due)}'
            fields_changed.append("Due")
        except:
            print("The value provided for Due does not match the correct format.\nDue date has not been changed.")

    task["lastActivity"] = datetime.now()
    tasks[index] = task

    if len(fields_changed) > 0:
        print(f"Success. Fields that were changed: {fields_changed}")
    else:
        print("The task was not updated")

    save()

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        storing the chosen task in 'task'.
        if the given value is null or the same as the existing value then the field is not updated.
        once a field is updated the field name is stored in 'fields_changed' lsit.
        when 'fields_changed' is empty which would imply that no changes were made therefore th task is updated.
        else the the fields that were updated will be displayed.
    '''
    

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function

    if index < 0:
        print(f'Provided index number {index + 1} is 0 or negative\n')
    elif index >= len(tasks):
        print(f'Provided index number {index + 1} is greater than the available number of tasks {len(tasks)}\n')
    else:
        task = tasks[index]
        name = task["name"]
        if task["done"] == False:
            task["done"] = datetime.now()
            print(f"the task no.{index+1} {name} has been marked done")
        else:
            print(f"The {name} task is already completed\n")
            
    save()
    
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        index is first checked for out of bounds.
        "done" field is checked if it False. in this case the task is not done.
        therefore the current time is stored.
        if it is not false then the value was changed therefore we can assume that
        the task was already done.
    '''
    

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    if index < 0:
        print(f'Provided index number {index + 1} is 0 or negative\n')
    elif index >= len(tasks):
        print(f'Provided index number {index + 1} is greater than the available number of tasks {len(tasks)}\n')
    else:
        task = {}
        task = tasks[index]
        print(f"""
            [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
            Description: {task['description']} \n 
            Last Activity: {task['lastActivity']} \n
            Due: {task['due']}\n
            Completed: {task['done'] if task['done'] else '-'} \n
            """.replace('  ', ' '))
        
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        Index is checked for out of bounds.
        if it does not match then an appropriate message is displayed.
    '''

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function

    if index < 0:
        print(f'Provided index number {index + 1} is zero or negative. No task(s) were deleted\n')
    elif index >= len(tasks):
        print(f'Provided index number {index + 1} is greater than the available number of tasks {len(tasks)}. No task(s) were deleted\n')
    else:
        name = tasks[index]['name']
        del tasks[index]
        print(f"The task {index+1} - {name} is successfully deleted")
        
    save()

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        Checking for out of bounds. 
        if index lies outside appropriate messages are displayed
        when a valid index is provided the task is deleted from the list and a success message is displayed.
    '''

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    
    _tasks = []
    for i in range(len(tasks)):
        if tasks[i]['done'] == False:
            _tasks.append(tasks[i])
    if not _tasks:
        print("There are no tasks that are incomplete")
    else:
        list_tasks(_tasks)

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        for loop is used to check value for Key "done".
        if its false then the task is not completed and the task is appended to the '_tasks' list.
        if the list is empty it implies that there are no tasks that are incomplete.
        if the list is not empty then the _tasks list is given in the list_tasks funtion.
    '''

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    
    _tasks = []
    now = datetime.now()
    x = str(now).split('.')[0]

    for i in range(len(tasks)):
        conv = str_to_datetime(tasks[i]['due'])
        if conv < str_to_datetime(x):
            _tasks.append(tasks[i])

    if not _tasks:
        print("There are no tasks that are overdue")
    else:
        print("The task that are overdue:\n")
        list_tasks(_tasks)

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        two variables now and x are used to obtain the current date and time in the required format.
        for loop is used to run through each task in 'tasks' list.
        conv is the due date and str_to_datetime(x) is the current day and time.
        these 2 can be compared since both are in datetime datatype.
        if the due is less than our current date and time then its appended in the _tasks list.
        if the list is not empty then the _tasks list is given in the list_tasks funtion.
        if it is empty it implies that not task is overdue
    '''

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)

    if index < 0:
        print(f'Provided index number {index + 1} is zero or negative\n')
    elif index >= len(tasks):
        print(f'Provided index number {index + 1} is greater than the available number of tasks {len(tasks)}\n')
    else:
        now = datetime.now()
        time = str_to_datetime(tasks[index]['due']) - now
        timediff = abs(time)
        timediffsecs = timediff.days * 24 * 3600 + time.seconds

        mins, secs = divmod(timediffsecs,60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        
        if time.days > 0:
            print(f"Time left for task - {tasks[index]['name']}: {days} days, {hours} hours, {mins} minutes, {secs} seconds.")
        else:
            print(f"Overdue for task - {tasks[index]['name']}: {days} days, {hours} hours, {mins} minutes, {secs} seconds.")

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    '''rr284 feb 19
        first we check if the index is out of bounds and if so approptiate messages are displayed.
        in now the current time is stored
        in 'time' the the difference between due and the present us stored
        timediff is the absolute value of time since days and time can only be positive.
        then we convert the time difference to seconds and store it in timediffsecs

        later we use divmod method to figure out the seconds, minutes, hours and days.
        It takes two numbers as arguments and returns their quotient and remainder in a tuple.
        in this code"mins, secs = divmod(timediffsecs,60)" we save the quotient in mins and the remainder in secs.
        we use similar code to calculate days, hours and minutes.

        when time.days() is greater than zero it means the there still time left until due.
        therefore the output is displayed as time left.
        when time.days() is less than 0 it means the time diff is negative.
        therefore the output is displayed as overdue.

        source: https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-37.php
        the above link has been useed as reference.
    '''

    #source: https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-37.php




# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("\nWhat would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()
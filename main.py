tasks = []
events = []


def space():
    print(" ")


def display_tasks():
    if len(tasks) != 0:
        tasks.sort()
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
            i += 1
    else:
        print("You do not have any task")


def create_task():
    tasks.append(input("The task: "))


def display_events():
    if len(events) != 0:
        events.sort()
        for i in range(len(events)):
            print(f"{i+1}. {events[i]}")
            i += 1
    else:
        print("You do not have any event")


def create_event():
    events.append(input("The event: "))


def clear_tasks():
    while len(tasks) != 0:
        tasks.pop()


def clear_events():
    while len(events) != 0:
        events.pop()


def delete_a_task():
    tasks.pop(
        int(
            input(
                "The number of the task you want to delete in the tasks list: ")) - 1)


def delete_an_event():
    events.pop(
        int(
            input(
                "The number of the event you want to delete in the list of the events : ")) - 1)


commands = ["Looking at tasks: display tasks",
            "Creating task: create task",
            "Looking at calendar: display tasks",
            "Create event: create event",
            "Delete a task: delete a task",
            "Delete an event: delete an event",
            "Clear all tasks: clear tasks",
            "Clear all events: clear events"
            "Closing app: stop"]


print("User guide")
print("Commands:")
for i in range(len(commands)):
    print(commands[i])
    i += 1
space()
print("When entering tasks or events, we recommend to enter them like this:")
print("Deadline(start time in events)/Name of task or event/Finish time in events")
print("---------------------------------------")

order = input("To start, type start: ")

while order != "stop":
    order = input("Write your command here: ")
    if order == "display tasks":
        display_tasks()
        space()
    elif order == "create task":
        create_task()
        space()
    elif order == "display events":
        display_events()
        space()
    elif order == "create event":
        create_event()
        space()
    elif order == "clear tasks":
        clear_tasks()
    elif order == "clear events":
        clear_events()
    elif order == "delete a task":
        delete_a_task()
        space()
    elif order == "delete an event":
        delete_an_event()
        space()

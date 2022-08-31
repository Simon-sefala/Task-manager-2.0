# =====importing libraries===========
from datetime import date, datetime
from os import path

from tomlkit import value


# Define a function for registering a user
def reg_user():
    # Request input of a new username
    # Request input of a new password
    # Request input of password confirmation.
    # Check if the new password and confirmed password are the same.
    # If they are the same, add them to the user.txt file,
    # Otherwise you present a relevant message
    new_username = input("Enter a username: ")
    new_password = input("Enter a password: ")
    confirm_password = input("Confirm password: ")
    if new_password == confirm_password:
        with open('user.txt', 'r') as f:
            for line in f:
                line = line.replace('\n', '').split(", ")
                if line[0] != new_username:
                    with open("user.txt","a") as file:
                        file.write('\n' + new_username + ', ' + new_password)
                else:
                    print("User already exists")
                    new_username = input("Enter a username: ")
                    new_password = input("Enter a password: ")
                    confirm_password = input("Confirm password: ")
    else:
        print("Your password does not match")
    
# Define a function for adding a task
def add_task():
    # Prompt a user for the following: 
    # A username of the person whom the task is assigned to,
    # A title of a task,
    # A description of the task and 
    # the due date of the task.
    # Then get the current date.
    # Add the data to the file task.txt and
    # You must remember to include the 'No' to indicate if the task is complete.'''
    username_tasked = input("Enter the username whom the task is assigned to: ")
    Task_title = input("Enter the title of the task: ")
    Task_description = input("Enter the description of the task: ")
    Due_date = input("Enter the due date: ")
    Today = date.today()
    Today = str(Today.strftime("%d %B %Y"))
    Task_complete = "No"
    with open('tasks.txt', 'a') as f:
        f.write('\n' + username_tasked + ', ' + Task_title + ', ' + Task_description + ', ' + Today + ', ' + Due_date + ', ' + Task_complete)

# Define a function for viewing all tasks
def view_all():
    # Read a line from the file task.txt.
    # Then print the results in the format shown in the Output 2 in L1T19 pdf
    with open('tasks.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(", ")
            print(f"\nTask: {line[1]} \nAssigned to: {line[0]} \nDate assigned: {line[4]} \nDue date: {line[3]} \nTask complete?: {line[5]} \nTask description: {line[2]}\n")

# Define a function for viewing a user's tasks
def view_mine():
    task_numb = 1
    tasks = {}
    # Read a line from the file user.txt
    # Split the line where there is comma and space.
    # Check if the username of the person logged in is the same as the username you have read from the file.
    # If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
    with open('tasks.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(", ")
            tasks[task_numb] = line
            if line[0] == username:
                print(f"Task number {task_numb}\nTask: {line[1]} \nAssigned to: {line[0]} \nDate assigned: {line[4]} \nDue date: {line[3]} \nTask complete?: {line[5]} \nTask description: {line[2]}\n")
            task_numb += 1
        
    task_choice = int(input("Select either a specific task by entering a number or input -1 to return to the main menu: "))
    
    mark_edit_task = input('''Select one of the following Options below:
mc - Mark task as complete
ed - edit task
: ''').lower()
    if mark_edit_task == 'mc':
        tasks[task_choice][5] = 'Yes'
    else:
        if line[5] == 'No':
            tasks[task_choice][0] = input("Edit username: ")
            tasks[task_choice][3] = input("Edit due date: ")
        else:
            print("You can't edit completed tasks")
    with open('tasks.txt', 'w') as f:
        for task in tasks.values():
            task = (", ").join(task)
            f.write(f'\n{task}')
           
# Define a function to generate task_overview
def task_overview():
    no_of_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    uncompleted_overdue = 0
    todays_date = date.today()
    
    with open('tasks.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(", ")
            no_of_tasks += 1
            due_date = datetime.strptime(line[-2], "%d %b %Y").date()
            if line[-1] == 'Yes':
                completed_tasks += 1
            elif line[-1] == 'No':
                uncompleted_tasks += 1
                if todays_date > due_date:
                    uncompleted_overdue += 1
            

    incomplete_percentage = round(((uncompleted_tasks / no_of_tasks) * 100), 2)
    overdue_percentage = round(((uncompleted_overdue / no_of_tasks) * 100), 2)
    with open('task_overview.txt', 'w') as f:
        f.write(f'The total number of tasks: {no_of_tasks} \nThe total number of completed tasks: {completed_tasks} \nThe total number of uncompleted task: {uncompleted_tasks} \nThe total number of tasks that have not been completed and overdue: {uncompleted_overdue} \nThe percentage of tasks that are incomplete: {incomplete_percentage}% \nThe percentage of tasks that are overdue: {overdue_percentage}%')
# Define a function to generate user_overview
def user_overview():
        with open('user.txt', 'r') as user_file:
            user_file_content = user_file.readlines()
            no_users = len(user_file_content)
        with open('tasks.txt', 'r') as task_file:
            task_file_content = task_file.readlines()
            no_of_tasks = len(task_file_content)
        with open('user_overview.txt', 'w') as my_file:
            for line in user_file_content:
                line = line.replace('\n', '').split(", ")
                user = line[0]
                user_total_tasks = 0
                user_completed = 0
                user_uncomplete = 0
                user_uncomp_overdue =0
                
                for line in task_file_content:
                    line = line.replace('\n', '').split(", ")
                    task_user = line[0]
                    if user == task_user:
                        todays_date = datetime.strptime(line[-3], "%d %b %Y").date()
                        due_date = datetime.strptime(line[-2], "%d %b %Y").date()
                        user_total_tasks += 1
                        if line[5] == 'Yes':
                            user_completed += 1
                        elif line[5] == 'No' and todays_date > due_date:
                            user_uncomp_overdue += 1
                        else:
                            user_uncomplete += 1

                
                user_task_percentage = round(((user_total_tasks / no_of_tasks) * 100), 2)
                user_task_comp_percent = round(((user_completed / no_of_tasks) * 100), 2)
                user_task_uncomp_percent = round(((user_uncomplete / no_of_tasks) * 100), 2)
                user_task_uncomp_odue_percent = round(((user_uncomp_overdue / no_of_tasks) * 100), 2)
                
                my_file.write(f'''Total number of users: {no_users}
Total number of tasks: {no_of_tasks}
\nTask user: {user}
Total number of user tasks: {user_total_tasks}
Total number of tasks user completed: {user_completed}
Total number of user uncompleted tasks: {user_uncomplete}
Total number of user uncompleted and overdue tasks: {user_uncomp_overdue}
User total tasks percentage: {user_task_percentage}%
User completed tasks percentage: {user_task_comp_percent}%
User uncompleted tasks percentage: {user_task_uncomp_percent}%
User uncompleted and overdue percentage: {user_task_uncomp_odue_percent}%''')

def display_stats():
    with open('task_overview.txt', 'r') as f:
        file_contents = f.readlines()
        [print(line) for line in file_contents]
    with open('user_overview.txt', 'r') as my_f:
        contents = my_f.readlines()
        [print(line) for line in contents]

# Log in section
user_names = {}
with open('user.txt', 'r') as f:
    for line in f:
        username_f, password_f = line.strip("\n").split(', ')
        user_names[username_f] = password_f

username = input("Enter your username: ")
while  not username in user_names:
    print("Invalid user")
    username = input("Enter your username: ")

password = input("Enter your password: ")
while password != user_names[username]:
    print("Invalid passoword")
    password = input("Enter your password: ")


while True:
    if username == 'admin':
    # Presenting the menu to the user and 
    # Making sure that the user input is converted to lower case.
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate reports
ds - Display stats
e - Exit
: ''').lower()
        if menu == 'r':
            reg_user()   
        elif menu == 'a':
            add_task()   
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'gr':
            task_overview()
            user_overview()         
        elif menu == 'ds':
            display_stats()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
        if menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

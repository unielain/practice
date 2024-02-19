import mysql.connector

# A small program to outline the time management application
greeting = "Welcome"

# Connection to database
connection = mysql.connector.connect(
    host = 'localhost',
    port=3306,
    database='time_management',
    user='root',
    password='database',
    autocommit=True
)

while True:
    print("***************")
    print("* SIGN IN (A) *")
    print("* LOG IN (B)  *")
    print("***************")
    log_choice = input("What do you want to do? ")
    name = input("Give your username: ")
    password = input("Give your password: ")
    
    #if sing in:
    if log_choice == "A":
        sql = 'INSERT INTO users (username, password, level, experience)'
        sql += 'VALUES ('+username+','+password+',0, 0);'
        cursor_add_user = connection.cursor()
        cursor_add_user(sql)
        print("Account created")
        response = True

    #if log in:    
    if log_choice == "B":
        sql = 'select name from users'
        sql += 'WHERE username"' + name + '" AND password "' + password + '"'
        experience = 1
        level_limit = 10
        cursor_find_user = connection.cursor()
        cursor_find_user(sql)
        result = cursor_find_user.fetchall()
        response = False
    
        if cursor_find_user.rowcount > 0:
            response = True

    # Checking that the credentials are given
    if response == False:
        print("Error: cannot find the name or password")
        name = input("Give your username: ")
        password = input("Give your password: ")
    
    # If the credentials are right, the program starts
    else:
        print(greeting + name)
        print("Today:")

        # The program will fetch the tasks from the database
        
        date = 19
        month = 2
        year = 2024
        print(date)
        print(month)
        print(year)
        
        print("New task (A)")
        print("Edit tasks (B)")
        print("Today's tasks (C)")
        print("Complete task (D)")

        choice = input("What do you want to do? ")
        add_task = False
        edit_task = False
        todays_tasks = False
        complete_task = False

        if choice == "A":
            add_task = True
        elif choice == "B":
             edit_task = True
        elif choice == "C":
            todays_tasks = True
        else:
            complete_task = True
        
        if add_task == True:
            new_task = input("What do you want to accomplish: ")
            tasks.append(new_task)
            print(tasks)
        
        if edit_task == True:
            print(tasks)
            task_to_edit = input("Which tasks you want to edit? ")
            task_index = tasks.index(task_to_edit)
            edited_task = input("Edit: ")
            tasks[task_index] = edited_task
            print(tasks)

        if todays_tasks == True:
            print(tasks)
        
        if complete_task == True:
            task_to_complete = input("Which tasks do you want to complete? ")
            task_index = tasks.index(task_to_complete)
            tasks.pop(task_index)
            print("Task completed!")
            experience += 1
            print(tasks)
            if experience > level_limit:
                print("Level Up!")


        print("Alarm!")
        
        
        
 

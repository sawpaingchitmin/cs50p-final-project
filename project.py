from datetime import datetime
import json
import re

FILE_PATH = "tasks.txt"
    
def main():     
    """ Main menu loop for task manager. """
    while True:
        tasks = load_tasks()
        print("\nDaily Task Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_tasks(tasks)
        
        elif choice == "2":
            add_task(tasks)
        
        elif choice == "3":
            edit_task(tasks)

        elif choice == "4":
            delete_task(tasks)            
                
        elif choice == "5":
            search_tasks(tasks)

        elif choice == "6":
            print("Exiting Daily Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def load_tasks():
    """ Load tasks from the file. Return an empty dictionary if file is missing or corrupted. """
    try:
        with open(FILE_PATH, "r") as task_file:
            return json.load(task_file)
    except FileNotFoundError:
        print("File does not exist yet. Add a task to create the file.")
        return {}
    except json.JSONDecodeError:
        print(f"⚠️ Warning: {FILE_PATH} is corrupted. Adding a new task will overwrite existing data.")
        return {}


def save_tasks(tasks):
    """ Save tasks to file, removing empty task lists. """
    tasks = {date: task_list for date, task_list in tasks.items() if task_list}
    with open(FILE_PATH, "w") as task_file:
        json.dump(tasks, task_file, indent=4)


def display_tasks(tasks):
    """ Show all tasks or tasks for a specific date. """
    if not tasks:
        print("No tasks found!")
        return
    
    print("\nChoose an option:")
    print("1. View All Tasks")
    print("2. View Tasks by Date")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        # Show all tasks with their dates and numbers
        for date, task_list in tasks.items():
            print(f"\n{date}")
            for i, task in enumerate(task_list, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        date = input("Enter the date(e.g., 20 February 2025): ").strip()
        # If the date has tasks, show the task list with numbers
        if date in tasks and tasks[date]:
            print(f"\nTasks on {date}:")
            for i, task in enumerate(tasks[date], 1):
                print(f"{i}. {task}")
        else:
            print(f"No tasks found for {date}.")

    else:
        print("Invalid choice. Please try again.") 


def add_task(tasks):
    """ Add a new task for today or a future date. """
    input_date = input("Enter the date (Current or Future Date. Format: Day Month Year. e.g., 20 February 2025): ").strip()
    try:
        # Convert the input into a date object
        task_date = datetime.strptime(input_date, "%d %B %Y").date()
        today_date = datetime.today().date()

        # Check if the entered date is in the future or today
        if task_date < today_date:
            print("Date cannot be a past date.")
            return

        task = input("Enter the task: ").strip()
        if not task:
            print("Task cannot be empty.")
            return      

        # Convert date to string and add task to the list for that date
        date_key = task_date.strftime("%d %B %Y")
        if date_key not in tasks:
            tasks[date_key] = []
        tasks[date_key].append(task)

        tasks = dict(sorted(tasks.items(), key=lambda x: datetime.strptime(x[0], "%d %B %Y")))

        # Save tasks back to the file
        save_tasks(tasks)
        print(f"Task added to {date_key}.")
    except ValueError:
        print("Invalid date format.")


def edit_task(tasks):
    """ Edit an existing task. """
    if not tasks:
        print("No tasks to edit!")
        return 
    
    date = input("Enter the date (e.g., 20 February 2025): ").strip()

    if date in tasks:
        print(f"\nTasks on {date}: ")
        for i, task in enumerate(tasks[date], 1):
            print(f"{i}. {task}")

        try: 
            task_number = int(input("Enter the task number to edit: "))
            # Check if the task number is valid  
            if 1 <= task_number <= len(tasks[date]):
                # Ask for a new task and update it if not empty  
                new_task = input("Enter the updated task: ").strip()
                if new_task:
                    tasks[date][task_number - 1] = new_task
                    print(f"Task {task_number} has been updated to: {new_task}")
                    
                    # Save the changes to the file  
                    with open(FILE_PATH, "w") as task_file:
                        json.dump(tasks, task_file, indent=4)     
                else:
                    print("The task cannot be empty. Edit canceled.")
            else:
                print("Invalid task number. Please try again.")       

        except ValueError:
            print("Invalid input. Please enter a valid number.")  

    else:
        print(f"No tasks found for {date}.")


def delete_task(tasks):
    """ Delete all tasks, tasks by date, or a specific task. """
    if not tasks:
        print("No tasks to delete!")
        return
    
    print("\nChoose an option:")
    print("1. Delete All Tasks")
    print("2. Delete Tasks by Date")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
         # Ask user to confirm before deleting all tasks 
        confirm = input('Are you sure? (Type "Yes" to confirm): ').strip()
        if confirm.lower() == "yes":
            # Clear all tasks and save the empty list to the file  
            tasks.clear()
            with open(FILE_PATH, "w") as task_file:
                json.dump(tasks, task_file, indent=4)
            print("All tasks have been deleted.")
        else:
            print("Deletion canceled.")

    elif choice == "2":
         # Ask for a date to delete tasks
        date = input("Enter the date (e.g., 20 February 2025): ").strip()
        if date in tasks:
            print("\nChoose an option:")
            print("1. Delete All Tasks for This Date")
            print("2. Delete by Task Number")
            sub_choice = input("Enter your choice (1 or 2): ").strip()

            if sub_choice == "1":
                # Delete all tasks for the selected date  
                del tasks[date]
                with open(FILE_PATH, "w") as task_file:
                    json.dump(tasks, task_file, indent=4)
                print(f"All tasks for {date} have been deleted.")
            
            elif sub_choice == "2":
                # Show tasks for the selected date  
                print(f"\nTasks on {date}:")
                for i, task in enumerate(tasks[date], 1):
                    print(f"{i}. {task}")
                try:
                     # Ask for a task number to delete  
                    task_number = int(input("Enter the task number to delete: "))
                    if 1 <= task_number <= len(tasks[date]):
                        # Remove the selected task 
                        delete_task = tasks[date].pop(task_number - 1)
                        print(f"Task '{delete_task}' has been deleted.")

                        # If no tasks remain for the date, remove the date 
                        if not tasks[date]:
                            del tasks[date]
                        with open(FILE_PATH, "w") as task_file:
                            json.dump(tasks, task_file, indent=4)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Invalid choice. Please try again.")
        else:
            print(f"No tasks found for {date}.")        
    else:
        print("Invalid choice. Please try again.")


def search_tasks(tasks):
    """ Search tasks by keyword. """
    if not tasks:
        print("No tasks to search!")
        return 
    
    # Ask for a keyword to search  
    keyword = input("Enter keyword to search for: ").strip()
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)

    # Store matching tasks 
    results = {}
    for date, task_list in tasks.items():
        # Find tasks that contain the keyword 
        matching_tasks = [task for task in task_list if pattern.search(task)]
        if matching_tasks:
            results[date] = matching_tasks
    
    # Show search results if found 
    if results:
            print("\nSearch Results:")
            for date, tasks in results.items():
                print(f"- {date}")
                for task in tasks:
                    print(f"- {task}")
    else:
        print("No tasks found matching the keyword.")
    
if __name__ == "__main__":
    main()


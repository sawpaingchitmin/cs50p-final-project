# Project Title: Daily Task Manager
## Video Demo: https://youtu.be/fa-FLFj1ACI
### Description
My project is about managing daily tasks. It has all CRUD operations. You can view, add, edit, delete, and search for tasks. All task data is saved in a tasks.txt file in JSON format.

I chose to make this project because I realized that every day, I need to schedule my tasks. For example, today I have some tasks to do, and tomorrow I have other things. Next week, I may need to go somewhere. But my schedule is only in my mind, not in a notebook or any software. This idea gave me the motivation to create my project.

There are six functions in the Daily Task Manager. I will explain what each function does.

### View Tasks
We can see all tasks in View Tasks. For convenience, there are two options: "View All Tasks" and "View Tasks by Date".

- **View All Tasks:** Shows all tasks saved in the JSON file.
- **View Tasks by Date:** Shows tasks for a specific date. You need to type the date to see the tasks.

### Add Task
You can add a task with a specific date format. But the date cannot be in the past. It must be today or a future date. The task cannot be empty.

### Edit Task
You can edit a task by entering a specific date and a valid task number. If you enter the correct date and task number but do not provide a new task, the edit process will be canceled.

### Delete Task
There are two options in Delete Task: "Delete All Tasks" and "Delete Tasks by Date".

- **Delete All Tasks:** You must type "Yes" to confirm. It is not case-sensitive. If you type "Yes", all task data in tasks.txt will be deleted. If you type anything else, the deletion will be canceled.

- **Delete Tasks by Date:** You must enter a date in the correct format. If tasks are available for that date, you will see two more options:

    - **Delete All Tasks for This Date:** Deletes all tasks for that date immediately without confirmation.
    - **Delete by Task Number:** You must enter a valid task number to delete a specific task.

### Search Tasks
You can search tasks by entering a keyword. The keyword is not case-sensitive. If a matching keyword is found, it will show all tasks that contain the keyword, from every date. 

Example: If you type "ing", it will show all tasks that include "ing", no matter the date.

### Exit
The program always loops back to the main menu after you manage your tasks. If you want to completely exit the program, you can choose "Exit".

### Test Project
In `test_project.py`, I use `pytest` to test my project. I use `monkeypatch` to simulate user input instead of typing manually. I use sample tasks with `monkeypatch` to test different cases. I use `capsys` to capture printed output and check if it is correct.
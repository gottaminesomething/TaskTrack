# TaskTrack

add and display tasks in the terminal as a task manager

## Current Features

-view task
-add task
-persistent tasks

## Requirements

-Python 3

## Project Files

-`tasktrack.py` — add and display tasks in the terminal
-`tasks.txt` — sample tasks to showcase persistent tasks across runs
-`.gitignore` — ignore more sensitive information

## Running the Program

open the project folder in your file manager, right click any empty area inside the folder, and select "open in terminal"

this opens a terminal with the project folder as the current directory

```text
python tasktrack.py
```

## Task Persistence

tasks are saved upon being added, tasks are loaded open running the program and save across different uses of the program in a text file called tasks

## Sample Interaction

```text
TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 2
Enter a new task: test1 of add_task update
Task Added Successfully

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 1

Tasks:
1. complete ica04
2. review github commands
3. update the tasktrack README
4. test2 of save_tasks function
5. test1 of add_task update
```

## Current Limitations

-marking tasks as complete is not a feature in this program
-deleting tasks is not possible in this program
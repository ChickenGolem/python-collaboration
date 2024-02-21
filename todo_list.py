# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:13:51 2024

@author: round
"""
#declares list used to keep track of tasks and bool used to determine whether to run while loop
run = True
tasks_list = []

#function to add new tasks
def Add_new(tasks):
    new_task = input("What is the new task? :")
    tasks.append(new_task)
    return tasks
#function to print all tasks, frequently used inside other functions
def View_tasks(tasks):
    print("\n-----------------\n")
    #runs once for every element in list, except from 1 - element+1 instead of 0 - element
    for i in range(1, len(tasks) + 1):  
        print(f"Task {i}: {tasks[i-1]}")
    return
#deletes a task from the task list
def task_complete(tasks):
    View_tasks(tasks)
    completed = int(input("Which tasks did you complete? :"))
    del tasks[completed - 1]
    return tasks
#deletes a task from the task list, the same as task_complete, except with a different print statement
def delete_tasks(tasks):
    View_tasks(tasks)
    delete = int(input("Which task do you want to delete? :"))
    del tasks[delete - 1]
    return tasks
#runs until user presses 5
while run == True:
    action = int(input("Options:\n1 : add a new task\n2 : view all tasks\n3 : mark a task as complete\n4 : delete a task\n5 : terminate this program\nWhat do you want to do? :"))
    if action == 1:
            Add_new(tasks_list)
    elif action == 2:
        View_tasks(tasks_list)
    elif action == 3:
        task_complete(tasks_list)
    elif action == 4:
        delete_tasks(tasks_list)
    elif action == 5:
        run = False
    #adding a random comment
    #used to help readability of ouput
    print("\n-----------------\n")

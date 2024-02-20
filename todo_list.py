# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:13:51 2024

@author: round
"""
tasks_list = []


def Add_new(tasks):
    new_task = input("What is the new task? :")
    tasks.append(new_task)
    return tasks

def View_tasks(tasks):
    for i in range(1, len(tasks) + 1):  
        print(f"Task {i}: {tasks[i-1]}")
    return

def task_complete(tasks):
    View_tasks(tasks)
    completed = int(input("Which tasks did you complete? :"))
    del tasks[completed - 1]
    return tasks

tasks_list = Add_new(tasks_list)
tasks_list = Add_new(tasks_list)
View_tasks(tasks_list)
tasks_list = task_complete(tasks_list)
View_tasks(tasks_list)


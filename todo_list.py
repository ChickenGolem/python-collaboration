# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:13:51 2024

@author: round
"""
tasks_dic = {}


def Add_new(tasks):
    new_task = input("What is the new task? :")
    dic_length = len(tasks)
    tasks[dic_length + 1] = new_task
    return tasks

def View_tasks(tasks):
    for i in range(1, len(tasks) + 1):  
        print(f"Task {i}: {tasks[i]}")
    return

def task_complete(tasks):
    
    return tasks

tasks_dic = Add_new(tasks_dic)
tasks_dic = Add_new(tasks_dic)
View_tasks(tasks_dic)
View_tasks(tasks_dic)


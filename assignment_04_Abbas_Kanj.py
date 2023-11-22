# FCS CYCLE 49
# Assignment 4
# Due Date: November 25, 10am
# Name: Abbas Kanj
#---------------------------------
class taskManager:
    
    def __init__(self, task_id, description, priority, completed):
        
        self.taskId = task_id
        self.description = description
        self.prio = priority
        self.completed = completed
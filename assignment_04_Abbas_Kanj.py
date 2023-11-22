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
        self.comp = completed
        
    def getTask(self):
        return self.taskId
    
    def getDescrip(self):
        return self.description
    
    def getPrio(self):
        return self.prio
    
    def getComp(self):
        return self.comp
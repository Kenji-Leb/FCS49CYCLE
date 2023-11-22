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
    # Initializing Getters
    def getTask(self):
        return self.taskId
    
    def getDescription(self):
        return self.description
    
    def getPrio(self):
        return self.prio
    
    def getComp(self):
        return self.comp
    # Initializing Setters
    def setTask(self, new_task):
        self.taskId = new_task
        
    def setDescription(self, new_description):
        self.description = new_description
        
    def setPrio(self, new_prio):
        self.prio = new_prio
        
    def setComp(self, new_comp):
        self.comp = new_comp
    
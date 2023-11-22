# FCS CYCLE 49
# Assignment 4
# Due Date: November 25, 10am
# Name: Abbas Kanj
#---------------------------------
class Task:
    
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
#-----------------------------------------------------
class PriorityQueue:

  def __init__(self):
    self.header = None
    self.size = 0

  def displayQueue(self):

    current = self.header
  
    while (current.next != None):
      print(current.info,end="--")
      current = current.next
  
    print(current.info)


  def enqueue(self,info):

    node = Node(info)

    if (self.size == 0):
      self.header = node
      self.size += 1
      print("we successfully added", node.info)

    else:

      if (node.info > self.header.info):

        node.next = self.header
        self.header = node
        self.size += 1

      else:
        current = self.header
        previous = current

        while current != None and current.info >= node.info:
          previous = current
          current = current.next

        previous.next = node
        node.next = current
        self.size += 1
        
  def dequeue(self):
    # Dequeue will remain the same as a regular queue since the logic is still the same.
    if self.size == 0:
      print("Your Queue is Empty! Enqueue first.")
    elif self.size == 1:
      print("We are removing:", self.header.info)
      self.header = None
      self.size -= 1
    else:
      print("We are removing:", self.header.info)
      current = self.header
      self.header = self.header.next
      current.next = None
      self.size -= 1

#-----------------------------------------------------
def main():

    while(True):

        try:
            displaymenu()
            choice = int(input("Please select one of the options: "))
        except:
            print("Invalid Input....")
            continue

        if choice == 1:
            
            task_discription = str(input("Enter the discription of the task: "))
            task_prio = int(input("Enter the priority of the task: "))
            task_completion = bool(input("Enter wether the task is comppleted or not(True/ False): "))
            addNewTask()

        elif choice == 2:
            
            getById

        elif choice == 3:
            
            markPrioComplete

        elif choice == 4:
            
            displayTasks

        elif choice == 5:
           
           displayNotCompTasks

        elif choice == 6:
            
            displayLastTask

        elif choice == 7:
            exit
#-----------------------------------------------------
def displaymenu():
    print("----------------------------")
    print("1- Adding a new task to the task manager\n" + 
          "2- Getting a task from the queue given a task id\n" + 
          "3- Marking the highest priority task as completed and putting it in the task history\n" + 
          "4- Displaying all tasks in order of priority\n" + 
          "5- Displaying only the tasks that are not completed\n" + 
          "6- Displaying the last completed task\n" + 
          "7- Exit\n")
    print("----------------------------")
#-----------------------------------------------------
def addNewTask():
    
    print()

#-----------------------------------------------------
def getById():
    
    print()

#-----------------------------------------------------
def markPrioComplete():
    
    print()

#-----------------------------------------------------
def displayTasks():
    
    print()

#-----------------------------------------------------
def displayNotCompTasks():
    
    print()

#-----------------------------------------------------
def displayLastTask():
    
    print()

#-----------------------------------------------------
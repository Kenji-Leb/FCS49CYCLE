# FCS CYCLE 46
# Midterm Solution
# Due Date: Nov 12th, 11:59 PM
# Name: Abbas kanj
# ---------------------------
import json
import requests 
from bs4 import BeautifulSoup 

#----------------------------------------------------- 
filePath = r'C:\Users\abbas\Desktop\Python-Projects\FCS-49-Cycle\url1.json'

with open(filePath) as json_file:
    dictionaryUrl = json.load(json_file)
print(dictionaryUrl)


#-----------------------------------------------------
def main():
    print("Greeetings User")
    while(True):

        try:
            displaymenu()
            choice = int(input("Please select one of the options: "))
        except:
            print("Invalid Input....")
            continue

        if choice == 1:
            
            title = str(input("Enter the Title of the website: "))
            url = str(input("Enter the Url of the website"))
            openTab(dictionaryUrl, title, url)
            print(dictionaryUrl)
            
        elif choice == 2:
            
            clsdTab = int(input("Enter the index of the tab you want to close: "))
            closeTab(dictionaryUrl, clsdTab)
            print(dictionaryUrl)
            
        elif choice == 3:
            
            switch_index = int(input("Enter the index of the tab you want to display: "))
            switchTab(dictionaryUrl, switch_index)

        elif choice == 4:
            
            
            displayAllTabs()

        elif choice == 5:
            
            
            openNestedTab()

        elif choice == 6:
            
            
            clearAllTabs()

        elif choice == 7:
            
            
            saveTabs()

        elif choice == 8:
            
            
            importTabs()

        elif choice == 9:
            exit

#-----------------------------------------------------
def displaymenu():
    print("----------------------------")
    print("1- Open Tab\n" + "2- Close Tab\n" + "3- Switch Tab\n" + "4- Display All Tabs\n" + "5- Open Nested Tab\n" + "6- Clear All Tabs\n" + "7- Save Tabs\n" + "8- Import Tabs\n" + "9- Exit\n")
    print("----------------------------")
    
#-----------------------------------------------------
def openTab(dict, title, url):
    iter = dict[-1].get("index") + 1
    dictionaryUrl.append({"index": iter, "Title": title, "Url": url})
    
#-----------------------------------------------------
def closeTab(dict, deletedTab):
    
    if deletedTab == 0:
        dict.pop()
        
    else:
        for i in dict:
            if i["index"] == deletedTab:
                dict.remove(i)
                break
            
#-----------------------------------------------------
def switchTab(dict, displayed_index):
    
    if displayed_index == 0:
        
        last_url = dict[-1].get("Url")
        # Making a GET request 
        r = requests.get(last_url) 
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'html.parser') 
        print(soup.prettify()) 
    

#-----------------------------------------------------

def displayAllTabs():
    print()

#-----------------------------------------------------

def openNestedTab():
    print()

#-----------------------------------------------------

def clearAllTabs():
    print()

#-----------------------------------------------------

def saveTabs():
    print()

#-----------------------------------------------------

def importTabs():
    print()

#-----------------------------------------------------
main()
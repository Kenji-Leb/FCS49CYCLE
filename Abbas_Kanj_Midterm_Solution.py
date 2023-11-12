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
            
            
            displayAllTabs(dictionaryUrl)

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
def openTab(dict_items, title, url):
    
    iter = dict_items[-1].get("index") + 1
    dictionaryUrl.append({"index": iter, "Title": title, "Url": url})
    
#-----------------------------------------------------
def closeTab(dict_items, deletedTab):
    
    if deletedTab == 0:
        dict_items.pop()
        
    else:
        for dict in dict_items:
            if dict["index"] == deletedTab:
                dict_items.remove(dict)
                break
            
#-----------------------------------------------------
def switchTab(dict_items, displayed_index):
    
    if displayed_index == 0:
        
        last_url = dict_items[-1].get("Url")
        # Making a GET request 
        r = requests.get(last_url) 
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'html.parser') 
        print(soup.prettify()) 
    
    else:
        
        for dict in dict_items:

            for key, value in dict.items():
                
                if value == displayed_index:
                    
                    selected_url = dict["Url"]
                    print(selected_url)
                
        # Making a GET request 
        r = requests.get(selected_url) 
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'html.parser') 
        
        print(soup.prettify())
                
#-----------------------------------------------------
def displayAllTabs(dict_items):
    
    for dict in dict_items:
        
        title = dict.get("Title")
        print(title)
        if "NestedTabs" in dict.keys():
            nestedTitle = dict["NestedTabs"]["Title"]
            print(f'\t{nestedTitle}')

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
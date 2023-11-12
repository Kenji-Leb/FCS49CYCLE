# FCS CYCLE 46
# Midterm Solution
# Due Date: Nov 12th, 11:59 PM
# Name: Abbas kanj
# ---------------------------
import json
import sys
import requests 
from bs4 import BeautifulSoup 

#----------------------------------------------------- 
filePath = r'C:\Users\abbas\Desktop\Python-Projects\FCS-49-Cycle\url1.json'

dictionaryUrl = []

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
            
            check_index = int(input("Enter the index of the parent tab you want to insert additional tabs: "))
            result = checkIndex(dictionaryUrl,check_index)
            
            if result:
                new_title = str(input("Enter the Title of the nested tab: "))
                new_url = str(input("Enter the Url of the title: "))
                openNestedTab(dictionaryUrl, check_index, new_title, new_url) 
            else:
                print("The index you where searching for is not found")

        elif choice == 6:
            
            dictionaryUrl.clear()
            print("Dictionary Cleared")

        elif choice == 7:
            
            new_file_path = str(input("Enter the file path you want to save the tabs in: "))
            saveTabs(dictionaryUrl, new_file_path)

        elif choice == 8:
            
            import_from = str(input("Enter the file path you want to import from: "))
            defined_import = rf'{import_from}'
            with open(defined_import) as json_file:
                imported_dictionary = json.load(json_file)
            dictionaryUrl = imported_dictionary
            print(dictionaryUrl)
        elif choice == 9:
           sys.exit()

#-----------------------------------------------------
def displaymenu():
    
    print("----------------------------")
    print("1- Open Tab\n" + "2- Close Tab\n" + "3- Switch Tab\n" + "4- Display All Tabs\n" + "5- Open Nested Tab\n" + "6- Clear All Tabs\n" + "7- Save Tabs\n" + "8- Import Tabs\n" + "9- Exit\n")
    print("----------------------------")
    
#-----------------------------------------------------
def openTab(dict_items, title, url):
    
    if not dict_items:
        dict_items.append({"index": 1, "Title": title, "Url": url})
    else:
        iter = dict_items[-1].get("index") + 1
        dict_items.append({"index": iter, "Title": title, "Url": url})
    
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
        
        if "NestedTabs" in dict:
            
            nested_tabs = dict['NestedTabs']
            
            for titles in nested_tabs:
                
                    nested_title = titles.get("Title")
                    print(f'\t{nested_title}')

#-----------------------------------------------------
def openNestedTab(dictionary, chosen_index, new_Title, new_Url):
    
    new_dic = {"Title": new_Title, "Url": new_Url}
    
    for dict_items in dictionary:
        if dict_items["index"] == chosen_index:
            if "NestedTabs" in dict_items:
                dict_items["NestedTabs"].append(new_dic)
            else:
                dict_items["NestedTabs"] = new_dic
        
    print(dictionary)
#-----------------------------------------------------
def saveTabs(dictionary, new_file_path):
    
    with open(new_file_path, "w") as outfile: 
        json.dump(dictionary, outfile)

#-----------------------------------------------------
def checkIndex(dict_items, index):
    
    for my_dict in dict_items:
        
        if my_dict.get("index") == index:
            return True
    return False

#-----------------------------------------------------
main()
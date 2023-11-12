# FCS CYCLE 49
# Midterm Solution
# Due Date: Nov 12th, 11:59 PM
# Name: Abbas kanj
# ---------------------------
import json # Used for handling json files
import sys # Library used for exiting the program
import requests # Library for making a GET request
from bs4 import BeautifulSoup  # Library for parsing Html code

#----------------------------------------------------- 
# Used links:
# https://www.geeksforgeeks.org
# https://www.datacamp.com/tutorial/web-scraping-using-python
# https://stackoverflow.com

#----------------------------------------------------- 
# Initializing an empty dicitonary to use in the program if non is imported.
dictionaryUrl = []

#-----------------------------------------------------
def main():
    # Start of the function
    print("Greeetings User")
    while(True):

        try:
            displaymenu()
            choice = int(input("Please select one of the options: "))
        except:
            # Error handling user input
            print("Invalid Input....")
            continue

        if choice == 1:
            # Option for creating a tab
            title = str(input("Enter the Title of the website: "))
            url = str(input("Enter the Url of the website(Make sure it starts with https://)"))
            openTab(dictionaryUrl, title, url)
            
        elif choice == 2:
            # Option for closing a tab
            clsdTab = int(input("Enter the index of the tab you want to close(Enter 0 to close the last opened tab): "))
            closeTab(dictionaryUrl, clsdTab)
            
        elif choice == 3:
            # Option for displaying tab
            switch_index = int(input("Enter the index of the tab you want to display(Enter 0 to show the last opened tab): "))
            switchTab(dictionaryUrl, switch_index)

        elif choice == 4:
            # Option for displaying all tabs
            displayAllTabs(dictionaryUrl)

        elif choice == 5:
            # Option for adding nested tabs
            
            # Check if the Parent tab is present in the list
            check_index = int(input("Enter the index of the parent tab you want to insert additional tabs: "))
            result = checkIndex(dictionaryUrl,check_index)
            
            if result:
                new_title = str(input("Enter the Title of the nested tab: "))
                new_url = str(input("Enter the Url of the title: "))
                openNestedTab(dictionaryUrl, check_index, new_title, new_url) 
            else:
                print("The index you where searching for is not found")

        elif choice == 6:
            # Option for clearing the list
            dictionaryUrl.clear()
            print("Dictionary Cleared")

        elif choice == 7:
            # Option for saving the tabs in a specific file path
            new_file_path = str(input("Enter the file path you want to save the tabs in: "))
            saveTabs(dictionaryUrl, new_file_path)

        elif choice == 8:
            # Option for importing the tabs for a specific file path
            import_from = str(input("Enter the file path you want to import from: "))
            defined_import = rf'{import_from}'
            
            with open(defined_import) as json_file:
                imported_dictionary = json.load(json_file)
            # Modifying the empty dicitonary
            dictionaryUrl = imported_dictionary
            print(dictionaryUrl)
            
        elif choice == 9:
            # Option for exiting the program
            print("Thanks for using my program! :)")
            sys.exit()

#-----------------------------------------------------
def displaymenu():
    # Function for displaying the menu
    print("----------------------------")
    print("1- Open Tab\n" + "2- Close Tab\n" + "3- Switch Tab\n" + "4- Display All Tabs\n" + "5- Open Nested Tab\n" + "6- Clear All Tabs\n" + "7- Save Tabs\n" + "8- Import Tabs\n" + "9- Exit\n")
    print("----------------------------")
    
#-----------------------------------------------------
def openTab(dict_items, title, url):
    # Append tab to an empty list
    if not dict_items:
        dict_items.append({"index": 1, "Title": title, "Url": url})
    # Append tab to an existing list
    else:
        iter = dict_items[-1].get("index") + 1
        dict_items.append({"index": iter, "Title": title, "Url": url})
    
#-----------------------------------------------------
def closeTab(dict_items, deletedTab):
    # Check if index is found
    if deletedTab not in dict_items:
        print("Index not found!")
    # Closing the last opened Tab
    elif deletedTab == 0:
        dict_items.pop()
    # Closing tab based on index
    else:
        for dict in dict_items:
            if dict["index"] == deletedTab:
                dict_items.remove(dict)
                break
            
#-----------------------------------------------------
def switchTab(dict_items, displayed_index):
    # Check if the index is present in the list
    index_found = False
    for dict_item in dict_items:
        for key, value in dict_item.items():
            if value == displayed_index:
                index_found = True
                break
    
    if not index_found:
        print("Index not found")
        return
    
    # Displaying the content of the last opened tab
    if displayed_index == 0:
        last_url = dict_items[-1].get("Url")
        # Making a GET request 
        r = requests.get(last_url) 
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'html.parser') 
        print(soup.prettify())
    # Display the content of the specified index
    else:
        for dict_item in dict_items:
            for key, value in dict_item.items():
                if value == displayed_index:
                    selected_url = dict_item["Url"]
                    print(selected_url)
                    
                    # Making a GET request 
                    r = requests.get(selected_url) 
                    # Parsing the HTML 
                    soup = BeautifulSoup(r.content, 'html.parser') 
                    print(soup.prettify())
                    return
                
#-----------------------------------------------------
def displayAllTabs(dict_items):
    # Check if the list is empty
    if dict_items == []:
        print("There are no Tabs to display")
        
    else:
        
        for dict in dict_items:
            title = dict.get("Title")
            print(title)
            # Checks if there are nested tabs inside the parent tab
            if "NestedTabs" in dict:
                nested_tabs = dict['NestedTabs']
                
                for titles in nested_tabs:
                        nested_title = titles.get("Title")
                        print(f'\t{nested_title}')

#-----------------------------------------------------
def openNestedTab(dictionary, chosen_index, new_Title, new_Url):
    # Creating nested tabs
    new_dic = {"Title": new_Title, "Url": new_Url}
    
    for dict_items in dictionary:
        # Check if the parent tab is not present
        if dict_items["index"] not in dictionary:
            print("Index wasn't found!")
        # Check if the parent tab is present
        elif dict_items["index"] == chosen_index:
            # Checks if there's a nested tab in the parent tab
            if "NestedTabs" in dict_items:
                dict_items["NestedTabs"].append(new_dic)
            # Creates a nested tab in the parent tab and appends the new content
            else:
                dict_items["NestedTabs"] = new_dic
        
    print(dictionary)
#-----------------------------------------------------
def saveTabs(dictionary, new_file_path):
    # Saving Tabs to a specified path
    with open(new_file_path, "w") as outfile: 
        json.dump(dictionary, outfile)

#-----------------------------------------------------
def checkIndex(dict_items, index):
    # Function for checking if a specific index is present in the list
    for my_dict in dict_items:
        
        if my_dict.get("index") == index:
            return True
        
    return False

#-----------------------------------------------------
main()
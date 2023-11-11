# FCS CYCLE 46
# Midterm Solution
# Due Date: Nov 12th, 11:59 PM
# Name: Abbas kanj
# ---------------------------
import json
import requests 
from bs4 import BeautifulSoup 

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
            openTab()

        elif choice == 2:
            closeTab()

        elif choice == 3:
            switchTab()

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

def openTab() :
    print()

#-----------------------------------------------------

def closeTab():
    print()

#-----------------------------------------------------

def switchTab():
    print()

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
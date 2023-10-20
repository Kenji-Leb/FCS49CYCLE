# FCS CYCLE 49
# Assignment 1
# Due Date: October 21, 10am
# Name: Abbas Kanj
#---------------------------------
def main():
    while(True):
        try:
            displaymenu()
            choice = int(input("Please select one of the options: "))
        except:
            print("Invalid Input....")
            continue
        if choice == 1:
            intFactorial()
        elif choice == 2:
            divFinder()
        elif choice == 3:
            reverseString()
        elif choice == 4:
            evenNb()
        elif choice == 5:
            print()


#-----------------------------------------------------
def displaymenu():
    print("----------------------------")
    print("1- Factorial Finder\n" + "2- Divisor Finder\n" + "3- Reverse a string\n" + "4- Only Even nb\n" + "5- Strong Password\n")
    print("----------------------------")
#-----------------------------------------------------
def intFactorial():
    n=int(input("Enter number: "))
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    print("Factorial of the number is: " + str(fact))
#-----------------------------------------------------
def divFinder():
    n = int(input("Enter number: "))
    div = []
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
    print(div)
#----------------------------------------------------
def reverseString():
    string = str(input("Enter word: "))
    str1 = "" 
    for i in string:  
        str1 = i + str1  
    print(str1)
#------------------------------------------------------
def evenNb():
    lst1 = []
    print("Enter your integers: (Type -1 to exit)")
    integer = int
    while integer != -1 :
        integer = int(input())
        if integer % 2 == 0:
            lst1.append(integer)
    print(lst1)
#------------------------------------------------------
def strongPass():
    print()
#------------------------------------------------------
main()



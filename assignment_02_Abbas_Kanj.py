# FCS CYCLE 49
# Assignment 2
# Due Date: October 28, 10am
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
            num = int(input("Enter your number: "))
            result = countDigits(num)
            print(result)
        elif choice == 2:
            listOfNums = list(map(int, input("Enter multiple values: ").split()))
            result2 = findMax(listOfNums)
            print(result2)
        elif choice == 3:
            htmlCode = '''
            <html>
            <head>
            <title>My Website</title>
            </head>
            <body>
            <h1>Welcome to my website!</h1>
            <p>Here you'll find information about me and my hobbies.</p>
            <h2>Hobbies</h2>
            <ul>
            <li>Playing guitar</li>
            <li>Reading books</li>
            <li>Traveling</li>
            <li>Writing cool h1 tags</li>
            </ul>
            </body>
            </html>
            '''
            tag = str(input("Enter the Tag you want to search: "))
            countTags(tag ,htmlCode)
        elif choice == 4:
            exit

#-----------------------------------------------------
def displaymenu():
    print("----------------------------")
    print("1- Count Digits\n" + "2- Find Maximum number\n" + "3- Count Tags\n" + "4- Exit\n")
    print("----------------------------")
#-----------------------------------------------------
def countDigits(number):
    if abs(number) < 10:
        return 1
    else:
        return 1 + countDigits(number // 10)
#-----------------------------------------------------
def findMax(newList):

    if not newList:
        return None

    if len(newList) == 1:
        return newList[0]

    maxNum = findMax(newList[1:])

    if newList[0] > maxNum:
        return newList[0]
    else:
        return maxNum
#-----------------------------------------------------
def countTags(tagFinder ,validHtml):
    newList = list(validHtml.split())
    tagList = []
    for i in newList:
        if i[0].startswith("<") and i[-1].endswith(">") :
            tagList.append(i)
    print(tagList)
    # startTag = "<" + tagFinder + ">"
    # endTag = "</" + tagFinder + ">"
    # for i in newList:
    #     if validHtml.index(startTag) == i and validHtml.index(endTag) == i :
    #         return 1 + countTags(tagFinder, validHtml)
    # else:
    #     print("Not found.")
#-----------------------------------------------------
main()
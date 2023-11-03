# FCS CYCLE 49
# Assignment 3
# Due Date: November 5, 10am
# Name: Abbas Kanj
#---------------------------------
import operator

def main():

    while(True):

        try:
            displaymenu()
            choice = int(input("Please select one of the options: "))
        except:
            print("Invalid Input....")
            continue

        if choice == 1:
            iD = int(input("Enter the Student's ID: "))
            GetStudentbyID(student_data, iD)

        elif choice == 2:
            GetAllStudents(student_data)

        elif choice == 3:
            major = str(input("Enter major: "))
            GetStudentsbyMajor(student_data, major)

        elif choice == 4:
            newName = str(input("Enter Student's name: "))
            newAge = int(input("Enter Student's Age: "))
            newMajor = str(input("Enter Studnet's Major: "))
            newGpa = float(input("Enter Studnent's GPA: "))
            AddStudent(student_data, newName, newAge, newMajor, newGpa)

        elif choice == 5:
            FindCommonMajors(student_data, student_data_2)

        elif choice == 6:
            student_ID = int(input("Enter the Student's ID you want to remove: "))
            DeleteStudent(student_data, student_ID)

        elif choice == 7:
            CalculateAverageGPA(student_data)

        elif choice == 8:
            top_Performers = int(input("Enter the number of Top Performers: "))
            GetTopPerformers(student_data, top_Performers)

        elif choice == 9:
            exit

#-----------------------------------------------------
def displaymenu():
    print("----------------------------")
    print("1- Get Student by ID\n" + "2- Get All Students\n" + "3- Get Students by Major\n" + "4- Add Student\n" + "5- Find Common Majors\n" + "6- Delete Student\n" + "7- Calculate Average GPA\n" + "8- Get Top Performers\n" + "9- Exit\n")
    print("----------------------------")
#-----------------------------------------------------
def GetStudentbyID(student_data, iD):

    for dict in student_data:
        for key, value in dict.items():
            if value == iD:
                print(f"{dict['Name']}, {dict['Age']}, {dict['Major']}, {dict['GPA']}")
            
#-----------------------------------------------------
def GetAllStudents(student_data):

    print(student_data)
#-----------------------------------------------------
def GetStudentsbyMajor(student_data, major):

    commonMajor = []

    for dict in student_data:
        for key, value in dict.items():
            if value == major:
                commonMajor.append(dict['Name'])

    print(commonMajor) 
#-----------------------------------------------------
def AddStudent(student_data, x, y, z, k):

    iteration = student_data[-1].get("ID") + 1

    newStudent = {"ID": iteration, "Name": x, "Age": y, "Major": z, "GPA": k}
    student_data.append(newStudent)

#-----------------------------------------------------
def FindCommonMajors(lst1, lst2):

    majorlst1 = []
    majorlst2 = []

    for dict in lst1:
        majorlst1.append(dict.get("Major"))

    for dict in lst2:
        majorlst2.append(dict.get("Major"))
    
    a_set = set(majorlst1)
    b_set = set(majorlst2)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")

#-----------------------------------------------------
def DeleteStudent(student_data, deleted_ID):
    
    for dict in student_data:
        for key, value in dict.items():
            if value == deleted_ID:
                student_data.remove(dict)

#-----------------------------------------------------
def CalculateAverageGPA(student_data):

    lst_of_GPA = []

    for dict in student_data:
        lst_of_GPA.append(dict.get("GPA"))
        
    print(f" Average GPA: {round( sum(lst_of_GPA) / len(lst_of_GPA), 2)}")

#-----------------------------------------------------
def GetTopPerformers(lstOfStudents, numOfTopStudents):

    lstOfNames = []
    lstOfGPA = []
    
    for x in lstOfStudents:
        lstOfNames.append(x.get("Name"))
        lstOfGPA.append(x.get("GPA"))

    dictionary = {}

    for i in range(len(lstOfNames)):
        dictionary[lstOfNames[i]] = lstOfGPA[i]

    sorted_dic = {key: val for key, val in sorted(dictionary.items(), key = lambda ele: ele[1], reverse = True)}

    top_Performers = dict(list(sorted_dic.items())[0: numOfTopStudents])

    print(str(top_Performers))

#-----------------------------------------------------
student_data = [
{
        "ID": 1,
        "Name": "Alice",
        "Age": 20,
        "Major": "Computer Science",
        "GPA": 3.7
    },
{
    "ID": 2,
    "Name": "Bob",
    "Age": 21,
    "Major": "Engineering",
    "GPA": 3.9
    },
{
    "ID": 3,
    "Name": "Frank",
    "Age": 25,
    "Major": "Pharmacist",
    "GPA": 4.0
    },
{
    "ID": 4,
    "Name": "Sally",
    "Age": 24,
    "Major": "Interior Architect",
    "GPA": 3.8
    },
{
    "ID": 5,
    "Name": "Rey",
    "Age": 22,
    "Major": "Engineering",
    "GPA": 3.9
    }
]
#-----------------------------------------------------
student_data_2 = [
{
        "ID": 1,
        "Name": "Alie",
        "Age": 20,
        "Major": "Computer Science",
        "GPA": 3.7
    },
{
    "ID": 2,
    "Name": "Bart",
    "Age": 21,
    "Major": "Mechanical Engineering",
    "GPA": 3.9
    },
{
    "ID": 3,
    "Name": "Freddie",
    "Age": 25,
    "Major": "Pharmacist",
    "GPA": 4.0
    },
{
    "ID": 4,
    "Name": "Susan",
    "Age": 24,
    "Major": "Interior design",
    "GPA": 3.8
    },
{
    "ID": 5,
    "Name": "Ralf",
    "Age": 22,
    "Major": "Bio Med",
    "GPA": 3.9
    }
]
#-----------------------------------------------------
main()
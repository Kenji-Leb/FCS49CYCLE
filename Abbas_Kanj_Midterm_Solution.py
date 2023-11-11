# FCS CYCLE 46
# Midterm Solution
# Due Date: Nov 12th, 11:59 PM
# Name: Abbas kanj
# ---------------------------
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

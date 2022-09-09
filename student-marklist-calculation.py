#Program to print students marklist
import os
os.system('clear')
try:
    print(f"Enter the number of  students marks total marks to be calculated:\n(Maximum 100 marks per subject)")
    number_of_students = int(input())
    students_details_dict= {}
    for i in range(number_of_students):
        print(f"Enter the student {i+1} details")
        print(f"Enter the student {i+1} register number")
        register_number = int(input())
        print(f"Enter the student {i+1} subject-1 mark")
        subject1_mark = int(input())
        print(f"Enter the student {i+1} subject-2 mark")
        subject2_mark =  int(input())
        print(f"Enter the student {i+1} subject-3 mark")
        subject3_mark =  int(input())
        total_marks = 0
        if subject1_mark > 100 or subject2_mark > 100 or subject3_mark > 100 or subject1_mark < 0 or subject2_mark < 0 or subject3_mark < 0:
            total_marks = "Invalid Marks"
        else:
            total_marks = str(subject1_mark + subject2_mark +subject3_mark)
        student_index_details = [register_number,subject1_mark,subject2_mark,subject3_mark,total_marks]
        students_details_dict[i] = student_index_details
    print("_______________________________________________________________________________________________________________________________________________")
    print('{:25s} {:32s} {:35s} {:35s} {:35s} '.format("Register Number","Subject-1 Mark","Subject-2 Mark","Subject-3 Mark","Total Marks"))
    print("_______________________________________________________________________________________________________________________________________________")
    for student_detail in students_details_dict.values():
        print('{:5d} {:25d} {:35d} {:35d} {:>37}'.format(student_detail[0],student_detail[1],student_detail[2],student_detail[3],str(student_detail[4])))
        print("_______________________________________________________________________________________________________________________________________________")
except Exception as error:
    print(f"Error occured inside the program\nPlease find the error deatils: {error}")
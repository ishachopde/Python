student_list=[]

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0

        total_sum = sum(self.marks)
        return total_sum / number

def create_student():
    # ask for student's name
    name = input("Enter new student's name: ")
    # create dictionary
    student_data = Student(name)
    # return dictionary
    return student_data

def add_mark(student, mark):
    # append marks to the dictionary
    student.marks.append(mark)


def student_details(student):
    print("{},average marks: {}.".format(student.name,
                                        student.average_mark()))


def print_student_list(students):
    for i,student in enumerate(students):
        print("ID: {}.".format(i))
        student_details(student)

def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")

    while selection!='q':
        if selection== "p" :
            print_student_list(student_list)
        elif selection== "s":
            student_list.append(create_student())
        elif selection== "a":
            student_id = int(input("enter  student ID to add marks to: "))
            student = student_list[student_id]
            new_marks = int(input("Enter new marks: "))
            add_mark(student,new_marks)

        selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")

menu()
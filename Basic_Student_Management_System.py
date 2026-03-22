'''
 The Basic Student Management System is an OOP project in Python which uses the classes, encapsulation and basic 
 operations like the add, view, search, update and delete students.  

 The main features of the Student Management System in Pyhton which uses the features like the: 
      1. Add the students 
      2. View Students 
      3. Search student by ID 
      4. Update student details 
      5. Delete students 
''' 

class Student: 
    def __init__(self, student_id, name, age, grade): 
        self.student_id = student_id 
        self.name = name 
        self.age = age 
        self.grade = grade 

    def display(self): 
        print(f"ID: {self.student_id}, Name:{self.name}, Age: {self.age}, Grade: {self.grade}") 

class StudentManagementSystem: 
    def __init__(self): 
        self.students = [] 

    def add_student(self): 
        student_id = input("Enter the Student ID: ") 
        name = input("Enter the name: ") 
        age = int(input("Enter the age: ")) 
        grade = input("Enter the grade: ") 

        student = Student(student_id, name, age,grade) 
        self.students.append(student) 
        print("✅ Student added successfully!\n") 

    def view_students(self): 
        if not self.students: 
            print("No students found\n") 

        else: 
            for student in self.students: 
                student.display()
            print()  

    def search_student(self): 
        student_id = input("Enter the student ID to search: ") 
        for student in self.students: 
            if student.student_id == student_id: 
                student.display() 
                return
        print("❌Student not found")  


    def update_student(self): 
        student_id = input("Enter the Student ID to update: ") 
        for student in self.students: 
            if student.student_id == student_id: 
                student.name = input("Enter the new name: ") 
                student.age = input("Enter the new age: ") 
                student.grade = input("Enter new grade: ")
                print("✅ Student updated successfully!\n") 
                return 
        print("❌ Student not found.\n")  

    def delete_student(self): 
        student_id = input("Enter the Student ID to delete: ") 
        for student in self.students: 
            if student.student_id == student_id: 
                self.students.remove(student) 
                print("✅ Student deleted successfully!\n") 
                return 
            
        print("❌ Student not found.\n") 


system = StudentManagementSystem() 

while True: 
    print("====== Student Management System =======") 
    print("1. Add Student") 
    print("2. View Students") 
    print("3. Search Student") 
    print("4. Update Student") 
    print("5. Delete Student") 
    print("6. Exit") 

    choice = input("Enter your choice: ") 

    if choice == '1': 
        system.add_student() 

    elif choice == '2': 
        system.view_students() 

    elif choice == '3': 
        system.search_student() 

    elif choice == '4': 
        system.update_student() 

    elif choice == '5':
            system.delete_student()
        
    elif choice == '6':
            print("Exiting program...")
            break  
    
    else: 
        print("Invalid Choice! Try Again.")  
    




    


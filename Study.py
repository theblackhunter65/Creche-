f1 = 1
while f1 == 1:
    print("\nMENU:")
    print("Enter the desired option:")
    print("1 - Registration")
    print("2 - Reports")
    print("3 - Exit")
    
    opc = int(input("Choose an option: "))
    
    if opc == 1:
        f3 = 1
        while f3 == 1:
            print("\nRegister")
            print("1 - Teacher")
            print("2 - Students")
            print("3 - Back")
            opc1 = int(input("What is your option: "))
            
            if opc1 == 1:
                print("\nRegister the teacher")
                teacher_name = input("Teacher's Name: ")
                teacher_age = int(input("Teacher's Age: "))
                teacher_email = input("Enter the teacher's email: ")
                teacher_salary = input("Teacher's Salary: ")
                teacher_phone = input("Teacher's Phone: ")

                print(f"Teacher {teacher_name} registered successfully!")
            
            elif opc1 == 2:
                print("\nRegister the student")
                student_name = input("Student's Name: ")
                student_age = int(input("Student's Age: "))
                student_enrollment = int(input("Student Enrollment: "))
                student_email = input("Enter the student's email: ")
                room_number = input("Classroom (number and letter): ")

                print(f"Student {student_name} successfully registered!")
            
            elif opc1 == 3:
                print("Returning to the main menu...")
                f3 = 0
            
            else:
                print("Invalid option! Try again.")

    elif opc == 2:
        f3 = 1
        while f3 == 1:
            print("\nSubmit reports")
            print("1 - Administrative")
            print("2 - Academic")
            print("3 - Back")
            
            opc2 = int(input("What is your option: "))
            
            if opc2 == 1:
                print("\nAdministrative Report")
                daycare_name = input("Name of the rural daycare: ")
                director_name = input("Director's Name: ")
                transportation_name = input("Name of the transport: ")
                daycare_cost = input("Cost of the daycare: R$ ")
                enrolled_children = input("Number of enrolled children: ")
                attendance_frequency = input("Attendance frequency: ")
                maintenance_cost = input("Maintenance and renovation cost: R$ ")

                print(f"\nReport Summary for {daycare_name}:")
                print("Director:", director_name)
                print("Transport:", transportation_name)
                print("Cost: R$", daycare_cost)
                print("Number of children:", enrolled_children)
                print("Attendance frequency:", attendance_frequency)
                print("Maintenance cost: R$", maintenance_cost)
                print("Our rural daycare is one of the best in the region!")

            elif opc2 == 2:
                print("\nAcademic Report")
                institution_name = input("Name of the Daycare: ")
                limited_resource = input("Amount of limited resource: R$ ")

                print(f"\nThe daycare {institution_name} is located in rural Minas Gerais.")
                print("It has one of the best approval rates in the region.")
                print(f"Limited resource available: R$ {limited_resource}")
                print("We are committed to creative solutions to maintain quality education.")

            elif opc2 == 3:
                print("Returning to the main menu...")
                f3 = 0

            else:
                print("Invalid option! Try again.")

    elif opc == 3:
        print("Exiting... See you soon!")
        f1 = 0

    else:
        print("Invalid option! Try again.")

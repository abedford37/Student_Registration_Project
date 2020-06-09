#Import student class
import student

#Import classes class
import course

#Define the input file
INPUT = "students.txt"

#Define the output file
OUTPUT = "students-updated.txt"

#Define the input file
INPUT_2 = "courses.txt"

#Define the output file
OUTPUT_2 = "courses-updated.txt"



#Define the main function
def main():
    
#Declare variables
    
    #Declare file_found variable as True
    file_found = True

    #Declare good_data variable as True
    good_data = True

    #Call Process Student File Function
    student_dict = process_student_file()

    #Call Process Course File Function
    course_dict = process_course_file()

    #Call print_main_menu function
    #print_main_menu()
    
    #Call the get_menu function to ask the user for their menu option
    menu_opt = get_menu()

    #Initialize x
    x=0

    #While x=0
    while (x==0):

        #If the user picks menu option 1, 
        if (menu_opt == 1):

            #Ask user for student id
            stu_id = input("What is your student ID? ")

	#if the student id is not found in the dictionary,
            while stu_id not in student_dict:

	    #Re-ask for user student id
                stu_id = input("Student is not found in the dictionary. What is your student ID? ")

	#Create a student object
            stu_object = student_dict[stu_id]       
            
           #Create a class list by calling a method from the student class
            class_list=stu_object.get_classes()
            
            #Call get_unique_num function
            unique_num = get_unique_num(course_dict)

	#Set added attempt to True
            added_attempt = True

	#If the unique class number is in the class list:
            if unique_num in class_list:

	    #Change added attempt to False
                added_attempt = False

	#If added attempt is false,
            if added_attempt == False:

	    #Print class is already added so it can’t be re-added
                print("Class is already added. It cannot be added again.")

	#Else,
            else:

                #Update the course catalog
                if unique_num in course_dict:

	       #Create a course object
                    course_object = course_dict[unique_num]

	        #Calculate the remaining seats left
                    spots=course_object.calc_seats_remaining()
                    
	        #If there are spots available in the class
                    if(spots>0):

	            #Call the enroll student method from the course cell
                        course_object.enroll_student()

	             #Call the add student method from the student cell
                        stu_object.add_class(unique_num)

	            #Create a student object
                        student_dict[stu_id]=stu_object

                        #Print class was added.
                        print("Class was successfully added. Everything is up to date")

	        #Else,
                    else:

		#Print no spots are available
                        print("no spots available")

            #Call the get_menu function
            menu_opt = get_menu()

        #Elseif  the user picks menu option 2,
        elif (menu_opt == 2):

	#Ask user for student id
            stu_id = input("What is your student ID? ")

	#While the student id is not found in the student dictionary,
            while stu_id not in student_dict:

	    #Re-ask for a different student id
                stu_id = input("Student is not found in the dictionary. What is your student ID? ")

	#Create a student object
            stu_object = student_dict[stu_id]       
         
            #Call get_unique_num function
            unique_num = get_unique_num(course_dict)
            
	#Set added to False
            added = False

	#If the unique class number is in the class list,
            if unique_num in class_list:

	    #Change added to True
                added = True

	#If added is False
            if added == False:

	    #Print the class is already dropped
                print("Class is already dropped. It cannot be dropped again.")

	#Else
            else:

                #If the unique number is in the course dictionary,
                if unique_num in course_dict:

	        #Create a course object
                    course_object = course_dict[unique_num]

	        #Call the drop student method in the course class
                    course_object.drop_student()

	        #Call the drop class method in the student class
                    stu_object.drop_class(unique_num)

	        #Create a student object
                    student_dict[stu_id]=stu_object

                #Print class was added.
                print("Class was successfully dropped. Everything is up to date")
                
            #Call the get_menu function
            menu_opt = get_menu()


         #Elif the user picks menu option 1
        elif (menu_opt == 3):

            #Call get_student_id function
            stu_object = get_student_id(student_dict)

	#Call the get_classes method from the student class
            courses = stu_object.get_classes()
            
	#for x in courses,
            for x in courses:

	   #Create a course object
                course_object=course_dict[x]

	   #Call the get_title method from the course class
                title= course_object.get_title()

	   #Call the get_prof method from the course class
                prof=course_object.get_prof()

	    #Print x, the course title, and the professor name
                print(x, title, prof)

            #Call the get_menu function 
            menu_opt = get_menu()


        #Elseif  the user picks menu option 4,
        elif (menu_opt == 4):

	#For y in the course dictionary,
            for y in course_dict:

	   #Create an object
                x=course_dict[y]

	   #Call the get_title method from the class
                title=x.get_title()

	   #Call the get_prof method from the class
                prof=x.get_prof()

	    #Call the get_capacity method from the class
                capacity=x.get_capacity()

	   #Call the calc_seats_remaining method from the class
                remaining=x.calc_seats_remaining()

	   #Print all information from above
                print(y, '; ' ,title, 'Professor: ', prof, '; Total seats: ', capacity, '; Seats available: ' , remaining)

            #Call the get_menu function 
            menu_opt = get_menu()

         #Else,
        else:

      	#Open the student output file
            s=open ("students-updated.txt", 'w')

	#for x in the student dictionary
            for x in student_dict:

	    #Create a student dictionary
                stu=student_dict[x]

	   #Call the line for file method from the student class
                output=stu.line_for_file()

                s.write(output)

                output=''

	#Close the file
            s.close()

	#Open the courses output file
            c=open ("courses-updated.txt", 'w')

	#for y in the course dictionary
            for y in course_dict:

	    #Create a course dictionary
                cou=course_dict[y]

	    #Call the line for file method from the course class
                output2=cou.line_for_file()

                c.write(output2)

                output2=''

	#Close the course output file
            c.close()

	#Print courses are up to date
            print("Your courses have been updated. Check the output file for the most up-to-date information.")

            #Set a new variable to exit out the while loop
            x=1



#Define process student file function
def process_student_file():
    
#Declare variables
    
    #Declare file_found variable as True
    file_found = True

    #Declare good_data variable as True
    good_data = True

#Exception Block

    #Try opening your input file
    try:
        
        #Open input file
        student_file = open(INPUT, 'r')

    #Except if the file cannot be found,
    except FileNotFoundError:
        
        #Print error
        print("Could not find", INPUT, "in the current directory.")
        
        #Re-set variable
        file_found = False

    #If everything looks good, continue with logic
    if file_found:

        #Create a blank dictionary
        student_dict = {}

        #Read the first name line 
        student_data = student_file.readline().rstrip('\n')

        #Initialize n
        n=0

        #Create student instances
        while (student_data != ""):
            
            #Split the string
            student_list = student_data.split(':')
            
            #Set uteid string equal to a variable
            uteid = student_list[0]

            #Set first name string to a variable
            first_name = student_list[1]

            #Set last name string to a variable
            last_name = student_list[2]

            #Create an index variable
            index = int(3)

            #Create a blank class list
            class_list = []
            
            #While the length of the student list is greater than the index,
            while (len(student_list) > index):

	    #Set a variable equal to each number
                class_1 = int(student_list[index])

	    #Append the numbers into a list
                class_list.append(class_1)

	    #Change the index
                index = index + 1
            
             #Create a new student object          
            student_object = student.Student(uteid, first_name, last_name, class_list)

            #Append to the student dictionary
            student_dict.update({uteid: student_object})

            #Read the first name line 
            student_data = student_file.readline().rstrip('\n')
   
    #Return the student dictionary
    return student_dict

#Define process course file function
def process_course_file():
    
#Declare variables
    
    #Declare file_found variable as True
    file_found = True

    #Declare good_data variable as True
    good_data = True

#Exception Block

    #Try opening your input file
    try:
        
        #Open input file
        course_file = open(INPUT_2, 'r')

    #Except if the file cannot be found,
    except FileNotFoundError:
        
        #Print error
        print("Could not find", INPUT_2, "in the current directory.")
        
        #Re-set variable
        file_found = False

    #If everything looks good, continue with logic
    if file_found:
        
        #Create a blank dictionary
        course_dict = {}

        #Read the first name line 
        course_data = course_file.readline()
       
        #Create student instances
        while (course_data != ""):
            
            #Create a list
            course_list = course_data.split(";")
           
            #Set uteid string equal to a variable
            course_id = int(course_list[0])

            #Set class name string to a variable
            class_name = course_list[1]

            #Set professor name string to a variable
            prof_name = course_list[2]

            #Set seats filled in class string to a variable
            seats_filled = int(course_list[3])

            #Set total seats available in class string to a variable
            tot_seats_avail =int( course_list[4])
            
            #Create a course object
            course_object = course.Course(seats_filled)

	#Call the set unique method from the course class
            course_object.set_unique(course_id)

	#Call the set capacity method from the course class
            course_object.set_capacity(tot_seats_avail)

	#Call the set title method from the course class
            course_object.set_title(class_name)

	#Call the set prof method from the course class
            course_object.set_prof(prof_name)

            #Append course info to the dictionary
            course_dict.update({course_id: course_object})

            #Read the first name line 
            course_data = course_file.readline()
            
    #Return course dictionary
    return course_dict

#Define print main menu function
def print_main_menu():

    #Print the initial menu
    print("1. Add course" + "\n" + "2. Drop course" + "\n" + "3. Print student's schedule" + "\n" + "4. Print course schedule" + "\n" + "5. Done " + "\n")

#Define get menu function
def get_menu():

    #Call the print main menu function
    print_main_menu()

    #Get user input from menu options
    menu_opt = int(input("What would you like to do? Select a number from the menu. "))

    #Input Validation
    while (menu_opt > 5) or (menu_opt < 1):

        #Re-ask for user input
        menu_opt = int(input("ERROR! Invalid integer." + '\n' + "What would you like to do? Select a number from the menu. "))

    #Return the menu option
    return menu_opt


#Define the get student id function
def get_student_id(student_dict):

    #Ask for student id
    stu_id = input("What is your student ID? ")

    #While the student id is not found in the dictionary
    while stu_id not in student_dict:

        #Re-ask for the student id
        stu_id = input("Student is not found in the dictionary. What is your student ID? ")

    #Create a student object
    stu_object = student_dict[stu_id]

    #Return the student object
    return stu_object

#Define the get unique number function
def get_unique_num(course_dict):

    #Get unique number from the user
    unique_num = int(input("What is the course unique number? "))

    #While the unique number is not found in the course dictionary
    while unique_num not in course_dict:

        #Re-ask for the unique number
        unique_num = int(input("Incorrect number was entered. What is the course unique number? "))
    
    #Return the unique number
    return unique_num



    
    
#Call main function
main()

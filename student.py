#Define the student class
class Student():

    #Define init method
    def __init__(self, new_id, new_fname, new_lname, classes):

        #Set the uteid attribute
        self.__uteid = new_id

        #Set the first name attribute
        self.__fname = new_fname

        #Set the last name attribute
        self.__lname = new_lname

        #Set the class list attribute
        self.__class_list = classes

    #Define get uteid method
    def get_uteid(self):

        #Return uteid attribute
        return self.__uteid

    #Define get first name method
    def get_fname(self):

        #Return first name attribute
        return self.__fname

    #Define get last name method
    def get_lname(self):

        #Return last name attribute
        return self.__lname

    #Define get classes method
    def get_classes(self):

        #Return class list attribute
        return self.__class_list

    #Define add class method
    def add_class(self, unique_num):
        
        #If the class is already added,
        if unique_num in self.__class_list:

            #Return False
            return False

        #Else the class is not already added,
        else:
            
            #Add the class
            self.__class_list.append(unique_num)

            #Return True
            return True
        
    #Define drop class method
    def drop_class(self, unique_num):

        #If the class is not already dropped,
        if unique_num in self.__class_list:

            #Drop the class
            self.__class_list.remove(unique_num)

            #Return True
            return True

        #Else the class is already dropped,
        else:

            #Return False
            return False

    #Define line for file method
    def line_for_file(self):

        #Create a string for the output file
        line = str(self.__uteid) + ":" + self.__fname + ":" + self.__lname + ":"

        #For x in class list
        for x in self.__class_list:

            #Add the classes from the list to the string
            line =line+str(x)+' '

        #Add a backslash n
        line=line+'\n'

        #Return the string
        return line

    #Define str method
    def __str__(self):

        #Create a string for the attributes above
        string = "UTEID: " + str(self.__uteid) + "Name: " + str(self.__fname) + " " + str(self.__lname) + "Classes Enrolled in: " 


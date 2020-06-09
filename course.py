
#Define Course Class
class Course():

    #Define the initialize method
    def __init__(self, seats_taken):

        #Set Unique Attribute
        self.__unique = ""

        #Set Title Attribute
        self.__title = ""

        #Set Professor Attribute
        self.__prof = ""

        #Set Seats Taken Attribute
        self.__seats_taken = seats_taken

        #Set Capacity Attribute
        self.__capacity = 0

    #Define get unique method
    def get_unique(self):

        #Return Unique Attribute
        return self.__unique

    #Define set unique method
    def set_unique(self, new_unique):

        #Set variable equal to unique attribute
        self.__unique = new_unique

    #Define get title method
    def get_title(self):

        #Return title attribute
        return self.__title

    #Define set title method
    def set_title(self, new_title):

        #Set variable equal to title attribute
        self.__title = new_title

    #Define get professor method
    def get_prof(self):

        #Return professor attribute
        return self.__prof

    #Define set professor method
    def set_prof(self, new_prof):

        #Set variable to professor attribute
        self.__prof = new_prof

    #Define get seats taken method
    def get_seats_taken(self):

        #Return seats taken attribute
        return self.__seats_taken

    #Define get capacity method
    def get_capacity(self):

        #Return capacity attribute
        return self.__capacity

    #Define set capacity method
    def set_capacity(self, new_capacity):

        #Set variable to capacity attribute
        self.__capacity = new_capacity

    #Define calc seats remaining method
    def calc_seats_remaining(self):

        #Calculate the total seats remaining in a class
        seats_remaining = (int(self.__capacity)) - (int(self.__seats_taken))
        
        #Return the seats remaining variable
        return seats_remaining

    #Define seats available method
    def seats_available(self):

        #If there are seats remaining,
        if (seats_remaining > 0):

            #Return True
            return True

        #Else
        else:

	#Return False
            return False

    #Define enroll student method
    def enroll_student(self):

        #Add another seat to seats taken attribute
        self.__seats_taken = int(self.__seats_taken) + 1

        #Return seats taken attribute
        return self.__seats_taken

    #Define drop student method
    def drop_student(self):

        #Subtract another seat to seats taken attribute
        self.__seats_taken = int(self.__seats_taken) - 1

         #Return seats taken attribute
        return self.__seats_taken
        
    #Define line for file method
    def line_for_file(self):

        #Create the string to put in an output file
        line = (str(self.__unique) + ";" + self.__title + ";" + self.__prof + ";" + str(self.__seats_taken) + ";" + str(self.__capacity)+'\n')

        #Return the string
        return line

    #Define string method
    def __str__(self):

         #Create a string for the attributes above
        string = "Unique Number: " + str(self.__unique) + "\n" + "Course Name: " + str(self.__title) + "\n" + "Professor: " + str(self.__prof) + "\n" + "Seats Occupied: " + str(self.__seats_taken) + "\n" + "Capacity: " + str(self.__capacity)     

# This program looks at a list of people with 4 different pieces of information
# The program takes the id numbers of said person and looks for id numbers with a 91 in it
# the program will then append the data and display them in a seperate file called new_list
class Person:
    def __init__(self,first_name,last_name,username,id_num):
        self.first_name = first_name
        self.last_name = last_name
        self.username = " "
        self.id_num = id_num
        # for loop to remove all characters after the @ symbol
        for e in range(len(username)):
            if "@" in username[e]:
                break
            else:
                self.username = self.username + username[e]
    # creates the list format for the names that will be displayed
    def __str__(self):
        return "First Name: {} \n Last Name: {} \n Username: {} \n ID: {} \n \n".format(self.first_name,self.last_name,self.username,self.id_num)

class Student(Person):
    def __init__(self,first_name,last_name,username,id_num):
        super().__init__(first_name,last_name,username,id_num)

class Instructor(Person):
    def __init__(self,first_name,last_name,username,id_num):
        super().__init__(first_name,last_name,username,id_num)

class TeachingAssistant(Person):
    def __init__(self,first_name,last_name,username,id_num):
        super().__init__(first_name,last_name,username,id_num)

class Parser:
    def __init__(self):
        self.students = []
        self.instructors =[]
        self.tas =[]
    def parse(self,filename):
        # opens the file and stores it values in a new array for 
        # parse places the stored values under the required names 
        read = open(filename, "r")
        lines = read.readlines()
        read.close()
        # it checks the first 4 given objects of the person
        # it appends the info and classifies if they are a student, etc.
        for i in range(len(lines)):
            x = lines[i].split(" ")
            if len(x) == 5:
                if x[4] == "Student\n":
                    self.students.append(lines[i])
                elif x[4] == "Instuctor\n":
                    self.instructors.append(lines[i])
                elif x[4] == "TA\n":
                    self.tas.append(lines[i])
    def get_students(self):
        return self.students

    def get_instructors(self):
        return self.instructors

    def get_tas(self):
        return self.tas

class Main:
    # Initializing the parser class and creates an array
    def __init__ (self):
        super().__init__()
        self.parser = Parser()
    def parse_file(self,filename):
        self.parser.parse(filename)
    def get_students(self,str1):
        self.persons = []
        self.student_list = self.parser.get_students()
        # checks to see if a student number includes a 91 and creates a list of those persons
        k = len(self.student_list)
        for i in range(k):
            str2 = self.student_list[i].split(" ")
            if "91" in str2[3]: 
                self.persons.append(self.student_list[i])
        return self.persons
    def write_to_file(self,persons,filename):
        writing = open(filename,"w")
        # goes through the filename and appends it in the person array
        # it then displays the values in the same format found in Person Class
        for i in range(len(persons)):
            z = persons[i].split(" ")
            person = Person(z[0],z[1],z[2],z[3])
            writing.write(str(person))

# oop_stuff.py

class Student(object):
    pop = 0
    def __init__(self, firstname, lastname):
        Student.pop += 1
        self.firstname = firstname
        self.lastname = lastname

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname   

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname 

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    @fullname.setter
    def fullname(self, fullname):
        firstname, lastname = fullname.split(' ')
        self.__firstname = firstname
        self.__lastname = lastname
    
    @classmethod
    def show_class(cls):
        print(cls.__name__)

    @staticmethod
    def get_total_students():
        print(Student.pop)

    @classmethod
    def how_many_students(cls):
        print(cls.pop)


if __name__ == "__main__":
    st1 = Student('Neeraj','Nabar')

    Student.get_total_students()
    Student.how_many_students()
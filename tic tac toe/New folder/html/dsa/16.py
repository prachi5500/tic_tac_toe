class student:
    collage_name ="abc clg"
    name="andi"
    def __init__(self, fullname ,marks):
          #reference of object
        self.name= fullname
        self.marks= marks

    #create method  
    @staticmethod   
    def welcome():
        print("welcome student", self.name)    

    def get_marks(self):
        return self.marks    

#create object
s1=student("jyoti",67)
print(s1.name, s1.marks) 

s1.welcome()
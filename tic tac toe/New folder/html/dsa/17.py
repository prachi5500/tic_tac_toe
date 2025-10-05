class student:
    def __init__(self, name , marks):
        self.name= name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+= val
        print("hi",self.name,"your avg score is to:",sum/3)        

s1= student("arav",[99,42,85])   
s1.get_avg()    

s1.name="ironman"
s1.get_avg()
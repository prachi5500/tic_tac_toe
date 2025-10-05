class student:
    def __init__(self,phy, chem,math):
        self.phy= phy
        self.chem= chem
        self.math=math
        self.percentage= str((self.phy + self.chem + self.math)/3) +"%"
    @property
    def percentage(self):
        return str((self.phy + self.chem +self.math)/3)+"%"
stu1= student(95,90,98)
print(stu1.percentage)      

stu1.phy= 60
print(stu1.percentage)
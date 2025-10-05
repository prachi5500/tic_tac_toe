# # class circle:
# #     def __init__(self,radius):
# #         self.radius=radius
# #     def area(self):
# #         return 3.14 *self.radius**2
# #     def perimeter(self):
# #         return 2 *3.14 *self.radius
# # c1=circle(21)
# # print(c1.area())
# # print(c1.perimeter())    
# class employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def showdetails(self):
#         print("role=", self.role)
#         print("dept=", self.dept)
#         print("salary=", self.salary)

# class engineer(employee):
#     def __init__(self,name,age):
#         self.name =name
#         self.age =age 
#         super().__init__("engineer","it","80000")

# e1=engineer("elon musk","40")
# e1.showdetails()

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price >odr2.price
odr1= order("chips",20)
odr2=order("tea",15)

print(odr1 >odr2)


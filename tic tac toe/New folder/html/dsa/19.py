# class account:
#     def __init__(self, acc_no , acc_pass):
#         self.acc_no= acc_no
#         self.__acc_pass= acc_pass


#     def reset_pass(self):
#         print(self.__acc_pass)




# acc1= account("12334","qwerrt")
# print(acc1.acc_no)
# print(acc1.__acc_pass)

class person:
    __name ="anymore"

    def __hello(self):
       print("hello person")
    def welcome(self):
       self.__hello()

p1= person()
print(p1.welcome)    
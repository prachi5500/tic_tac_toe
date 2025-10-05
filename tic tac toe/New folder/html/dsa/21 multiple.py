# class a:
#     vara = "welcome to class a"

# class b:
#     varb = "welcome to class b"

# class c(a,b):
#     varc = "welcome to class c"

# c1 = c()

# print(c1.varc)
# print(c1.varb)
# print(c1.vara)

class car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("car start..")

    
    @staticmethod
    def stop():
        print("car stoped..")

class toyotacar (car):
    def __init__(self, name, type ):
        super().__init__(type)
        self.name = name
class fortuner(toyotacar):
    def __init__(self, type):
        self.type = type


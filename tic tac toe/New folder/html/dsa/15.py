# with open("practice.txt","w") as f:
#     #we create file directly by using write module
#     f.write ("hi everyone \n we are learning file i/o")
#     f.write ("using java.\n i like programming in java.")

#questiion

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data =data.replace("java","python")
# print(new_data)
# 
# question    

# with open ("practice.txt","w") as f:
    #f.write(new_data)
# def check_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("not found")
# check_word()


# #question
# def check_for_line():
#     word ="learning"
#     data =True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1  
# check_for_line()

with open("practice.txt","r")as f:
    data=f.read()
    print(data)

    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num=""
    #     else:
    #         num += data[i]
    nums= data.split(",")
    print(nums)



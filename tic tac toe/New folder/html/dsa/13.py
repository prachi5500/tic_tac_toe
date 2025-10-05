# def show(n):
#     if(n==0):            #base case
#         return
#     print(n)
#     show(n-1)
#     print("end")
# show(5)    
# def fact(n):
#     if(n==1 or n==0):
#         return 1

#     return fact(n-1)*n
# print(fact(53))

# def calcsum(n):
#     if(n==0):
#         return 0
    
    
#     return calcsum(n-1) + n
# print(calcsum(8))

def list_p(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    list_p(list,idx+1)

fruits=["mango","banana","apple","litchi"]
list_p(fruits)    
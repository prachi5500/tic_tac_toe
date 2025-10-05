n= int(input(" enter a no:"))
fact=1
i=1
#while i<= n:
for i in range(1,n+1):
    fact*=i
    i+=1
print("factorial=",fact)
    
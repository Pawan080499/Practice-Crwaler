# n = int(input("enter the number"))
# n1 = 0
# n2 = 1
# for i in range(2,n):
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#     n = a + b 
#     n = b
#     b = c
#     print(c)

# for i in range(10):
#     c = n1+n2
#     n1 = n2
    
#     n2 = c
#     print(c)
    
# a=int(input("enter the value"))
# b=int(input("enter the value"))
# c=int(input("enter the value"))

# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))
# print(area)

    
    

    
    
    
    
            
# b = 1
# if n ==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(1,n):
#             a = i + b
#             print(a)


# count = 0
# while count < 5:
#    print (count, " is  less than 5")
#    count = count + 1
# else:
#    print (count, " is not less than 5")


# import datetime

# Get the current date and time
# now = datetime.datetime.now()

# # Extract month, week, hour, minute, and second
# current_month = now.month
# current_week = now.strftime("%U")  # ISO week number (0-53)
# current_hour = now.hour
# current_minute = now.minute
# current_second = now.second

# # Print the results
# print("Current Month:", current_month)
# print("Current Week:", current_week)
# print("Current Hour:", current_hour)
# print("Current Minute:", current_minute)
# print("Current Second:", current_second)


# interview questions

# my_list=['p','q']
# n=4
# l=[]
# # output= ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5', 'p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4']

# for i in range(1,n+1):
#     for a in my_list:
#         l.append(a+str(i))
# print(l)






# name = ['ram' ,'shyam','manoj']
# roll_nob = [1,2,3]
# marks = ['10' ,'20','30']

# # name [1]= "roll_nob"

# list = {
#     "output" : roll_nob [0] + name [0] + marks [0], 
# }

# print(str(list))


# fibonacci series in python
a=0
b=1
# print(a)
# print(b)
for i in range(1,11):
    c=a+b
    print(c)
    a,b=b,c
    
    
# n=int(input("Enter the number: "))
# a=0
# b=1
# if n<=0:
#     print(a)
# else:
#     print(b,end=" ")
#     for x in range(2,n):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
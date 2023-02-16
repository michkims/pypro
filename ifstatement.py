# if statement
x=1
marks=49
grade=200
points=8
if(x>0):
    print("The number is positive")
# if... else statement
if(marks>=50):
    print("You have passed the exam")
else:
    print("You have failed the exam")
# if.. elif..else statement
if(grade<=29 and grade>=0):
    print("You failed")
elif grade>=30 and grade<=49:
    print("You passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have a distinction")
else:
    print("wrong grade entered")

if(points>=0 and points<=2):
    print("last place")
elif points>=2 and points<=5:
    print("second place")
elif points>=5 and points<=8:
    print("first place")
else:
    print("no position")







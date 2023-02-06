# Python Program to Take in the Marks of 5 Subjects and Display the Grade
sub1=int(input("enter the marks of sub1:"))
sub2=int(input("enter the marks of sub2: "))
sub3=int(input("enter the marks of sub3: "))
sub4=int(input("enter the marks of sub4: "))
sub5=int(input("enter the marks of sub5: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("the grade is A")
elif(avg>=80):
    print("the grade is B")
elif(avg>=70):
    print("the grade is C")
elif(avg>=60):
    print("the grade is D")
else:
    print("the grade is F")

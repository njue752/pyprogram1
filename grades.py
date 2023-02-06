#program to output average grade score
subject_1=int(input("Enter subject 1 score"))
subject_2=int(input("Enter subject 2 score"))
subject_3=int(input("Enter subject 3 score"))
average=(subject_1+subject_2+subject_3)/3
if(average>=70 and average <100):
    print("Your grade is A")
elif(average>=60 and average <69):
    print("Your grade is B")
elif(average>=50 and average <59):
    print("Your grade is C")
elif(average>=40 and average <49):
    print("Your grade is D")
else:
    print("Your grade is Fail")

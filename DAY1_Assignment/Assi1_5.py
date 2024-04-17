# The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
#ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
#Average Grade
#90-100 A
#80-89 B
#70-79 C
#60-69 D
#0-59 F

sub1=int(input("Enter sub1 marks : "))
sub2=int(input("Enter sub2 marks : "))
sub3=int(input("Enter sub3 marks : "))

avg=int((sub1 + sub2 + sub3)/3)
print(f"avg = {avg}")
print(f"type def avg = {type(avg)}")

#def grade(A ,B ,C ,D, E, F):
if 90 < avg :
    print("Grade A")

elif 80 < avg:
    print("Grade B")
    
elif 70 < avg :
    print("Grade C")

elif 60 < avg :
    print("Grade D")

else:
    print("Grade F")
    






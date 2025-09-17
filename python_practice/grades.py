# define exam grades
grade = 36
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif grade <= 59 and grade >50:
    print("D-")
else : # the grade fall between 0 and 49
    print("fail")

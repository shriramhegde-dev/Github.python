name=input("name:") #enters student name
semester=int(input("semester:")) #enters student's sem
department=input("department:")  #enters student's department  
grade_point=int(input("grade_point:")) #enters student's grade_point
if grade_point>90:
    print("outstanding")
elif grade_point>=80:
    print("excellent")
elif grade_point>=70:
    print("good")
elif grade_point>=60:
    print("average")
elif grade_point>=40:
    print("passed")
else:
    print("failed")
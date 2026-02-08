import sys
student_name = input("Enter student name:")
maths_marks = int(input("Enter Maths marks:"))
if((maths_marks<0) or (maths_marks>100)):
   print("Invalid marks entered")
   sys.exit()
science_marks = int(input("Enter Science marks:"))
if(science_marks<0 or science_marks>100 ):
   print("Invalid marks entered")
   sys.exit()

english_marks = int(input("Enter English marks:"))
if(english_marks<0 or english_marks>100 ):
   print("Invalid marks entered")
   sys.exit()
total_marks = maths_marks+science_marks+english_marks

average_percentage = total_marks/3
print("Student Name:", student_name)
print("Total Marks:", total_marks)
print(f"Percentage: {average_percentage:.2f}")
if(maths_marks <40 or science_marks <40 or english_marks < 40):
    print("Status: FAIL")
else:
   print("Status: PASS")

if(average_percentage >= 75):
   print("Grade: A")
elif(average_percentage >= 60 and average_percentage<75):
    print("Grade: B")
else:
  print("Grade: C")




print("------STUDENT REPORT------")
Subjects={
    "Maths":int(input("Enter your Maths Marks: ")),
    "English":int(input("Enter your English Marks: ")),
    "Science":int(input("Enter your Science Marks: ")),
    "Social":int(input("Enter your Social Marks: ")),
    "Hindi":int(input("Enter your Hindi Marks: ")),
}
average=(Subjects["Maths"]+Subjects["English"]+Subjects["Science"]+Subjects["Social"]+Subjects["Hindi"])/5
print("Average:",average,"%")
if average>=90:
    print("Grade:A+ Excellent performance")
elif average>=85:
    print("Grade:A Good Performance")
elif average>=80:
    print("Grade:B+")
elif average>=75:
    print("Grade:B")
elif average>=70:
    print("Grade:C+")
elif average>=65:
    print("Grade:C")
elif average>=60:
    print("Grade:D")
else:
    print("Grade:F")
overall_fail=False
for Subject, marks in Subjects.items():
    print(Subject,marks)
    if marks <35:
        print(Subject,"Fail")
        overall_fail=True
    elif marks <45:
        print("You Need Improvement in ",Subject,".")
highest = max(Subjects, key=Subjects.get)
print("TOP SUBJECT is :",highest)
lowest = min(Subjects, key=Subjects.get)
print("WEAK SUBJECT is :",lowest)
if overall_fail:
    print("Overall Result:FAIL")
else:
    print("Overall Result:PASS")
print("-----THE-END-----")

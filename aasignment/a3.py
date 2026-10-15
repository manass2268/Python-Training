#Student Report Card Generator
s1=int(input("enter you first subject marks:"))
s2=int(input("enter you second subject marks:"))
s3=int(input("enter you third subject marks:"))
s4=int(input("enter you forth subject marks:"))
s5=int(input("enter you fifth subject marks:"))
total_marks=s1+s2+s3+s4+s5
avg=total_marks/5
per=total_marks/500*100
print("Total Marks:",total_marks)
print("Average Marks:",avg)
print("Percentage:",per,"%")

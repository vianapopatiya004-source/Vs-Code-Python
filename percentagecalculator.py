print("Enter Marks Obtained in 4 subjects:")
math = int(input("maths:"))
english = int(input("english:"))
hindi = int(input("hindi:"))
science = int(input("science:"))


sum = math+english+hindi+science 
print("Sum of all the subjects",sum)

perc= (sum/400)*100 

print("end=Percentage Mark=")
print(perc)
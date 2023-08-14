
Physics = int(input("Enter the Marks in Physics : "))
Chemistry = int(input("Enter the Marks in Chemistry: "))
Biology = int(input("Enter the Marks in Biology: "))
Mathematics = int(input("Enter the Marks in Mathematics: "))
Computer = int(input("Enter the Marks in Computer: "))
Total_Marks = Physics+Chemistry+Biology+Mathematics+Computer
Total_Subject = 5
Percentage= (Total_Marks / (Total_Subject * 100)) * 100
print("Percenage is ",Percentage)


if Percentage >= 90:
    print("Grade A")
elif Percentage >= 80:
    print("Grade B")
elif Percentage >= 70:
    print("Grade C")
elif Percentage >= 60:
    print("Grade D")
elif Percentage >= 40:
    print("Grade E")
elif Percentage < 40:
    print("Grade F")


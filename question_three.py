'''
NAME:KELVIN NZIOKA
REG_NO: PA106/G/9983/20
'''

#part (1)
def get_grade(average_mark):
    if average_mark >= 80  and average_mark<= 100:
        return "A"
    elif  average_mark >=70 and average_mark< 80:
        return "B"
    elif average_mark >=60 and average_mark < 70:
        return "C"
    elif  average_mark>=50  and average_mark < 60:
        return "D"
    elif average_mark >=0 and average_mark < 50:
        return "E"
    else:
        return "Invalid Mark"

# Input average mark
average_mark = float(input("Enter the average mark: "))

# Get and display the grade using the get_grade function
result = get_grade(average_mark)
print(f"Grade: {result}")




#part 2
def grade(average_mark):
    if  average_mark >=80 and average_mark <= 100:
        print("Grade: A")
    elif  average_mark >=70 and average_mark < 80:
        print("Grade: B")
    elif average_mark>=60 and average_mark < 70:
        print("Grade: C")
    elif average_mark >=50 and average_mark < 60:
        print("Grade: D")
    elif average_mark >=0 and average_mark < 50:
        print("Grade: E")
    else:
        print("Invalid Mark")

# Input average mark
average_mark = float(input("Enter the average mark: "))

# Call the grade function to print the grade
grade(average_mark)

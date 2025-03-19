#Title - Assignment-1-Control Structures - Q3
#To print the BMI Category
#Author - Yuvaraj Rajendran
#Date - 19/03/2025
indexValue = float(input("Enter the BMI Index: "))
if(indexValue < 18.5):
    print("Underweight")
elif(indexValue > 18.5 and indexValue < 24.9): 
    print("Normal Weight")
elif(indexValue > 25 and indexValue < 29.9): 
    print("Overweight")
else:
    print("Obese")
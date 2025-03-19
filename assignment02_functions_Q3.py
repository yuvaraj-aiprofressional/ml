#Title - Assignment-2- Functions - Q3
#Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
#Author - Yuvaraj Rajendran
#Date - 19/03/2025
class ElegiblityForMarriage:
    def Elegible():
        print("Your Gender : ",gender)
        print("Your Age : ",age)
        if((gender == 'Male' and age > 21) or (gender == 'Female' and age > 18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")    
gender, age = input("Enter Your Gender: "), int(input("Enter Your Age: "))
ElegiblityForMarriage.Elegible()
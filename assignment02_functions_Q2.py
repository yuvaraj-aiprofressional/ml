#Title - Assignment-2- Functions - Q2
#Create a function that checks whether the given number is Odd or Even
#Author - Yuvaraj Rajendran
#Date - 19/03/2025
class OddEven:
    def OddEven():
        if((inputValue%2) == 0):
            print(inputValue," is Even number")
        else:
            print(inputValue," is Odd number")  

inputValue = int(input("Enter a number: "))
OddEven.OddEven()              
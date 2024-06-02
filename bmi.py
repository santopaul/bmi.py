#from pyfiglet import figlet_format
import os
import sys
#from colorama import Fore, Style
# try:
#     #banner creation
#     if sys.platform == "linux" or sys.platform == "linux2":
#         os.system("clear")
#     elif sys.platform == "win32":
#         os.system("cls")
#     elif sys.platform == "darwin":
#         os.system("clear")
#     print(Fore.BLUE + figlet_format("WELCOME MR.SANTO", font="banner"))
#     print(Style.RESET_ALL)
# except:
#     print("Banner Error!")

#colors used
blue='\033[94m'
red='\033[31m'
yellow='\033[93m'
lgreen='\033[92m'
clear='\033[0m'
pink='\033[95m'
bold='\033[01m'

#banner
print(blue+"""
 '##:::::'##:'########:'##::::::::'######:::'#######::'##::::'##:'########:     
 ##:'##: ##: ##.....:: ##:::::::'##... ##:'##.... ##: ###::'###: ##.....::     
 ##: ##: ##: ##::::::: ##::::::: ##:::..:: ##:::: ##: ####'####: ##:::::::     
 ##: ##: ##: ######::: ##::::::: ##::::::: ##:::: ##: ## ### ##: ######:::     
 ##: ##: ##: ##...:::: ##::::::: ##::::::: ##:::: ##: ##. #: ##: ##...::::     
 ##: ##: ##: ##::::::: ##::::::: ##::: ##: ##:::: ##: ##:.:: ##: ##:::::::     
. ###. ###:: ########: ########:. ######::. #######:: ##:::: ##: ########:     
:...::...:::........::........:::......::::.......:::..:::::..::........::     
'##::::'##:'########::::::::'######:::::'###::::'##::: ##:'########::'#######::
 ###::'###: ##.... ##::::::'##... ##:::'## ##::: ###:: ##:... ##..::'##.... ##:
 ####'####: ##:::: ##:::::: ##:::..:::'##:. ##:: ####: ##:::: ##:::: ##:::: ##:
 ## ### ##: ########:::::::. ######::'##:::. ##: ## ## ##:::: ##:::: ##:::: ##:
 ##. #: ##: ##.. ##:::::::::..... ##: #########: ##. ####:::: ##:::: ##:::: ##:
 ##:.:: ##: ##::. ##::'###:'##::: ##: ##.... ##: ##:. ###:::: ##:::: ##:::: ##:
 ##:::: ##: ##:::. ##: ###:. ######:: ##:::: ##: ##::. ##:::: ##::::. #######::
..:::::..::..:::::..::...:::......:::..:::::..::..::::..:::::..::::::.......:::
"""+clear)
#Intro to bmi calculation
print("Welcome to BMI Calculator!")
print("Enter the operation number that you want.")
print("1. Metric System.(Kgs, Meters)")
print("2. Imperial System.(Pounds, inches)")
print("3. Read about BMI")

try:
    #select operation number
    operation=int(input("\n Operation number: "))

    #function for calculation a/bsqr
    def bmi_calculation(a,b):
        bsqr=b*b
        res=float(a/bsqr)
        return res
    
    #taking values based on system and units
    if operation == 1:
        print("Metric System calculation selected!")
        global weight
        weight=float(input("Enter weight in Kgs: "))
        global heights
        height=float(input("Enter height in meters: "))
        global bmi
        bmi=bmi_calculation(weight,height)
    elif operation == 2:
        print("Imperial System calculation selected!")
        weight=float(input("Enter weight in Pounds: "))
        height=float(input("Enter height in inches: "))
        bmi=703*bmi_calculation(weight,height)
    elif operation == 3:  
        #Readmore section
        print(bold+"Body Mass Index (BMI): BMI is a tool proved to be useful for health care professionals in analyzing the risk for future cardiovascular, endocrine and other diseases such as: diabetes, arthritis, liver disease, several types of cancer (such as those of the breast, colon, and prostate), high blood pressure (hypertension), high cholesterol, sleep apnea, metabolic syndrome.")
        print("It is important to note that BMI can miss accuracy when it comes to adults who are pregnant, have high muscle mass, for children or elderly. Which is why this data alone can not be used to make any diagnosis."+clear)
    else:
        print(red + "Sorry invalid Input!"+clear)

except:
    print("Operation Number error!")
#Diagnostics
if (bmi<16):
    print(pink+"your bmi is: ",str(bmi)+clear)
    print(lgreen + "You're severely underweight."+clear)
elif (16<=bmi<=18.4):
    print(pink+"your bmi is: ",str(bmi)+clear)
    print(lgreen + "You're underweight."+clear)
elif (18.5<=bmi<=24.9):
    print(pink+"your bmi is: ",str(bmi)+clear)
    print(lgreen + "You're normal."+clear)
elif (25<=bmi<=29.9):
    print(pink+"your bmi is: ",str(bmi)+clear)
    print(red + "You're overweight."+clear)
elif (30<=bmi<=34.9):
    print(pink+"your bmi is: ",str(bmi)+clear)
    print(red + "You're moderately obese."+clear)
elif (35<=bmi<=39.9):
    print(pink+"your bmi is: ",str(bmi)+clear)
    print(red + "You're severely obese."+clear)
elif (bmi>=40):
    print(pink+"your bmi is: ",str(bmi)+clear)
    print(red + "You're morbidly obese."+clear)

print(yellow +bold+ "Thank you for using me. For more tools visit: https://santopaul.github.io/Santo/"+clear)

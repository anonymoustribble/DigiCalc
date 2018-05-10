"""
Project Name: DigiCalc Graphing Calculator
Created: 5/8/2018
Last Modified: 5/8/2018
Version: 0.01
"""
print("Welcome to DigiCalc...")
print("Initializing Startup...")

#################################
#IMPORT
#################################
import os
import time

#################################
#CONSTANTS
#################################


#################################
#VARIABLES
#################################
dataIn = ""
dataOut = ""

#################################
#FUNCTIONS
#################################
def calculate(data):
    answer = 0
    dataList = []
    temp = ""
    count = -1
    flag = False
    
    for i in data:
        flag = False
        count += 1
        if i == "+" or i == "-" or i == "*" or i == "/" or i == "^":
            dataList += i
            flag = True
            
        while True:
            if count == len(data) - 1 and flag != True:
                break
            elif str(data[count+1]).isdigit() and flag != True:
                temp += i
            else:
                dataList += str(temp)
                break

    print(dataList)
    
    
    return answer

###################################
os.system('cls')

while True:
    print(dataOut)
    dataIn = input("> ")

    if dataIn.startswith("graph"):
        #GRAPHING
        dataOut = "Function coming soon."

    elif dataIn.startswith("shutdown"):
        break
    
    elif dataIn.startswith("clear"):
        os.system('cls')
    
    else:
        
        dataOut = calculate(dataIn)

        
    

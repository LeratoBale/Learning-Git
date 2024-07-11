# Firstly I had to define the calculator function

def calculator():
    print("\n")
    
 # Had to put exception handling here as user can input a string instead of a number which would cause an error   
    try:
        num1 = float(input("Please enter the 1st number:")) # Had to use a float as user could input intergers to avoid errors 
        num2 = float(input("Please enter the 2nd number:"))
    except ValueError as ERROR:
        print(ERROR)
        print("\n Please input a valid number")
        return
    
    # User has to input operation they wanted and used elif function to counter if a desired operation is not input
    opp = input("Please input an operation: + - * /") 

    if opp == "+":
        ans = num1 + num2 

    elif opp == "-":
        ans = num1 - num2

    elif opp == "*":
        ans = num1 * num2

    # Exception Handling in case client divide with a zero  
    elif opp == "/":
        try:
            ans = num1/num2
        except ZeroDivisionError as Error:
            print("ERROR")
            print("Please divide with the correct number")
            return
    else:
        ans = "Invalid Operations"

    calc_answer = (str(num1) + " " + str(opp) + " " + str(num2) + " " + str("=") + " " + str(ans)+ "\n")

    file = open('equation.txt','a')
    file.write(calc_answer)

    print(calc_answer)
    file.close()

    another_calculation = input("Would you like to make another calculation? Y for Yes or N for No")

    if another_calculation == "N":
        print("Thank you for the calculation, See you next time!")
        exit()
            
    
# After defining the calculator function, I opened a text file to allow all the user input to be written into a txt file

# Coding the option the program is going to ask user what she want do on calculator app

choice = input("Please choose from these 3 option." + "\n" + "For calculator, please enter C" + "\n" + "For previous equations, please enter A" + "\n" +"To exit, please enter E")


if choice == "C":
    while True:
        calculator()
    
elif choice == "A":
    try:
        file = open("equation.txt", "r")
        print(file.read())
        file.close() #close the file
    except IOError:
        print("File does not exist")

elif choice == "E":
    print ("End to Calculator app")

else:
    print(" The input is invalid, Please choose the the correct option")



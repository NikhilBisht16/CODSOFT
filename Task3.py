import random                       # importing the random module  
  
# defining a function to randomly generate the password  
def generate_password(len):  
    "This function accepts a parameter 'len' and returns a randomly generated password"  
  
    # defining the list of characters that will be used to generate the password  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
  
    # using the random.sample() method to return a list of randomly selected characters from the list of characters.  
    selected_char = random.sample(list_of_chars, len)  
  
    # converting the list into the string  
    pass_str = "".join(selected_char)  
      
    # returning the generated password string  
    return pass_str  
  
# main function  
if __name__ == "__main__":  
    # creating an infinite loop  
    while True:  
        # asking user for their selection  
        userSelection = input("Do you wish to generate a Password?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")  
        # if the user does not want continue  
        if userSelection == 'N' or userSelection == 'n':  
            # printing a message  
            print("Thank You! See you next time.")  
  
            # breaking the loop  
            break  
  
        # if the user wants to continue  
        elif userSelection == 'Y' or userSelection == 'y':  
            # using the input() method to ask the user to input the length of the Password as integer  
            len = int(input("Enter the length of the Password: "))  
  
            # calling the generate_password() function and storing the returned value in a variable  
            pass_str = generate_password(len)  
  
            # printing the final result for the users  
            print("A randomly generated Password is:", pass_str)  
            print("") # one line spacing  
  
        # if the user enters wrong input  
        else:  
            # printing a message  y
            print("Invalid Input! Try Again.")  
            print("") # one line spacing  
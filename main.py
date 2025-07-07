
from read import display, display_supplier
from operation import buy, sell, add


'''----------------------------------------------Main Function--------------------------------------------------'''
#this is the main function that is displayed in the beginning
def main():
    """
    Summary: Displays the main menu and handles user choices and provides options to display, buy, sell,
        add products, and exit the program.

    Parameters: This function dosenot take any parameter.

    Returns: There is no return statement.
    """
    #wassssssup upakar
    condition = True
    while condition == True:
        try:
            #printing the header of main menu
            print("\n")
            print("="*80)
            print("\t\t\t\tWeCare Beauty Shop")
            print("\t\t\tPepsicola, Kathmandu | Contact: 999999999 ")
            print("-"*80)
            print("\t\tWelcome to WeCare Beauty Shop! Have a good day ahead!")
            print("="*80)
            print("\n")

            #Displaying the options
            print("What would you like to do?")
            print("1. Display Products")
            print("2. Buy Products")
            print("3. Sell Products")
            print("4. Add New Products")
            print("5. Exit")

            #asking user for the input
            choice = int(input("Please enter your choice: "))

            #if user chooses option 1 then display the table
            if(choice == 1):
                display()
                
            #if user chooses option 2 then buy function is called
            elif(choice == 2):
                buy()

            #if user chooses option 3 then sell function is called
            elif(choice == 3):
                sell()

            #if user chooses option 4 then add function is called
            elif(choice == 4):
                add()

            #if user chooses option 5 then exit the loop and print thank you
            elif(choice == 5):
                print("Thank you for visiting WeCare Beauty Shop!")
                break
                condition = False
                
            else:
                #incase of choice>5 or choice<1
                print("Invalid choice! Please try again.")

        except ValueError:
            #exceptional handling if the user input anything other than number
            print("Invalid Input! Please enter numbers only.")


#calling the main function
main()


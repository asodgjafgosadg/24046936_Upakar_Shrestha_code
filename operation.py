
from read import read,display_supplier,display
from write import write,buy_invoice,customer_invoice

'''---------------------------------------------Buy Function for admin------------------------------------------'''
#this function is used to buy products from suppliers (restocking)
def buy():
    """
    Summary: This function handles product restocking from suppliers by asking for supplier's name,products S.N.,
        quantities,and chnaging prices(optional). It also creates a supplier invoice with VAT.

    Parameters: This function takes no parameters.

    Returns: There is no return statement.
    """    
    #displaying buying product header
    print("\n")
    print("="*80)
    print("\t\t\t\tBuying Product")
    print("="*80)
    
    try:
        #Read the product file and store it in item_list
        item_list = read()

        # Check if item_list is empty
        if len(item_list) == 0:  
            print("No products available or error reading product file!")
            return

    except FileNotFoundError:
        print("File not found!!")

    #creating an empty list to store the items
    items = []
    
    #calling the function to display the supplier table
    display_supplier()

    name = input("\nEnter supplier name: ")
    
    while True:
        try:
            sn = int(input("\nEnter product S.N.: "))

            #check if the sn given by the user is valid or not
            if(sn < 1 or sn > len(item_list)):
                print("Invalid ID! Try again.")
                continue

            #storing the selected product detail in a dictionary
            product = item_list[sn-1]  
            print("\nSelected item: " + product['name'])
            print("\nCost price: "+str(product['price']))

            while True:
                    try:
                        #ask the user about the quantity
                        quantity = int(input("\nEnter the number of quantity: "))

                        #qunatity shoulod be positive
                        if quantity <= 0:
                            print("Enter a positive number!")
                            continue
                        break
                    except ValueError:
                        print("Invalid Input!")

            #if the user wants to change the price
            new_price = input("\nEnter a new cost price(click enter to keep current): ")

            # Checks if new_price is empty or not
            if(new_price != ""):  
                item_list[sn-1]['price'] = int(new_price)

            #adding product to the stock
            item_list[sn-1]['quantity'] += quantity

            #adding purchase details to items list
            items.append({'name':product['name'],'brand':product['brand'],'quantity': quantity,'price':
                          product['price']})

            print("\n"+str(quantity)+" "+product['name']+" added sucessfully.")

            while True:
                    #ask if the user wants more items
                    more = input("\nDo you want to buy more? (yes/no): ").lower()
                    if(more == "yes" or more == "y"):
                        display_supplier()  
                        break
                    elif(more == "no" or more == "n"):
                        #checks if the items list is empty or not
                        if len(items) > 0:
                            #calling the write function
                            write(item_list)
                            #calling the invoice function
                            buy_invoice(items,name)
                            print("\nRestocking completed!")
                        else:
                            print("\nNo items restocked.")
                        return  #exit function
                    else:
                        print("Please enter 'yes' or 'no'")

            
        except ValueError:
            print("Invalid Input! Please enter numbers only.")
        
'''-----------------------------------------Sell Function for Customers--------------------------------------------'''

#this function is used to sell products to customers
def sell():
    """
    Summary: This function handles product selling to customers by asking for customer's name,products S.N.,
        quantity,and also calculate free item(Buy 3 get 1 free). It also creates a customer invoice.

    Parameters: This function takes no parameters.

    Returns: There is no return statement.
    """ 
    
    #printing the selling product heading
    print("\n")
    print("="*80)
    print("\t\t\t\tSelling Product")
    print("="*80)

    try:
        #read the product file and store it in item_list
        item_list = read()

        # Check if item_list is empty
        if len(item_list) == 0:  
            print("No products available or error reading product file!")
            return

    except FileNotFoundError:
        print("File not found!!")

    #creating an empty list to store the items
    items = []

    #calling the function to display the table
    display()
    
    name = input("\nEnter customer name: ")

    while True:
        try:
            sn = int(input("\nEnter product S.N.: "))
            #check if the sn given by the user is valid or not
            if sn < 1 or sn > len(item_list):
                print("Invalid ID! Try again.")
                continue

            #storing the selected product detail in a dictionary
            product = item_list[sn - 1]
            print("\nSelected item: " + product['name'])
            print("\nSelling price: " + str(product['price'] * 2))
            print("\nAvailable: " + str(product['quantity']) + " units")

            while True:
                try:
                    #ask the user for the quantity
                    quantity = int(input("\nEnter the number of quantity to buy: "))
                    #quantity should be positive
                    if quantity <= 0:
                        print("Enter a positive number!")
                        continue

                    #when buy 3 get 1 free
                    free = quantity // 3
                    total = quantity + free

                    #checks if the product is avialbale in the stock
                    if total > product['quantity']:
                        print("Not enough stock!")
                        continue
                    break
                
                except ValueError:
                    print("Invalid Input!")

            #decrease the quantity in stock
            item_list[sn-1]['quantity'] -= total

            #adding the product detail to items list
            items.append({'name': product['name'], 'brand': product['brand'],'quantity': quantity,
                          'price': product['price'] * 2})

            print("\n" + str(quantity) + " " + product['name'] + " added successfully (" + str(free) + " free).")

            while True:
                #ask if the user wants to buy more
                more = input("\nDo you want to buy more? (yes/no): ").lower()
                if more == "yes" or more == "y":
                    display()
                    break
                elif more == "no" or more == "n":
                    #checks if the items list is empty or not
                    if len(items) > 0:
                        #calling the write function
                        write(item_list)
                        #calling invoice function
                        customer_invoice(items, name)
                        print("\nSelling completed!")
                    else:
                        print("\nNo items purchased.")
                    return
                else:
                    print("Please enter 'yes' or 'no'")

        except ValueError:
            print("Invalid Input! Please enter numbers only.")

'''-----------------------------------------Add new product Function for admin------------------------------'''
#this function is used to add new products from suppliers (restocking)
def add():
    """
    Summary: This function adds new product to the product.txt file by asking the user for the product details
        such as name,brand,quantity,price,country of origin.

    Parameters: This function takes no parameters.

    Returns: There is no return statement.
    """ 
    
    #displaying the add product heading
    print("\n")
    print("="*80)
    print("\t\t\t\tAdd New Product")
    print("="*80)

    #creating an empty dictionary
    new_item={}

    #reads the product file and store in item_list
    item_list = read()
    
    try:
        #ask the user for name and brand
        name = input("\nEnter product name: ")
        brand = input("\nEnter product brand: ")

        while True:
            try:
                #ask for quantity
                quantity = int(input("\nEnter quantity: "))
                #quantity is positive or not
                if quantity < 0:
                    print("Quantity can't be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer for quantity.")

        while True:
            try:
                #ask for price
                price = int(input("\nEnter price: "))
                #checks if price is positive
                if price < 0:
                    print("Price can't be negative.")
                    continue
                break
            except ValueError:
                print("Invalid Input!")

        #ask for the country of origin
        country = input("\nEnter country of origin: ")

        #creating the new product dictionary
        new_item = { 'name': name,'brand': brand,'quantity': quantity,'price': price,'country': country }

        #adding the new items to the item_list
        item_list.append(new_item)


        while True:
                #ask if the user wants to buy more
                more = input("\nDo you want to add more? (yes/no): ").lower()
                if more == "yes" or more == "y":
                    display()
                    break
                elif more == "no" or more == "n":
                    #checks if the item_list is empty or not
                    if len(item_list)>0:
                        write(item_list)
                        display_supplier()    
                    else:
                        print("\nFailed to add product!")
                    return
                else:
                    print("Please enter 'yes' or 'no'")
        

    except:
        print("Unexpected error")


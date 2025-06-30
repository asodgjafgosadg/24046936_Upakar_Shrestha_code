#importing datetime for bill
import datetime

'''---------------------------------------------Function to write to file------------------------------------------'''
def write(item_list):
    '''
    Summary: This function opens the product file in write mode and writes the product detail in the txt file.

    Parameters: This function takes item_list as parameter.
        item_list (list): List of product dictionaries

    Returns: There is no return statment.
    '''
        
    try:
        #opening the file in write mode
        file = open("product.txt", "w")
            
        for item in item_list:
            #writing the product data in the txt filter
            line = item['name']+","+item['brand']+","+str(item['quantity'])+","+str(item['price'])+","+item['country']
            file.write(line + "\n")

        #closes the file
        file.close()
            
    #error handling
    except:
        print("Error writing to product file!")


'''-------------------------------------------Invoice Function for Suppliers--------------------------------------'''
#this function prints the invoice in terminal and create a new txt file
def buy_invoice(items,name):
    '''
    Summary: This function creates a purchase invoice when buying products from suppliers which shows the supplier
            name,date,time of purchase,list of products and the total amount with VAT it also prints the invoice
            in terminal.

    Parameters: This function takes items list and the suppiler's name as parameters.
            items (list): Purchased products with details
            name (str): Supplier's name for invoice

    Returns: There is no return statment.
    '''

    total = 0
        
    #storing todays date in "date"
    date = datetime.datetime.now().date()
        
    #storing todays time in "time"
    time = datetime.datetime.now().time()
        
    #writing the file name in which the restock invoice will be saved as
    filename = "restock_" + name +".txt"

    try: 
        #Printing the invoice in the terminal
        print("\n")
        print("="*70)
        print("\n\tWeCare Wholesale Restock Invoice\n")
        print("="*70)
        print("Date: " + str(date))
        print("Time: " + str(time))
        print("Supplier Name: " + name)
        print("-" * 70)
        print("Product\t\t Brand\t   Quantity\tPrice\tAmount\n")
        print("-" * 70)

        #calculating and displaying the total for each item
        for item in items:
                amount = item['quantity'] * item['price']
                total += amount
                print(item['name']+"\t"+item['brand'] + "\t" + str(item['quantity']) + "\t " + str(item['price'])+
                          "\t " + str(amount) + "\n")
        #adding 13% vat
        vat = total * 0.13
        VAT_total = total + vat

        print("-" * 70)
        print("Total: " + str(total))
        print("VAT (13%): " + str(vat))
        print("Total with VAT: " + str(VAT_total))
        print("=" * 70)

    except:
        print("Unexpected error!")

    try:    
        #writing the invoice in txt file
        w=open(filename,"w")
        w.write("="*70)
        w.write("\n")
        w.write("\t\tWeCare Wholesale Restock\n")
        w.write("="*70)
        w.write("\n")
        w.write("Date: " + str(date))
        w.write("\n")
        w.write("Time: " + str(time))
        w.write("\n")
        w.write("Supplier Name: " + name)
        w.write("\n")
        w.write("-" *70)
        w.write("\n")
        w.write("Product\t\t Brand\t   Quantity\tPrice\tAmount\n")
        w.write("-" *70)
        w.write("\n")

        for item in items:
                amount = item['quantity'] * item['price']
                total += amount
                w.write(item['name'] +"\t"+item['brand'] + "\t" + str(item['quantity']) + "\t " + str(item['price'])+
                        "\t " + str(amount) + "\n")
        #adding vat
        vat = total * 0.13
        VAT_total = total + vat

        #writing the total with vat
        w.write("-" *70)
        w.write("\n")
        w.write("Total: " + str(total))
        w.write("\n")
        w.write("VAT (13%): " + str(vat))
        w.write("\n")
        w.write("Total with VAT: " + str(VAT_total))
        w.write("\n")
        w.write("=" *70)
        w.write("\n")
        w.close()
    #error handling
    except:
        print("Error writing to product file!")
        

'''-------------------------------------------Invoice Function for Customers--------------------------------------'''

#this function prints the customer invoice in terminal and creates a new txt file
def customer_invoice(items, name):
    '''
    Summary: This function creates a sales invoice when selling products to which shows the customer name,date and
            time of purchase,list of products and the total amount with VAT it also prints the invoice in terminal.

    Parameters: This function takes items list and the suppiler's name as parameters.
            items (list): Purchased products with details
            name (str): Customer's name for invoice

    Returns: There is no return statment.
    '''

    total = 0

    #storing todays date in "date"
    date = datetime.datetime.now().date()

    #storing todays time in "time"
    time = datetime.datetime.now().time()
        
    #writing the file name in which the customer invoice will be saved as
    filename = "invoice_" + name + ".txt"

    try:
        #printing the invoice in terminal
        print("\n")
        print("="*80)
        print("\n\t\tWeCare Customer Invoice\n")
        print("="*80)
        print("Date: " + str(date))
        print("Time: " + str(time))
        print("Customer Name: " + name)
        print("-" * 80)
        print("Product\t\tBrand\t Paid Quantity\tFree Quantity\tPrice\tAmount\n")
        print("-" * 80)

        #calculating the amount and free items
        for item in items:
            paid = item['quantity']
            #calculation free items 
            free = paid // 3 
            amount = paid * item['price']
            total += amount
            print(item['name'] + "\t" + item['brand'] + "\t" + str(int(paid)) +"\t\t" +str(int(free)) + "\t" +
                  str(item['price'])+ "\t" + str(amount) + "\n")

        print("-" * 80)
        print("Total Amount: " + str(total))
        print("=" *80)
        print("Thank you for shopping with us!")
        
    except:
        print("Unexpected error!")

    try:
        #writing the invoice in txt file
        w = open(filename, "w")
        w.write("="*80)
        w.write("\n")
        w.write("\t\t\tWeCare Customer Invoice\n")
        w.write("="*80)
        w.write("\n")
        w.write("Date: " + str(date))
        w.write("\n")
        w.write("Time: " + str(time))
        w.write("\n")
        w.write("Customer Name: " + name)
        w.write("\n")
        w.write("-" *80)
        w.write("\n")
        w.write("Product\t\t Brand\t Paid Quantity\tFree Quantity\tPrice\tAmount\n")
        w.write("-" *80)
        w.write("\n")

        #calculating the amount and free items
        for item in items:
            paid = item['quantity']
            free = paid // 3
            amount = paid * item['price']
            total += amount
            w.write(item['name'] + "\t" + item['brand'] + "\t" + str(int(paid)) +"\t\t" +str(int(free)) + "\t" +
                    str(item['price']) + "\t" + str(amount) + "\n")

        w.write("-" *80)
        w.write("\n")
        w.write("Total Amount: " + str(total))
        w.write("\n")
        w.write("=" *80)
        w.write("\n")
        w.write("Thank you for shopping with us!\n")
        w.close()
    
    except:
        print("Error writing to product file!")

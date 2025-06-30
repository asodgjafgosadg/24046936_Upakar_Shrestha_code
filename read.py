
'''---------------------------------------------Function to read from file------------------------------------------'''

def read():
    """
    Summary: This function reads product data from file and returns it as a list of dictionaries
             containing product details.

    Parameters: This function takes no parameters.

    Returns: This function returns item_list.
        item_list (list): List of product dictionaries with keys:
            - name (str): The name of product
            - brand (str): The brand of product
            - quantity (int): The quantity of product
            - price (int): The price of product
            - country (str): The country of origin of product
    """
    
    try:
        #opens the product file in read mode
        file = open("product.txt","r")

        #creating empty list
        item_list = []
        item={}
        
        #reads each line from the file
        for line in file:
            line = line.replace("\n","")
            item_data = line.split(",")

            #creating dictionary for each item
            item = {'name': item_data[0],'brand': item_data[1],'quantity': int(item_data[2]),'price': int(item_data[3]),
                    'country': item_data[4]}
            item_list.append(item)
        
        #closes the file
        file.close()
        return item_list
        
    except FileNotFoundError:
        print("File not found!")

'''-------------------------------------------Display Function for customers--------------------------------------'''
def display():
    """
    Summary: Displays products in a table for customers with selling prices 200% of cost price.

    Parameters: This function takes no parameters.

    Returns: There is no return statement.
    """
    
    try:
        print("\n")

        #reads the product file store in item_list
        item_list = read()
        
        #using a counter to increae the SN in the table
        c=1
        
        # Display product table with selling price
        print("="*80)
        print("S.N\tProduct Name\t Brand Name\tQuantity\tPrice\tCountry")
        print("="*80)    

        #printing each product
        for item in item_list:
            print(str(c) +"\t"+ item['name'] +"\t "+ item['brand'] +"\t "+ str(item['quantity']) +"\t\t"+
                  str(item['price']*2) + "\t"+ item['country'])
            c+=1
        print("="*80)
    except FileNotFoundError:
        print("File not found!")

'''-------------------------------------------Display Function for suppliers--------------------------------------'''

def display_supplier():
    """
    Summary: Displays products with product detail in a table.

    Parameters: This function takes no parameters.

    Returns: There is no return statement.
    """
    
    try:
        print("\n")

        #reads the product file store in item_list
        item_list = read()
        
        #using a counter to increae the SN in the table
        c=1
        
        # Display product table with selling price
        print("="*80)
        print("S.N\tProduct Name\t Brand Name\tQuantity\tPrice\tCountry")
        print("="*80)

        #printing each product
        for item in item_list:
            print(str(c) +"\t"+ item['name'] +"\t "+ item['brand'] +"\t "+ str(item['quantity']) +"\t\t"+
                  str(item['price']) + "\t"+ item['country'])
            c+=1
        print("="*80)
    except FileNotFoundError:
        print("File not found!")

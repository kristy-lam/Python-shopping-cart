""" This is an online shopping cart application for a pet related
products. Users are able to view, add and remove items from their 
cart, as well as determine the total cost of the items."""


# Item list and price list for the background
menu_items = ["dog food", "cat nips", "hair brush", "pet toys", "dog leash"]
menu_price = [3, 4, 7, 8, 6, 5]


# Print menu for users with index, item and price
print("\n\033[1mWelcome to Kristy's online pet supplies store!\033[0m\n")
print("Here's the menu -\n")
print("INDEX & ITEM" + "\tPRICE (£)")
for index in range(len(menu_items)):
    print(f"{(index + 1)} - {menu_items[index]}\t{menu_price[index]}")


# Define global variables before the loop
done = False
cart = []
quantity = []
price = []
total_price = 0


# Print update in shopping cart function
def print_updated_cart():
    if cart != []:
        print("\nIn your shopping cart -\n")
        print("INDEX & ITEM x QUANTITY" + "\t\tPRICE (£)")
        for cart_index in range(len(cart)):
            print(f"{cart_index + 1} - {cart[cart_index]} x " + 
                f"{quantity[cart_index]}\t\t{price[cart_index]}")
        print(f"Total price =\t£ {total_price}\n")
    else:
        print("\nYour shopping cart is empty.\n")


# While loop for continuous operation until check out
while not done:
    options = """
    Choose from the following options:\n
    a - Add an item to your shopping cart\n
    b - Amend quantity of an item in your shopping cart\n
    c - Remove an item from your shopping cart\n
    d - Clear your shopping cart\n
    e - Check out\n
    """
    print(options)
    user_input = input("Key in your choice: ").lower()
    
    
    # Option a: Add an item to shopping cart
    if user_input == "a":
        # Ask for index input
        index_input = int(input(
            "Input the index of the item you want: "))
        
        # If loop to prevent invalid index_input
        if 0 < index_input <= 5:
            # Find item using the index input
            item_input = menu_items[index_input - 1]
            # Find price from index input
            price_input = int(menu_price[index_input - 1])
            # Ask for quantity input
            quantity_input = int(input("Input the quantity: "))
            
            if quantity_input > 0:
                
                # If it is a new item not in the cart
                if item_input not in cart:
                    # Add new item to shopping cart list 
                    cart.append(item_input)
                    # Add quantity input to quantity list
                    quantity.append(quantity_input)
                    # Add price input to price list
                    price.append(price_input)
                    # Add price of item x quantity to total price
                    total_price += (price_input * quantity_input)
                    # Print update message
                    print(f"You have added \033[1m{item_input} x "
                        f"{quantity_input} \033[0m to your shopping "
                        f"cart.\n")
                    # Print update in shopping cart            
                    print_updated_cart()
                
                # If item already exists in the cart
                else:
                    # Define variable for index of quantity by item
                    quantity_index_by_item = cart.index(item_input)
                    # Add to existing quantity for same item
                    quantity[quantity_index_by_item] += quantity_input
                    # Add price of item x quantity to total price
                    total_price += (price_input * quantity_input)
                    # Print update message
                    print(f"You have added \033[1m{item_input} x "
                        f"{quantity_input} \033[0m to your shopping "
                        f"cart.\n")
                    # Print update in shopping cart            
                    print_updated_cart()
                                
            # Print result of adding 0 quantity
            elif quantity_input == 0:
                print("You did not add any item to the cart.")
            
            # Print error message for invalid input for quantity
            else:
                print("Invalid input, please try again!\n")
        
        # Print error message for invalid input
        # i.e. index input out of range
        else:
            print("No such item, please try again!\n")
            
    
    # Option b: Amend quantity of an item in shopping cart
    elif user_input == "b":
        
        # If the cart is not empty
        if cart != []:            
            # Ask for cart index input
            cart_index_input = int(input(
                "Input the index of the cart item you want to amend: "))
            
            # If cart index input is valid
            if (cart_index_input - 1) in range(len(cart)):
                # Find item using the cart index input
                cart_item_input = cart[cart_index_input - 1]
                # Find price from cart index input
                cart_price_input = int(price[cart_index_input - 1])
                # Find previous quantity from cart index input
                cart_quantity_input = int(quantity[cart_index_input - 1])
                # Ask for new quantity input
                new_quantity_input = int(input("Input the new quantity: "))
                            
                if new_quantity_input > 0:
                    # Replace previous quantity with new quantity
                    quantity[cart_index_input - 1] = new_quantity_input  
                    # Deduct price of item in previous quantity
                    total_price -= (cart_price_input * cart_quantity_input)
                    # Add price of item in new quantity 
                    total_price += (cart_price_input * new_quantity_input)
                    # Print update message
                    print(f"You now have \033[1m{cart_item_input} x " + 
                        f"{new_quantity_input}\033[0m in your shopping cart.\n")
                    # Print update in shopping cart            
                    print_updated_cart()
                
                elif new_quantity_input == 0:
                    # Remove selected item from cart
                    cart.remove(cart_item_input)
                    # Remove quantity of selected item from quantity list
                    quantity.remove(cart_quantity_input)
                    # Remove price of selected item from price list
                    price.remove(cart_price_input)
                    # Substract price of item x quantity from total price
                    total_price -= (cart_price_input * cart_quantity_input)
                    # Print update message
                    print(f"You have removed \033[1m all {cart_item_input}" +
                        f"\033[0m from your shopping cart.\n")
                    # Print update in shopping cart            
                    print_updated_cart()
                    
            # If cart index input is invalid i.e. out of range
            else:
                print("Invalid input, please try again!\n")
        
        # If the cart is empty
        else:
            print("\nYour shopping cart is empty. There is nothing " +
                  "to be amended.\n")

    
    # Option c: Remove an item from shopping cart         
    elif user_input == "c":
        
        # If the cart is not empty
        if cart != []:
            # Ask for art index input
            cart_index_input = int(input(
                "Input the index of the cart item you want to remove: "))
            
            # If cart index input is valid
            if (cart_index_input - 1) in range(len(cart)):
                # Find item using the cart index input
                cart_item_input = cart[cart_index_input - 1]
                # Find quantity from cart index input
                cart_quantity_input = int(quantity[cart_index_input - 1])
                # Find price from cart index input
                cart_price_input = int(price[cart_index_input - 1])
                # Remove selected item from cart
                cart.remove(cart_item_input)
                # Remove quantity of selected item from quantity list
                quantity.remove(cart_quantity_input)
                # Remove price of selected item from price list
                price.remove(cart_price_input)
                # Substract price of item x quantity from total price
                total_price -= (cart_price_input * cart_quantity_input)
                # Print update message
                print(f"You have removed \033[1mall {cart_item_input}" + 
                    f"\033[0m from your shopping cart.\n")
                # Print update in shopping cart            
                print_updated_cart()
            
            # If cart index input is invalid i.e. out of range
            else:
                print("Invalid input, please try again!\n")
        
        # If the cart is empty
        else:
            print("\nYour shopping cart is already empty.\n")
    
    # Option d: Clear shopping cart
    elif user_input == "d":
        cart.clear() # Remove all items from cart
        quantity.clear() # Remove all items from quantity list
        price.clear() # Remove all items from price list
        total_price = 0
        print("\nYour shopping cart is now empty.\n")

    # Option e: Check out        
    elif user_input == "e":
        
        # If the cart is not empty
        if cart != []:
            print("\nIn your shopping cart -\n")
            print("INDEX & ITEM x QUANTITY" + "\t\tPRICE (£)")
            for cart_index in range(len(cart)):
                print(f"{cart_index + 1} - {cart[cart_index]} x " +
                    f"{quantity[cart_index]}\t\t{price[cart_index]}")
            print(f"Total price =\t£{total_price}")
            print("\nPlease pay at the cashier. \033[1m" + 
                "Thank you and come back soon!\033[0m\n")
            done = True
        
        # If the cart is empty
        else:
            print("\nYour shopping cart is empty.\n")
        
    else:
        print("Invalid input, please try again!\n")

import time
import os
def clear_output():
    os.system("cls" if os.name == "nt" else 'clear')

class Cart():
    def __init__(self, customer_name):
        self.customer_name = customer_name.title()
        self.cart = {}

    
# Add items to cart
    def add_to_cart(self):
        item = input("What would you like to add to your cart? ")
        if item in self.cart:
            how_many = int((input(f"How many {item.title()} would you like to add? ")))
            self.cart[item]['how many'] += how_many
        else:
            price = float(input(f"What is the price of {item.title()}? "))
            how_many = int(input(f"How many {item.title()}(s) would you like to add? "))
            self.cart[item] = {'price':price, 'how many':how_many}
            clear_output()
            print(f'You have successfully added {self.cart[item]["how many"]} {item.title()}(s) to your cart! ')
            time.sleep(2)
            clear_output()

    # Remove items from cart

    def remove_from_cart(self):
        item = input("What would you like to remove from your cart? ")
        if item not in self.cart:
            clear_output()
            print(f"{item.title()} is not currently in your cart. Please check your spelling and try again.")
            time.sleep(5)
            clear_output()
        else:
            how_many = int((input(f"How many {item.title()}(s) would you like to remove? ")))
            self.cart[item]['how many'] -= how_many
            if self.cart[item]['how many'] <= 0:
                del self.cart[item]
            clear_output()
            print(f'You have {self.cart[item]["how many"]} {item.title()}(s) left in your cart.')
            time.sleep(2)
            clear_output()

    # Show current items in cart without total

    def view_cart(self):
        if self.cart == {}:
            print("Your cart is empty. :(")
            time.sleep(2)
            clear_output()
        else:
            print("Here is what you currently have in your cart:")
            for item, info in self.cart.items():
                print(f"\n{info['how many']} {item.title()}(s) for ${info['price']:.2f} each.")
            time.sleep(5)
            clear_output()

    # Clear cart of all items

    def clear_cart(self):
        if self.cart != {}:
            confirm = input("Please confirm you would like to clear your cart:\nYes or No ").lower()
            if confirm == 'yes':
                clear_output()
                self.cart.clear()
                print("You've successfully cleared your cart!")
                time.sleep(2)
                clear_output()
            else:
                clear_output()
                print("Ok, I've cancelled your clear request. Back to the beginning!")
                time.sleep(3)
                confirm == 'no'
                clear_output()
        else:
            clear_output()        
            print("Your cart is already empty.")
            time.sleep(3)
            clear_output()

    # Checkout with receipt
    def checkout(self):
        if self.cart != {}:
            print("------------------|-receipt-|------------------\nYour cashier's name is Kevin McClain\n")
            total = 0
            for item, info in self.cart.items():
                time
                print(f"{info['how many']} {item.title()}(s) for ${info['price']:.2f} each.\n")
                total += info['how many'] * info['price']
            print(f'Your total is ${total:.2f}.\n')
            print("Follow this link for a chance to win big!\n\nhttps://github.com/12mmhamdan\n\n------------------|-receipt-|------------------\n")
            
        else:
            print("You can't checkout. Your cart is empty.")
            welcome()

    # Welcome intro
def welcome():
    # name = input('Enter your name: ') put name as a parameter in cart = Cart(name)
    choices = {'add', 'remove', 'view', 'clear', 'checkout'}
    name = input('Enter your name: ')
    cart = Cart(name)
    clear_output()
    print(f"\nHi {name}! Welcome to the best local mart in town!")
    time.sleep(4)
    clear_output()
    while True:
        response = input("What action would you like to choose for your cart today? \n\nWould you like to: Add, Remove, View, Checkout or Clear? ").lower()
        if response in choices:
            if response == 'add':
                clear_output()
                cart.add_to_cart()
            elif response == 'remove':
                clear_output()
                cart.remove_from_cart()
            elif response == 'view':
                clear_output()
                cart.view_cart()
            elif response == 'clear':
                clear_output()
                cart.clear_cart()
            elif response == 'checkout':
                clear_output()
                cart.checkout()
                print(f"Thanks {name}! It was a pleasure doing business with you!")
                break
        else:
            clear_output()
            print(f"'{response.title()}' is not one of the available options.\nPlease select from {choices}.")
            time.sleep(6)
            clear_output()

welcome()
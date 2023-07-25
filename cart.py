# Using Python and the skills we learned over the past week, create a shopping cart program that will allow a user to add and remove items to a shopping cart. The cart should keep track of the quantity and price of each item.  The user should also be able to view the items that are currently in their cart. The user should be able to continue to add to, remove from, and view their cart until the user "quits" or "checks out". When the user quits/checks out, the program should display a receipt showing the items in the cart with quantity and price and the total price.
import os
import time

def clear_output():
    os.system("cls" if os.name == "nt" else 'clear')
class Cart():
    def __init__(self):
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
            print(f"{item.title()} is not currently in your cart. Please check your spelling and try again")
            time.sleep(4)
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

    # Show current cart without total
    def show_cart(self):
        if self.cart == {}:
            print("Your cart is empty. :(")
            time.sleep(2)
            clear_output()
        else:
            print("Here is what you currently have in your cart:")
            for item, info in self.cart.items():
                print(f"\n{info['how many']} {item.title()}(s) for ${info['price']:.2f} each.")
            time.sleep(4)
            clear_output()

    # Remove all items from cart
    def clear_cart(self):
        if self.cart != {}:
            confirm = input("Are you sure you want to clear cart?: \nYes or No: ").lower()
            if confirm == 'yes':
                clear_output()
                self.cart.clear()
                print("You've successfully cleared your cart!")
                time.sleep(3)
                clear_output()
            else:
                clear_output()
                print("Clearing cancelled: Returning back to options ")
                time.sleep(3)
                confirm == 'no'
                clear_output()

        else:
            print("Your cart is already empty.")
            time.sleep(3)
            clear_output()
            
# Checkout function
    def checkout(self):
        if self.cart != {}:
            print('--------------------------Receipt--------------------------\n')
            total = 0
            for item, info in self.cart.items():
                print(f"{info['how many']} {item.title()}(s) for ${info['price']:.2f} each.\n")
                total += info['how many'] * info['price']
            print(f'Your total is ${total:.2f}.\n')
        else:
            print("You can't checkout. Your cart is empty.")
            welcome()




# Welcome intro main function
def welcome():
    choices = ('add', 'remove', 'show', 'clear', 'checkout')
    cart = Cart()
    print("Hello, Welcome To The Best Local Mart!")
    time.sleep(3)
    clear_output()
    while True:
        response = input("Please choose what you would like to do with your cart. \nWould you like to: Add, Remove, Show, Checkout or Clear? ").lower()
        if response in choices:
            if response == 'add':
                clear_output()
                cart.add_to_cart()
            elif response == 'remove':
                clear_output()
                cart.remove_from_cart()
            elif response == 'show':
                clear_output()
                cart.show_cart()
            elif response == 'clear':
                clear_output()
                cart.clear_cart()
            elif response == 'checkout':
                clear_output()
                cart.checkout()
                print("It was a pleasure doing business with you! \n---------------------Have a Great Day!---------------------")
                break
        else:
            clear_output()
            print(f"{response} is not a valid selection, \nplease select from {choices}. ")
            time.sleep(4)
            clear_output()










# Running main function   
welcome()


























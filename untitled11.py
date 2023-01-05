# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:28:01 2023

@author: pulle
"""

from tkinter import *
root = Tk()
root.title("Dish")
root.geometry("600x600")
root.configure(bg="skyblue")

class parent():
    
        def __init__(self):
            print("This is the parent class.")
            
        def menu(dish):
            if dish=="burger":
                print("You can add the following toppings.")
                print("More Cheese | Add Jalapeno")
                    
            elif dish=="iced_americano":
                print("You can add the following flavoring.")
                print("Chocolate | Caramel")
                print("Choose a size.")
                print("Small | Medium | Large")
                        
            else:
                print("Sorry, This dish is not on our menu.")
                    
        def final_amount(dish, add_ons):
            if dish=="burger" and add_ons=="cheese":
                print("The total comes out to $8.50.")
            elif dish=="burger" and add_ons=="jalepeno":
                print("The total comes out to $8.50.")
            elif dish=="iced_americano" and add_ons=="chocolate" and add_ons=="small":
                print("The total comes out to $4.50")
            elif dish=="iced_americano" and add_ons=="chocolate" and add_ons=="medium":
                print("The total comes out to $5.50")
            elif dish=="iced_americano" and add_ons=="chocolate" and add_ons=="large":
                print("The total comes out to $7.00")
            elif dish=="iced_americano" and add_ons=="caramel" and add_ons=="small":
                print("The total comes out to $4.50")
            elif dish=="iced_americano" and add_ons=="caramel" and add_ons=="medium":
                print("The total comes out to $5.50")
            elif dish=="iced_americano" and add_ons=="caramel" and add_ons=="large":
                print("The total comes out to $7.00")
                
class child1(parent):
    
    def __init__(self,dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
       
class child2(parent):
    
    def __init__(self,dish):
        self.new_dish - dish
        self.addons = addons
        
    def get_final_ammount(self):
        parent.final_amount(self.new_dish, self.addons)
        
        
child1_object=child1("burger")
child1_object.get_menu()

child2_object=child2("burger","jalepeno")
child2_object.get_final_amount()

root.mainloop()
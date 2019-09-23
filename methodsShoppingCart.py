#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:45:54 2019

@author: bedlex
"""



class shopingCart():


    def __init__(self,items):
        self.items = items



    def add_to_cart(self):

        while True:
            item = input("Enter an item wich you wanna add: ")
            self.items[item] = input("Enter an price: ")
            answer = input("Do you want to add more items? ")
            if answer.lower() == "no":
                break


    def cart_items(self):
        for key, value in self.items.items():
            print ("item: {} price: $ {}".format(key, value))

    def remove_from_cart(self):

            while True:
                check = False
                answer = input("Enter an item wich you want to remove from cart \n ")
                for key in self.items.keys():
                    if answer.lower() == key:
                        check = True
                if check == True:
                    del self.items[answer]
                    break
                else:
                    print("You don't have this item in your cart")


    def clear_cart(self):
        answer = input("do you want to empty your cart? yes/no")
        if answer.lower() == "no":
            return
        else:
            self.items.clear()





def shop(cart):
    print("your shoping cart \n\n You can exit by type quit \n\n for check items in cart type: check \n\n for add item into your cart type: add \n")
    print (" for remove items in cart type: remove \n\n for clear your cart type: clear")
    while True:
        answer = input("so what you want to do? ")
        if answer.lower() == "quit":
             break
        elif answer.lower() == "check":
            cart.cart_items()
        elif answer.lower() == "add":
            cart.add_to_cart()
        elif answer.lower() == "remove":
            cart.remove_from_cart()
        elif answer.lower() == "clear":
             cart.clear_cart()
        else:
            print("We dont have this options")


cart = shopingCart({})
shop(cart)



#cart= shopingCart({})
#cart.add_to_cart()
#cart.cart_items()
#cart.remove_from_cart()
#cart.cart_items()
#print(cart.items)
#cart.clear_cart()
#print(cart.items)

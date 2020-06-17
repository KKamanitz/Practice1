# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:43:49 2020

@author: Kevin
"""

name = input ("Enter your name: ")
print ("Your name is " + name)
prompt = "Use this method when your request is more than one line long."
prompt += "\nEnter your favorite number: "
favoriteNumber = input (prompt)
print (favoriteNumber + " is a great number!")
number = input ("Enter a number greater than 3 and less than 8: ")
if number > 3 :
   print ("Your number is greater than 3.")
number = int(number)
if number > 3 :
    print ("Your number is more than 3.")
    if number < 8 :
        print ("Your number is less than 8.")
if (number > 3 and number < 8) :
    print ("Your number is BOTH greater than 3 AND less than 8.")
elif (number > 3 or number < 8) :
    print ("Your number is EITHER greater than 3 OR less than 8.")
letter = input ("Enter a letter: ")
if letter == "A" :
    print ("Statement 1")
    print ("Statement 2")
print ("Statement 3")

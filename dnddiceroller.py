import sys
import random
import math
import os

question = raw_input
attack = raw_input
"""d20 = random.randint(1,20)
d4 = random.randint(1,4)
d6 = random.randint(1,6)
d8 = random.randint(1,8)
d10 = random.randint(1,10)
d12 = random.randint(1,12)
d100 = random.randint(1,100)"""
x = 0

def attackroll():
    roll = raw_input("Roll! Press Enter")
    x = 0
    while x < 1:
    roll = random.randint(1,20)
	x += 1
	x1 = raw_input("Bonus? ")
	d = (int(roll))
	print roll, 'base', x1, 'Bonus'
	print (int(roll) + int(x1)), 'Total'
    print "*~" *30
    
    
    
def dicetype():
    
    num_dice = int(input("How many DICES did you want?: "))
    num_side = int(input("How many SIDED dice do you want?: "))
    x = 0
    while x < num_dice:
	roll = random.randint(1,num_side)
	x += 1
	d = (int(roll))
	print d
    print "*~" *30
    
def power():
    
    damage_time = raw_input("What dice? d4, d6 , d8 ,d10 ,d12, d100 ")
    
    if damage_time == "d10":
        x = 0 
        while x < 1:
            roll = random.randint(1,10)
            x += 1
            x1 = raw_input('Bonus? ')
            print roll, 'base', x1, 'Bonus'
	    print (int(roll) + int(x1)), 'Total'
        print "*~" *30 
        
    elif damage_time == "d12":
        x = 0 
        while x < 1:
            roll = random.randint(1,12)
            x += 1
            x1 = raw_input('Bonus? ')
            print roll, 'base', x1, 'Bonus'
	    print (int(roll) + int(x1)), 'Total'
        print "*~" *30 
        
    elif damage_time == "d8":
        x = 0 
        while x < 1:
            roll = random.randint(1,8)
            x += 1
            x1 = raw_input('Bonus? ')
            print roll, 'base', x1, 'Bonus'
	    print (int(roll) + int(x1)), 'Total'
        print "*~" *30 
        
    elif damage_time == "d6":
        x = 0 
        while x < 1:
            roll = random.randint(1,6)
            x += 1
            x1 = raw_input('Bonus? ')
            print roll, 'base', x1, 'Bonus'
	    print (int(roll) + int(x1)), 'Total'
        print "*~" *30 
       
    elif damage_time == 'd4':
        x = 0 
        while x < 1:
            roll = random.randint(1,4)
            x += 1
            x1 = raw_input('Bonus? ')
            print roll, 'base', x1, 'Bonus'
	    print (int(roll) + int(x1)), 'Total'
        print "*~" *30 
    
    elif damage_time == 'd100':
        print d100
        print "*~" *30
        
    
print "Welcome"
print "*~" *30

while question:
    question = raw_input("Business or Pleasure ")
    if question == "business":
        print "Okay, Lets do this"
        question = False
    elif question == "pleasure":
        print ".....okay...."
        print".....freak...."
        print"....what's wrong with you...."
        question = False
        
print "Let's start"
print "*~" *30


while attack:
    attack = raw_input("Attacking or Damage.  a for Attack roll or d for Damage or l for Dice ")
    if attack == 'a':
        print "*~" *30
        attackroll()
        
    elif attack == 'd':
        print "*~" *30
        power()
        
    elif attack == 'l':
        print "*~" *30
        dicetype()
    
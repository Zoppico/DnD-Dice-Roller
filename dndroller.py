import sys
import random
import math
import os
import ctypes

ans = True

#To make color text in Windows
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool
    
#Change this to change color

set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)

def startroller():            
	while ans:
		main_question = raw_input("Attack roll or pick dice? roll for attack roll or dice to pick dice ")
		print "*~" *30
		
		if main_question == 'roll':
			roll()
	
		elif main_question == 'dice':
			dice()
			
def dice():
	while ans:
			dice_number = raw_input("What dice? d4, d6, d8, d10, d12, d20 or d100 ")
			print '*~' *30
			if dice_number == "d4":
				print random.randint(1,4)
				startroller()
					
			elif dice_number == "d6":
				print random.randint(1,6)
				startroller()
				
			elif dice_number == "d8":
				print random.randint(1,8)
				startroller()
				
			elif dice_number == "d10":
				print random.randint(1,10)
				startroller()
				
			elif dice_number == "d12":
				print random.randint(1,12)
				startroller()
				
			elif dice_number == "d20":
				print random.randint(1,20)
				startroller()
				
			elif dice_number == "d100":
				print random.randint(1,100)
				startroller()					
							

def roll():
	while ans:
		rolling = raw_input("Roll! Press Enter or back to go back to the menu ")
		print "*~" *30
		if rolling == "":
			roll1 = random.randint(1,20)
			print roll1	
			x = input("Bouns? ")
			print (x + roll1)
			print "*~" *30
			go()
			
		elif rolling == "back":
			startroller()	
    
def go():
	
	while ans:
		question = raw_input("Did you hit? yes or no? ")
		
		if question == "yes":
			print "*~" *30
			print ("Damage Time")
			print "*~" *30
			power()
			
		elif question == "no":
			print ("Sorry")
			print "*~" * 30
			roll()
       
def power():
    while ans:
        damage_time = raw_input("What dice? d4, d6, d8, d10 or d12 ")
    
        if damage_time == "d10":
            rolld10 = random.randint(1,10)
            print rolld10
            xd10 = input("Bouns? ")
            print (xd10 + rolld10)
            print "*~" *30	
            roll()
            
        elif damage_time == "d8":
            rolld8 = random.randint(1,8)
            print rolld8
            xd8 = input("Bonus? ")
            print (xd8 + rolld8)
            print "*~" *30
            roll()
            
        elif damage_time == "d6":
            print random.randint(1,6)
            print "*~" *30
            more = raw_input("More? yes or no ")
            if more == "yes":
				print random.randint(1,6)
            elif more == "no":
				print "*~" *30 
				roll()   
            roll()
            
        elif damage_time == "d12":
            rolld12 = random.randint(1,8)
            print rolld12
            xd12 = input("Bonus? ")
            print (xd12 + rolld12)
            print "*~" *30
            roll()
            
        elif damage_time == "d4":
            rolld4 = random.randint(1,4)
            print rolld4
            xd4 = input("Bonus? ")
            print (xd4 + rolld4)
            print "*~" *30
            roll()
            
        elif damage_time =="":
            print "*~" *30
            print "restarting round"
            print "*~" *30
            roll()
            
startroller()

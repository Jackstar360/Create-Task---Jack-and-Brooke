#Requirements:
#user input
#function w/ params, conditional, and loop
#list or dictionary
import time
import sys
import random

#counts up to a number, used to show how much you won
def countUpTo(desired_amount, color):
    current_number = 0
    sleep = 0.1
    while current_number < desired_amount:
        print(f"{color}{' $'}{current_number}{reset}", end='\r')
        current_number += 1
        sleep -= 0.001
        sleep = max(sleep, 0.001)
        time.sleep(sleep)
    print(f"{color}{' $'}{current_number}{reset}")

#deletes lines and moves the cursor up
def delete_lines(length):
    for i in range(length):
        sys.stdout.write('\x1b[1A')  
        sys.stdout.write('\r')        
        sys.stdout.write(' ' * 120)
        sys.stdout.write('\r')

#typewriter effect
def typewriter_effect(phrase, color):
    # Loop through each character in the sentence
    for char in phrase:
        
        print(f"{color}{char}", end='', flush=True)
        time.sleep(0.05)
    print(reset)

def typewriter_effect2(phrase1, phrase2, color):
    for char in phrase1:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    for char in phrase2:
        print(f"{color}{char}{reset}", end='', flush=True)
        time.sleep(0.05)
    print(reset)
    
def typewriter_effect3(phrase1, phrase2, phrase3, color):
    for char in str(phrase1):
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    for char in str(phrase2):
        print(f"{color}{char}", end='', flush=True)
        time.sleep(0.05)
    
    for char in str(phrase3):
        print(f"{reset}{char}", end='', flush=True)
        time.sleep(0.05)
    print(reset)

def typewriter_effect4(phrase1, phrase2, color):
    for char in phrase1:
        print(f"{color}{char}{reset}", end='', flush=True)
        time.sleep(0.05)
    
    for char in phrase2:
        print(f"{color}{char}{reset}", end='', flush=True)
        time.sleep(0.05)
    print(reset)
#Colorer function
def colorize(text, color):
    print(f'{color}{text}{reset}')

#random lines for when you use an item
class cLines:
    whippedCream = ["you still feel empty","it fills you with Determination","you can feel it evaporate before even reaching your stomach","and leave none for the next person!","it's just what you need to heal the open wounds"]
    toyMouse = ["and begin swinging it around like a maniac","you opponent seemed to get quite excited","it reminds you that you forgot to eat lunch","you wonder if this will actually be an effective weapon"]
    cardboardBox = ["it makes you feel safe","your opponent seems jealous","it would be a pretty fun rocket ship","its more comfortable than any bed","it makes you feel a little sleepy"]
    scratchingPost = ["it reminds you of your favorite curtains","it makes you feel unnaturally strong","your opponent seems worried","you have so much fun you almost forgot you were fighting","your claws glisten in the light"]
    
#Pawl's powers
pawlPower = ["pity", "tired", "hungry", "nap", "sneeeze"]

#Player Stats
class ps:
    hp = float(5.0) #health points
    maxhp = float(5.0)
    atk = float(1.0) #attack damage
    prot = float(0.05) #armor multiplier
    oprot = float(0.05)
    cash = 0 #money
    tm = False #toy mouse equipped
    cb = False #cardboard box equipped
    wpLvl = 1 #level of current weapon
    td = False #turn finished
#Opponent's Stats
class cs:
    name = "Catrick"
    hp = float(4.0)
    maxhp = 4.0 #highest health points allowed
    atk = float(0.8)
    prot = float(0)
    oprot = float(0)
    payout = 40 #money for winning
    charge = -1
class js:
    name = "Jessicat"
    hp = float(5.0)
    maxhp = 5.0
    atk = float(1.0)
    prot = float(0.1)
    oprot = float(0.1)
    payout = 70
    charge = -1
class ms:
    name = "Mattmew"
    hp = 5.5
    maxhp = 5.5
    atk = 1.2
    prot = 0.2
    oprot = 0.2
    payout = 100
    charge = 2
class ts:
    name = "Tabbytha"
    hp = 4.0
    maxhp = 4.0
    atk = 1
    prot = 0
    oprot = 0
    payout = 150
    charge = -1
class ccs:
    name = "Cleocatra"
    hp = 7.0
    maxhp = 7.0
    atk = 1.5
    prot = 0.3
    oprot = 0.3
    payout = 200
    charge = 4
class ls:
    name = "Pawl"
    hp = 15.0
    maxhp = 15
    atk = 0.3
    prot = 0.3
    oprot = 0.3
    payout = 400
    charge = 2
pawlNap = False
class mcs:
    name = "Mewlious Caesar"

#Global variables for buying from Boe
tms = False
cbbs = False
bleh = "g"

#opponents list
fighters = [cs, js, ms, ts, ccs, ls, mcs]
roster = [cs, js, ms, ts, ccs, ls, mcs]

#player's inventory
inventory = {
    "Whipped Cream":0, #heals
    "String":0, 
    "Toy Mouse":0, #offensive Item
    "Cardboard Box": 0, #defensive item
    "Scratching Post":0, #bonus atk
    "Ball of Yarn":0, #distracts opponent for a turn, resets charges
    "Catnip":0, #heals + bonus atk
    "Bullets":0, #ammo for gun
    "Gun":0, #strongest offensive item, requires bullets
    "Stripped Tophat":0, #strongest defensive item + bonus atk
    } 
#used when retrying after dying
invSave = {}
#shop layout
items = ["Whipped Cream","String","Toy Mouse","Cardboard Box","Scratching Post","Ball of Yarn","Catnip","Bullets","Gun","Stripped Tophat"]
#used for displaying inventory
playerInv = []

#Logo
print ("""⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀
⠀⠀⢸⠈⠙⢷⡄⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⡇⠀⠀
⠀⠀⠁⠀⠀⠀⠙⠋⠉⠉⠉⠉⠙⠋⠀⠀⠀⠀⠀⠀
⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀
⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀
⠀⡎⠀⠑⣦⣤⣀⠀⢀⠀⠀⡀⢀⣀⣤⣴⠀⠀⢹⠀
⢀⣇⡀⠀⠹⣯⣻⡽⠁⠀⠀⠉⢿⣯⣼⠟⠀⢀⣸⡀
⠠⢷⠚⢽⣵⣶⣆⠀⠀⢻⡞⠀⠀⣰⣶⣮⠯⠶⡼⠄
⠀⠊⣯⡽⠛⠉⠉⠒⠂⠉⠉⠒⠒⠉⠉⠙⠻⣽⠑⠀
⠀⠀⠀⠉⠲⣤⣀⡀⠀⠀⠀⠀⣀⣀⣤⡴⠎⠀⠁⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠛⠋⠉⠉⠉⠁⠀⠀⠀⠀""")

#Text colors
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
bright_black = "\033[90m"
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"
reset = "\033[0m"

#Title
colorize("""
 ██ ▄█▀ ██▓▄▄▄█████▓▄▄▄█████▓▓██   ██▓    ██ ▄█▀ ▒█████   ███▄ ▄███▓ ▄▄▄▄    ▄▄▄     ▄▄▄█████▓
 ██▄█▒ ▓██▒▓  ██▒ ▓▒▓  ██▒ ▓▒ ▒██  ██▒    ██▄█▒ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▒████▄   ▓  ██▒ ▓▒
▓███▄░ ▒██▒▒ ▓██░ ▒░▒ ▓██░ ▒░  ▒██ ██░   ▓███▄░ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░
▓██ █▄ ░██░░ ▓██▓ ░ ░ ▓██▓ ░   ░ ▐██▓░   ▓██ █▄ ▒██   ██░▒██    ▒██ ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ 
▒██▒ █▄░██░  ▒██▒ ░   ▒██▒ ░   ░ ██▒▓░   ▒██▒ █▄░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ 
▒ ▒▒ ▓▒░▓    ▒ ░░     ▒ ░░      ██▒▒▒    ▒ ▒▒ ▓▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   
░ ░▒ ▒░ ▒ ░    ░        ░     ▓██ ░▒░    ░ ░▒ ▒░  ░ ▒ ▒░ ░  ░      ░▒░▒   ░   ▒   ▒▒ ░   ░    
░ ░░ ░  ▒ ░  ░        ░       ▒ ▒ ░░     ░ ░░ ░ ░ ░ ░ ▒  ░      ░    ░    ░   ░   ▒    ░      
░  ░    ░                     ░ ░        ░  ░       ░ ░         ░    ░            ░  ░        
                              ░ ░                                         ░                   
""", red)
print("")

#checks if the invetory is empty
def invEmpty():
    tempInv = 0
    for i in inventory.values():
        if int(i) >= 1:
            tempInv += 1
    if tempInv == 0:
        return True
    
    else:
        return False
    
#displays the healthbar for opponents
def healthbar():
    if fighters[0].hp <= 0:
        print("""⢠⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 1/16):
        print("""⢠⣶⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 2/16):
        print("""⢠⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 3/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 4/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 5/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 6/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 7/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 8/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 9/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 10/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 11/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 12/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 13/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 14/16):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp < fighters[0].maxhp:
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠾⠿⠃""")
    elif fighters[0].hp == fighters[0].maxhp:
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠃""")
    else:
        print(fighters[0].hp)
        
#displays player inventory
def inventoryUi():
    healthbar()
    inv = ["empty"]
    invLoc = 0
    invLoc2 = 0
    if invEmpty() == False:
        inv.remove("empty")
        for i in inventory:
            if inventory[i] != 0:
                playerInv.append(items[invLoc])
                invLoc2 = invLoc2 + 1
                if inventory.get(i) >= 2:
                    inv.append(str(invLoc2) + (") ") + i + (" x") + str(inventory.get(i)))
                else:
                    inv.append(str(invLoc2) + (") ") + i)
                if invLoc == 9:
                    break
            invLoc = invLoc + 1
    ps.hp = round(ps.hp, 2)
    hpclr = green
    if ps.hp <= (ps.maxhp * 1/5):
        hpclr = red
    elif ps.hp <= (ps.maxhp * 2.5/5):
        hpclr = bright_yellow
    print(f"{'Health: ' + hpclr + str(ps.hp) + reset}{'  Cash: ' + green + '$' + str(int(round(ps.cash))) + reset}")
    print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    print(inv)
    print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")

#checks if the player or opponent is dead
def death():
    global fighters
    if ps.hp <= 0:
        typewriter_effect("You Died", bright_red)
        playAgain = input("Try Again or Give Up [t/g]")
        if playAgain == "t":
            delete_lines(100)
            ps.hp = ps.maxhp
            fighters[0].hp = fighters[0].maxhp
            inventory.update(invSave)
            fight(fighters[0])
        if playAgain == "g":
            delete_lines(100)
            ps.maxhp = 5.0
            ps.hp = ps.maxhp
            ps.cash = 0
            fighters = roster.copy()
            fight(fighters[0])
    if fighters[0].hp <= 0 and ps.hp > 0:
        typewriter_effect("You Won!", bright_yellow)
        prize = (fighters[0].payout * ps.hp)
        ps.cash += prize
        ps.cash = round(ps.cash)
        countUpTo(prize, bright_green)
        fighters.pop(0)
        time.sleep(2)
        ps.hp = ps.maxhp
        shop()

#calculates damage
def damage(atk, per):
    sign = random.randint(1, 2)
    multiplier = round(random.uniform(0.00, 0.50), 2)
    if sign == 1:
        critAtk = (atk - multiplier)
    else:
        critAtk = (atk + multiplier)
    critAtk = (critAtk - (critAtk * per))
    if critAtk < 0:
        critAtk = 0
    float(critAtk)
    critAtk = round(critAtk, 2)
    return(critAtk)

#function to use items
def item(menuSelected):
    global bleh
    x = (int(menuSelected) - 1)
    it = playerInv[x]
    #checks if the player has the item and can use it
    if it == "Whipped Cream" and ps.hp < ps.maxhp:
        ps.hp += 1
        if ps.hp >= ps.maxhp:
            ps.hp = ps.maxhp
        inventory["Whipped Cream"] -= 1
        delete_lines(11)
        inventoryUi()
        typewriter_effect4("You guzzle the airy white foam, ", random.choices(cLines.whippedCream), yellow)
        time.sleep(2)
        delete_lines(1)
    #what is displayed if they cant
    elif it == "Whipped Cream" and ps.hp >= ps.hp:
        delete_lines(1)
        typewriter_effect("Your health is full", green)
        time.sleep(1)
        delete_lines(4)  
    elif it == "Toy Mouse":
        ps.tm = True
        inventory["Toy Mouse"] -= 1
        delete_lines(11)
        inventoryUi()
        typewriter_effect4("You reveal a rubbery toy of a gray mouse, ", random.choices(cLines.toyMouse), yellow)
        time.sleep(2)
        delete_lines(1)
    elif it == "Cardboard Box":
        ps.cb = True
        ps.prot += 0.2
        inventory["Cardboard Box"] -= 1
        delete_lines(11)
        inventoryUi()
        typewriter_effect4("You sit in a cardboard box, ", random.choices(cLines.cardboardBox), yellow)
        time.sleep(2)
        delete_lines(1)
    elif it == "Scratching Post":
        ps.atk = ps.atk * 2
        scpos = True
        inventory["Sratching Post"] -= 1
        delete_lines(11)
        inventoryUi()
        typewriter_effect4("You ferociously scratch a clearly beat up pole covered in carpet, ", random.choices(cLines.scratchingPost), yellow)
        time.sleep(2)
        delete_lines(1)
    elif it == "Ball of Yarn":
        inventory["Ball of Yarn"] -= 1
        delete_lines(11)
        inventoryUi()
        

        
    #Lets the player do things after using an item
    td2 = False
    while td2 == False:
        colorize("""Press [a] to Attack
Press [d] to Defend
Press [1-10] to select Items""", bright_cyan)
        menuSelect = input()
        bleh = menuSelect
        #player's attack
        if menuSelect == "a":
            delete_lines(11)
            dmg = damage(ps.atk, fighters[0].prot)
            if ps.tm == True:
                dmg += (0.25 + ps.wpLvl * 0.25)
            dmg = round(dmg, 2)
            fighters[0].hp = fighters[0].hp - dmg
            typewriter_effect3("You dealt ", str(dmg), " damage", red)
            td2 = True
            ps.td = True
            if scpos == True:
                scpos = False
                ps.dmg = ps.dmg/2
        #player's block
        elif menuSelect == "d":
            delete_lines(11)
            typewriter_effect2("You ", "Blocked", black)
            ps.prot += 0.6
            td2 = True
            ps.td = True
        #using another item
        elif menuSelect == "1" or menuSelect == "2" or menuSelect == "3" or menuSelect == "4" or menuSelect == "5" or menuSelect == "6" or menuSelect == "7" or menuSelect == "8" or menuSelect == "9" or menuSelect == "0":
            item(menuSelect)
        #if they accidentally press a wrong button
        else:
            print("error: unknown input")
            time.sleep(1.5)
            delete_lines(4)


#runs the main game, displays your opponent, lets both sides take their turn
def fight(opponent):
    global bleh
    global pawlNap
    #makes sure no one is already dead
    if ps.hp <= 0 or fighters[0].hp <= 0:
        death()
        return
    m = 2
    #makes sure everything is reset from the last round
    nprot = ps.prot
    oprot = fighters[0].prot
    #displays opponent
    if opponent == cs:
        print("""

              
⠀⠀⠀⢻⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠂⠀⠀
⠀⠀⠀⢸⣼⣙⣯⡉⠓⠒⠶⠤⣤⠶⠚⠉⠁⢀⡄⠀⢠⣤⠈⠉⠑⠲⢤⡤⠴⠖⠒⠉⣩⡾⢫⢸⠀⠀⠀
⠀⠀⠀⠸⣿⡻⣌⢻⣄⠀⣠⠆⠀⠀⠀⢀⣴⠋⢿⡆⢸⡇⢻⣦⡀⠀⠀⢶⣦⠀⢀⣼⠏⡤⣸⡞⠀⠀⠀
⠀⠀⠀⠀⢯⣧⠾⣿⣿⣷⢳⠃⠀⣠⣾⠋⠀⠀⠀⠘⠟⠀⠀⠈⠻⣆⠀⠈⢫⢳⣿⢳⣿⣇⣷⡇⠀⠀⠀
⠀⠀⠀⠀⠸⡽⣞⣿⣷⡇⡎⠀⠈⢁⣀⠤⢖⣊⣉⣛⣋⣁⡒⠦⢤⣀⣀⡀⠈⣧⢿⣾⣿⣿⡾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣽⣿⣿⣸⣗⡿⢚⣭⣶⣿⣿⠿⠿⠿⠿⢿⣿⣿⣷⣦⣝⠻⣷⣿⣸⣿⣿⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣡⣶⣿⡿⠟⠉⠁⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⣷⣦⣙⣟⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⠛⠛⠋⠁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢻⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠐⣞⠛⢉⡠⠴⢾⣿⢿⣿⣿⣦⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣷⠶⢤⣀⠙⢻⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠠⣴⣾⡥⠖⠋⠀⠀⠈⠛⠮⣧⣤⣿⠆⠀⠀⠀⠈⠿⢤⣤⣿⠞⠋⠀⠀⠸⣷⢬⣿⣦⡄⠀⠀⠀
⠀⠀⠀⠀⠈⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⠉⠀⠀⠀⠀
⠀⠀⠀⠘⠿⣿⠆⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠙⢿⣿⣿⠟⠀⠀⠠⡄⠀⠀⠀⠀⠀⠈⠲⣿⡿⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢹⡄⠀⠀⣤⣤⠴⢾⣀⠀⠀⠀⢤⣿⣣⣤⠀⠀⣀⣹⠶⣤⣤⣀⠀⠀⡼⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣤⣀⣠⡴⠞⣻⡷⣦⡴⠛⠉⠀⠉⠛⠶⣴⢾⣟⠻⢶⣄⣍⣩⠞⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⢿⣇⡀⠘⠋⠀⠉⠙⠶⠄⠀⠀⠰⠊⠉⠀⠉⠣⠀⣼⡟⣿⡷⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⣷⣤⡀⣄⠀⣴⢆⠀⠀⠀⡴⡄⠀⣠⢀⣤⣾⣿⣇⡀⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣷⣾⣦⣸⣾⣧⠀⣸⣷⣯⣾⣷⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀
⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀     
   ____      _        _      _    
  / ___|__ _| |_ _ __(_) ___| | __
 | |   / _` | __| '__| |/ __| |/ /
 | |__| (_| | |_| |  | | (__|   < 
  \____\__,_|\__|_|  |_|\___|_|\_\ """)
    elif opponent == js:
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣞⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠉⠳⡤⣀⠀⠀⣀⣀⡀⠀⣀⣀⡀⠀⣀⡠⡴⠛⠁⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⢈⡆⠉⠉⠁⠀⠀⠀⠀⠀⠉⠉⢁⡞⠀⠀⡀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣰⢁⣀⢩⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⢨⣿⡀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢉⣪⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⡄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠓⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠹⣿⣿⣿⡄⠀⠀⠀⠠⢫⡟⢿⢻⠏⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⠀⠀⠀⠈⠁⠉⠋⠀⠀⠀⠀⠈⠉⠀⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⣴⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠿⡿⠀⣀⠤⠀⠀⠀⠀⠀⠀⢹⡏⠄⡀⠤⠄⡐⠤⢤⣀⠀⠘⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢾⣿⡯⡫⡠⣿⣿⣷⣤⡀⠐⠁⠐⠊⠉⠈⠑⠂⠙⢮⣤⣾⣿⣟⢻⠠⡀⠙⢿⡷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠡⠊⠐⠅⣿⣿⣿⣿⣿⣷⣶⣦⣄⣀⣀⣤⣶⣿⡿⠿⣿⣿⢙⣿⠒⡌⠄⠀⠝⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡡⠊⠀⡠⡞⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⠟⠁⠀⠘⠤⢀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠈⠀⠠⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠟⠁⠀⠀⠀⠀⠀⠀⡗⠢⠄⣘⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⢀⡤⠒⡀⠀⠀⠈⠂⢘⠻⣿⣿⣿⣿⣿⣿⣋⣤⣴⠿⠃⠀⠀⠀⠀⠀⠀⣀⠔⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢠⣣⣿⣿⣷⡀⠀⠀⠀⠀⠁⠂⠙⠿⠿⠿⠿⠛⠉⠀⠀⠀⢀⠂⠀⣠⣴⠿⣿⣷⣄⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣰⠀⢸⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⣡⡶⠟⢹⠁⣰⡱⠙⢯⡆⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣇⠆⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⣰⠃⢠⣿⠁⠀⠘⣾⠀⡸⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣷⣶⣦⣤⡤⠴⢒⣿⠟⠁⠀⠀⡰⢡⣴⣾⣿⠀⠀⠀⢳⣴⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⠇⠘⣿⣿⣿⡛⢿⣿⣷⣄⣀⡤⠖⠉⠀⠀⠀⣠⠟⠀⢸⣿⣿⣿⣇⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
      _               _           _   
     | | ___  ___ ___(_) ___ __ _| |_ 
  _  | |/ _ \/ __/ __| |/ __/ _` | __|
 | |_| |  __/\__ \__ \ | (_| (_| | |_ 
  \___/ \___||___/___/_|\___\__,_|\__|                              """)
    elif opponent == ms:
        print("""
              
⠀⠀⣦⠚⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⡇⣇⠀⠀⠀⠀
⠀⠀⡟⠀⠻⣿⣷⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⢶⠀⠀⣳⡻⣿⣿⣯⣫⡷⣶⣤⣀⣀⣤⣤⣶⢾⣵⣤⣤⣤⣤⣦⣶⣿⣿⠋⣻⣿⣿⣿⣿⣿⡀⠄⠀⠀
⠀⠀⡾⣀⢰⡜⢾⣯⣭⣛⣿⠿⣕⠻⢿⣻⣿⠿⠿⡹⠝⢿⣿⢿⣿⣿⣿⣿⣁⣼⣿⣟⣿⣿⣿⡏⢀⠔⠀⠀
⠀⠀⠹⣣⢫⣷⣶⣿⣛⣷⡮⠵⣪⣿⣆⠙⠁⠀⠀⠀⠀⢂⠌⣿⣼⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣟⡁⠀⠀⠀
⠀⠀⠀⣿⣽⣿⢿⣿⣿⡴⣒⣼⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠈⡬⠻⣿⣿⢿⣿⣭⣿⣿⣿⡃⠀⠀⠀⠀
⠀⠀⠀⠈⢿⢟⣷⣿⣿⣷⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡓⢁⣾⡟⣡⡿⢿⣿⣿⣿⣏⠀⠐⠀⠀⠀
⠀⠀⠀⠀⠻⣷⣐⣿⡟⠋⠀⢰⡿⠻⢖⢶⠦⣄⡀⠁⠀⠀⣐⡈⠀⣐⣿⣾⣯⣤⣸⣿⣿⣿⠋⠡⠀⠀⠀⠀
⠀⠀⠀⢄⠀⠘⠛⠋⠀⠀⠀⠀⠹⣧⠀⢠⣶⠀⠹⣿⣦⣤⣾⢆⣌⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⡱⠄⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⡤⣤⣤⣾⣿⢿⢿⣿⣿⣷⣅⣿⣿⣿⣿⣿⣿⣿⡥⠀⠀⠀⠀⠀
⠀⠀⠀⠱⡶⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠙⠻⡉⠀⢀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⢈⣫⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠀⠀⢆⡀⢀⣑⣘⣯⠻⡛⢿⣿⣻⣿⣿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠛⣓⢊⡻⣵⢄⡀⠀⣀⠀⠠⠎⠀⣐⠠⠀⠀⠻⢿⣽⡿⠋⠀⣿⣿⣻⣿⡫⠟⠒⠒⠠⠄⢉⡁
⠀⠀⠀⠀⠐⣺⣯⣦⣖⡾⠛⢯⣖⣤⡴⢓⣢⢤⡶⠢⢀⣠⢴⣾⣏⠀⠀⣾⣷⣴⡦⢞⡁⠄⠁⠐⠂⠤⡀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣷⣴⣎⠭⣶⢿⣯⣍⠓⢶⠷⠗⠋⢽⢿⣿⣿⣦⣼⠿⣋⠐⢕⠤⡑⠢⢀⠀⠀⠀⠁
⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣻⣿⣿⣶⣤⣀⣤⣾⣾⣿⡿⠋⠁⠀⠡⡱⡈⠂⠈⠢⡀⠑⢄⠀⠀
⠀⠀⣴⣿⣿⢿⢿⣿⣟⠷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠐⠄⠀⠑⠄
⢠⣾⣿⡿⠃⠠⢎⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠀⠀⠈⠄⠀⠀
⣿⣿⣿⣿⣿⣶⢿⣥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣼⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  __  __       _   _                           
 |  \/  | __ _| |_| |_ _ __ ___   _____      __
 | |\/| |/ _` | __| __| '_ ` _ \ / _ \ \ /\ / /
 | |  | | (_| | |_| |_| | | | | |  __/\ V  V / 
 |_|  |_|\__,_|\__|\__|_| |_| |_|\___| \_/\_/                             """)
    elif opponent == ts:
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⣞⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⢸⡟⢏⠓⢦⣄⡀⠀⠀⠀⣆⠀⠀⠀⢀⣠⠞⣱⡧⠁⢸⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⣿⠀⠀⠀⠀⠀⣇⠘⡷⡀⠈⢫⣷⣾⣶⣿⣷⣤⡴⢫⠃⣼⢝⣷⡄⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣺⣷⡄⠀⠀⠀⠀⣿⢀⠹⡿⣶⣾⢿⡏⡝⣟⣞⠏⠉⠓⢰⣿⠀⣼⡅⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⡇⠀⠀⠀⠀⢸⣇⢺⣿⣿⡇⣿⢱⠼⡼⡎⠀⠀⠀⠀⠙⠧⣿⢊⣱⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠠⣿⣿⢷⠈⡇⢿⢸⠇⣷⠀⢀⠄⡀⢀⣄⡌⢻⣯⣿⣿⡃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⣸⡏⢸⢦⣑⠸⣀⠃⠙⣠⢗⣽⣷⢿⣻⠁⢀⠹⣭⣿⣳⣶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⢿⡾⠀⠀⠀⠀⠀⣾⣷⣾⣷⣝⢦⢾⢸⠲⣡⣞⠟⢽⣾⣷⣾⣏⠿⣯⣻⣿⡋⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣸⣤⣿⡆⣀⡄⠀⠀⠹⣧⣿⡮⠻⡷⠿⠓⣻⢟⠒⡬⢑⡯⠵⠦⡴⣾⣿⣿⠟⠀⠀⠀⠀⠀
⠀⠀⠀⡤⢦⠀⣿⣿⡏⣾⠃⠀⠀⠒⠘⣿⣿⠞⣧⣲⠌⠁⠱⠁⠒⠒⠓⢒⡾⡾⣷⡿⠇⠀⠀⠀⠀⠀⠀
⠀⣠⣏⢳⡈⣇⣓⣿⢠⡃⠀⠀⠀⠐⠁⡸⢻⢧⣀⠑⠤⠤⠠⢄⠀⢀⣴⣷⡯⠊⡬⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠙⣾⣦⣷⡾⠋⠀⡰⠁⠀⠀⠀⠀⠰⠀⠊⠀⠀⠉⠐⠤⣀⣤⣶⣿⡿⡛⠀⠀⢸⣾⢦⣀⠀⠀⠀⠀⠀
⠀⠀⠻⣦⡼⢿⣶⡞⠁⠀⠀⠀⠀⢀⣠⣦⠴⣤⣄⣤⢤⣤⢒⡿⠟⢋⠔⢀⣠⠖⣫⢴⣾⣿⠷⣦⣤⣀⠀
⠀⠀⢰⡻⡀⢸⣸⠀⠀⠀⠀⠀⢠⡿⠟⣫⣱⡴⢟⣶⡿⠛⠭⠷⡲⠛⡫⠛⣵⣶⠟⢋⡩⠴⠷⢿⣿⣿⣅
⠀⠀⣾⡯⠉⠛⠋⡇⠀⠀⠀⣠⣟⣒⣤⡾⡟⣡⣽⠋⡰⡴⠀⢚⣦⡾⣫⣺⡟⠁⠀⠠⠐⠒⠀⠸⣷⣾⣳
⠀⢠⢳⠃⠀⠀⢀⣇⠀⢀⣴⢟⣶⠟⢋⠎⡴⣾⣇⣠⠁⣀⡴⡻⢉⢮⣿⣽⠖⠁⠀⠀⠐⠒⠶⣤⡜⠈⡟
⠀⡾⠟⠀⠀⠀⠘⢹⡞⡿⢵⡾⠁⠀⠀⣄⢹⣻⢟⣛⡩⠕⠈⠊⣱⣿⡟⠃⠤⠄⣀⠀⠀⢀⣰⠿⠁⣼⡇
⢰⣗⡀⢀⠠⣐⠝⣽⣷⢀⣿⢇⠀⠀⣨⠎⡾⣶⠃⢀⠀⠀⢀⣼⣿⡛⣒⣀⠬⣁⠒⡭⣶⣟⠁⣠⣺⡟⠀
⣼⠙⢳⣀⠩⣔⠝⣹⢿⣏⢾⣷⡙⢆⠹⣔⣧⡞⠴⠃⠀⠂⣱⡿⠬⠤⠀⣀⣈⡵⠿⣦⣌⣻⢯⣾⠏⠀⠀
  _____     _     _           _   _           
 |_   _|_ _| |__ | |__  _   _| |_| |__   __ _ 
   | |/ _` | '_ \| '_ \| | | | __| '_ \ / _` |
   | | (_| | |_) | |_) | |_| | |_| | | | (_| |
   |_|\__,_|_.__/|_.__/ \__, |\__|_| |_|\__,_|
                        |___/                 """)
    elif opponent == ccs:
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣤⣀⣾⣽⣿⣳⣀⣤⣴⡿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠊⢿⣿⣿⡿⣷⣿⣿⣿⣿⡟⠰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡠⠋⠒⠒⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣰⠋⢀⣀⡤⢤⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⡏⠀⠀⠈⣇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣼⣿⡟⢿⣟⠛⠛⠛⣛⣿⠟⣻⣿⣯⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢧⠀⠙⣄⣀⣀⠜⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡟⠈⠸⣿⣿⣿⣿⣿⣿⣵⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡤⠵⠄⠀⠀⠀⠒⠳⠤⡄⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣦⣄⠀⠘⢶⠂⠀⠀⠤⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠓⠒⢲⠀⠀⢺⠲⠤⠤⠇⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣧⣀⠀⠂⠉⠐⠀⢀⣤⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠒⠤⠔⢚⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡜⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠋⠑⠀⠀⠊⠛⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⠹⣿⣿⣿⣿⣿⣷⣬⠂⠀⣭⣼⣿⣿⣿⣿⣿⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⠇⠀⢸⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡟⠀⠀⢳⣿⣿⣿⣿⣟⣿⣶⣶⣿⣟⣿⣿⣿⣿⡏⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠀⣀⡏⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⡇⠀⢀⣰⢿⣿⢿⣿⢿⢿⢷⣾⣿⣿⣿⣿⣿⣿⢁⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡴⢚⣅⢳⡀⠀⣼⣿⢫⣾⣿⣿⣿⡟⠁⠀⢠⠃⠈⢻⣮⠻⣿⣾⣾⣷⣾⣿⡿⢿⣾⠇⠘⣄⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡄⠤⢙⡇⢣⣰⣳⠃⣿⣾⣿⣿⡿⠁⠀⠀⠘⡄⠀⠀⠙⢷⣄⡙⠛⡟⠛⣉⣴⠿⠁⠀⠀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡹⠲⢿⢅⣸⢿⣿⣴⣿⡿⠿⠿⢇⠀⠀⠀⣠⣿⣤⣀⠀⠀⠙⢻⡽⢿⣽⡋⠁⠀⠀⣀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⠒⢼⣠⣫⣿⣟⣭⡗⡇⠀⠀⠀⠑⠀⡰⣿⣿⣿⣿⣟⣿⣿⣿⡷⠿⣿⣽⣿⣻⣿⡟⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠃⠀⡇⠀⠉⢻⢿⣿⡵⠁⠀⠀⠀⠀⠐⣼⣿⠟⣹⣏⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⡇⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⡇⠀⠀⡞⢠⣿⣿⣿⣿⣶⣶⣶⣾⣿⠃⣼⡟⢹⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡸⠀⢰⠃⠀⢠⢇⡏⣿⢸⣿⣿⣿⣿⣿⣿⠃⣸⠟⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣶⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⢸⠀⠀⢸⡼⠀⢿⣿⣿⣿⣿⣿⣿⡏⢀⠏⠀⣼⣅⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⢀⣼⣿⠏⢝⣧⡀⠀⠀⠀⠀⠀⠀
   ____ _                      _             
  / ___| | ___  ___   ___ __ _| |_ _ __ __ _ 
 | |   | |/ _ \/ _ \ / __/ _` | __| '__/ _` |
 | |___| |  __/ (_) | (_| (_| | |_| | | (_| |
  \____|_|\___|\___/ \___\__,_|\__|_|  \__,_|""")
    elif opponent == ls:
        print(""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢶⣤⡘⣷⣄⣀⣤⣤⣤⣤⡴⠾⠛⠷⠶⠶⠶⠾⠟⠳⢶⣦⣄⡀⢰⡿⠀⣠⣶⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣼⠿⣿⣿⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣷⣿⣏⣀⣀⣀⣀⣀⣤⣤⣤⡶⠶⠾⠛⠛⠛⠛⠛⣷⡀⠀⠀
⢿⣧⣀⠀⠉⠉⠙⠛⠻⠶⠶⠶⠶⠶⠶⠾⠛⠉⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⣀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣯⣍⡉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀
⠀⠈⠙⠻⢶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣶⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠻⣦⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠋⣁⣤⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣏⠉⠉⠉⠁⠀⠀⠀⠀⣠⣴⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠿⢋⣿⠃⠀⢀⣀⣀⣤⣤⣤⣤⣶⣶⣶⣦⣤⣤⣀⣀⣀⡀⠻⣦⡀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⢀⣴⠿⠋⠀⠀⣼⣧⣶⠾⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠻⣿⣿⡄⠀⡀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⠘⠻⢶⣄⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠘⠿⢶⣄⣀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠿⣣⡾⠋⠀⠀⠈⢿⣌⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣡⣤⣤⣤⣾⣿⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠉⠛⢷⣄⡉⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀⢰⡟⣠⡾⠋⠀⠀⠰⠶⠶⠿⣿⣿⣷⣶⠶⢶⣶⣤⣤⣀⣀⣀⠀
⠀⠀⠀⠰⠶⠾⠛⠛⢛⣿⠉⠀⠀⣀⣽⣧⣤⣴⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣦⣘⠇⠀⠀⠀⠀⠀⠀⠀⢨⣿⠏⠀⠀⠀⠀⠰⠶⢶⣤⣿⡀⠈⠛⢷⣦⣄⠀⠈⠉⠉⠛⠛
⠀⠀⠀⠀⠀⠀⢀⣀⣼⣷⠶⠿⠛⠋⢹⡇⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣦⣀⡀⠀⠀⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠰⢶⣤⣿⠛⠿⢶⣤⣈⠙⢷⣄⠀⠀⠀⠀
⠀⣀⣠⣤⡶⠾⠛⠉⠉⣿⡀⢀⣀⣤⡾⣿⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠻⣶⣄⡈⠙⠿⠎⢿⣆⠀⠀⠀
⠟⠛⠉⠀⠀⠀⠀⢀⣠⣼⣿⡛⠋⠁⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⢶⣤⣄⡀⠀⠀⠀⠀⠀⢀⣠⣼⠟⠁⠀⠀⠀⠙⠻⣶⡄⠀⠀⢻⣆⠀⠀
⠀⠀⠀⠀⣀⣴⠾⠛⠉⣸⡯⢿⣄⠀⠀⠀⠀⠈⠛⠷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠉⠀⠀⠈⠉⠛⠛⠿⣿⡿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⢿⡆⠀
⠀⢠⣴⠿⠋⠁⠀⢀⣼⠟⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠷⠶⠶⠶⠶⣶⣶⡾⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀
⠀⠀⠁⠀⠀⢀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡷
⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠶⠶⠶⠶⠾⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⣤⣴⣤⣖⣦⣤⣦⣤⣤⣤⣖⣦⡌⠛
  ____                _ 
 |  _ \ __ ___      _| |
 | |_) / _` \ \ /\ / / |
 |  __/ (_| |\ V  V /| |
 |_|   \__,_| \_/\_/ |_|""")
    #displays inventory and battle options
    while ps.hp > 0 and fighters[0].hp > 0:
        inventoryUi()
        ps.td = False
        colorize("""Press [a] to Attack
Press [d] to Defend
Press [1-10] to select Items""", bright_cyan)
        menuSelect = input()
        bleh = menuSelect
        #player's attack
        if menuSelect == "a":
            delete_lines(11)
            dmg = damage(ps.atk, fighters[0].prot)
            if ps.tm == True:
                dmg += (0.25 + ps.wpLvl * 0.25)
            dmg = round(dmg, 2)
            fighters[0].hp = fighters[0].hp - dmg
            inventoryUi()
            typewriter_effect3("You dealt ", str(dmg), " damage", red)
            ps.td = True
        #player's block
        elif menuSelect == "d":
            delete_lines(11)
            inventoryUi()
            typewriter_effect2("You ", "Blocked", black)
            ps.prot += 0.6
            ps.td = True
        #using an item
        elif menuSelect == "1" or menuSelect == "2" or menuSelect == "3" or menuSelect == "4" or menuSelect == "5" or menuSelect == "6" or menuSelect == "7" or menuSelect == "8" or menuSelect == "9" or menuSelect == "0" and inventory[int(menuSelect) > 0]:
            item(menuSelect)
        #incase of misinput
        else:
            print("error: unknown input")
            time.sleep(1.5)
            delete_lines(4)
        #switches to opponent's turn if the player is done
        if ps.td == True:
            time.sleep(1)
            delete_lines(1)
            #resets opponent's block
            fighters[0].prot = fighters[0].oprot
            invEmpty()
            if fighters[0].hp <= 0:
                death()
                return
            #checks if Pawl is napping
            if pawlNap == True:
                pawlNap = False
                fight(fighters[0])
            typewriter_effect(f"{fighters[0].name}{'s Turn'}", yellow)
            #checks for Mattmew's chargeAtk
            if ms.charge == 0:
                    ms.charge = 2
                    chrgdmg = 3 - (3 * ps.prot)
                    chrgdmg = round(chrgdmg, 2)
                    ps.hp -= chrgdmg
                    typewriter_effect3(f"{fighters[0].name}{' bashed you over the head for '}", chrgdmg, " Damage", red)
                    time.sleep(1.5)
                    delete_lines(9)
            #checks for Cleocatra's chargeAtk
            elif ccs.charge == 0:
                ccs.charge = 4
                chrgdmg = 5 - (5 * ps.prot)
                chrgdmg = round(chrgdmg, 2)
                ps.hp -= chrgdmg
                typewriter_effect3(f"{fighters[0].name}{' summoned the spirit of Raw, the Tuna God, smiting you for '}", chrgdmg, " Damage", red)
                time.sleep(1.5)
                delete_lines(9)
            #checks for Pawl's chargeAtk
            elif ls.charge == 0:
                ls.charge = 1
                #randomly selects a "Pawl Power"
                luck = random.choices(pawlPower, weights=[0.15, 0.1, 0.35, 0.2, 0.2], k=1)
                if luck == ['pity']:
                    typewriter_effect2("Pawl feels pity for you ", "[+2.0 HP]", green)
                    ps.hp = ps.hp + 2
                    if ps.hp > ps.maxhp:
                        ps.hp = ps.maxhp
                elif luck == ['tired']:
                    typewriter_effect2("Pawl has tired of this fruitless game ", "[-99% HP]", red)
                    ps.hp = ps.hp/100
                elif luck == ['hungry']:
                    if inventory["Whipped Cream"] >= 1:
                        inventory["Whipped Cream"] -= 1
                        ls.hp += (ls.hp * 0.1)
                        typewriter_effect2("Pawl is hungry ", "[-1 Whipped Cream]", yellow)
                    else:
                        typewriter_effect("Pawl seems more restless", yellow)
                        ls.atk = ls.atk * 1.5
                elif luck == ['nap']:
                    ls.prot = 0.9
                    ls.atk * 0.5
                    pawlNap = True
                    typewriter_effect("Pawl decides to take a nap ", yellow)
                elif luck == ['sneeze']:
                    pdmg = ps.hp * 0.1
                    ps.hp -= pdmg
                    typewriter_effect2("Pawl sneezes ", f"{'[-'}{pdmg}{']'}")
                time.sleep(1.5)
                delete_lines(9)
            else:
                #checks what the player did
                if menuSelect == "a":
                    #checks if the opponent is Cleocatra
                    if fighters[0] == ccs:
                        aord = random.randint(1, 5)
                        #Chooses whether Cleocatra will attack or defend
                        if aord < 3:
                            oppdmg = damage(fighters[0].atk, ps.prot)
                            typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage", red)
                            ps.hp -= oppdmg
                            time.sleep(1)
                            delete_lines(9)
                        elif aord >= 3:
                            typewriter_effect2(fighters[0].name, ' Blocked', black )
                            fighters[0].prot += 0.5
                            if fighters[0].charge > 0:
                                typewriter_effect(f"{fighters[0].name}{' is preparing a big attack['}{fighters[0].charge}{']'}", yellow)
                                fighters[0].charge -= 1
                            time.sleep(2)
                            delete_lines(10)
                    #checks if the opponent is Tabbytha
                    elif fighters[0] == ts:
                            oppdmg = damage(fighters[0].atk, ps.prot)
                            typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage x2", red)
                            ps.hp -= (oppdmg * 2)
                            time.sleep(2)
                            delete_lines(9)
                    else:
                        #chooses opponent's move
                        aord = random.randint(1, 2)
                        #opponent atk
                        if aord == 1:
                            oppdmg = damage(fighters[0].atk, ps.prot)
                            if fighters[0] == ts:
                                typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage x2", red)
                                ps.hp -= (oppdmg * 2)
                            else:
                                typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage", red)
                                ps.hp -= oppdmg
                            time.sleep(1)
                            delete_lines(9)
                        else:
                            #opponent block
                            typewriter_effect2(fighters[0].name, ' Blocked', black )
                            fighters[0].prot += 0.4
                            if fighters[0].charge > 0:
                                typewriter_effect(f"{fighters[0].name}{' is preparing a big attack['}{fighters[0].charge}{']'}", yellow)
                                fighters[0].charge -= 1
                                time.sleep(2)
                                delete_lines(10)
                            else:
                                time.sleep(2)
                                delete_lines(9)
                else:
                    #makes tabbytha deal x2 damage
                    if fighters[0] == ts:
                            typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage x2", red)
                            ps.hp -= (oppdmg * 2)
                    else:
                        #deals the opponent's damage to the player
                        oppdmg = damage(fighters[0].atk, ps.prot)
                        typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage", red )
                        ps.hp -= oppdmg
                    time.sleep(1)
                    delete_lines(9)
                ps.prot = nprot
    death()
    return

#gambling chances
gamble = ["🐶","😿","🐭","🧶","😸"]
weights = [0.25, 0.23, 0.22, 0.2, 0.1]

#Boe's Shop
def shop():
    global tms
    global cbbs
    delete_lines(100)
    #Displays Boe
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠶⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠰⠃⠀⢀⣠⡀⠓⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢋⣠⡀⠀⠁⠁⠒⠠⠤⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⣰⣼⣿⣷⡀⠈⠷⡤⠐⠂⠈⠐⢒⢄⣶⠃⠀⢰⣿⣿⣆⡄⠀⠀⠀⠀⠀⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⡔⠀⠀⢀⣾⢿⡉⢻⣗⠠⡀⠀⠂⠀⠀⠀⠀⠀⠀⠀⢄⡄⣘⣿⠃⣿⣿⢷⣤⣀⡀⢀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⢀⠀⣀⣀⣴⠟⢹⣾⣵⣤⡿⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣅⣴⣿⡿⠀⠀⠉⠉⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠈⢯⣺⡿⠃⠀⠀⢀⢀⠀⠀⠀⠀⠀⡀⡀⠀⠀⠨⢻⣏⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠟⢺⠅⠀⠁⢈⡀⠲⠀⠀⠀⠀⠀⣖⢁⣁⠁⠀⠘⡝⠛⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⠝⡱⠟⠁⢴⣿⣅⣽⡿⠁⠀⠀⠀⡼⣿⣅⣽⣿⡾⣿⡿⢦⡫⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠴⡞⢸⡇⠀⠀⠙⠋⠛⠟⠉⠀⠀⠀⠉⢻⠛⠓⠋⠀⠀⣨⡏⢳⠦⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⢤⠀⠀⠀⠀⠸⢷⠿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢨⢷⣽⠇⠀⠀⠀⠀⣤⡠⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣎⠐⣟⢆⢲⣦⣄⡀⠻⣁⣾⣷⡄⠰⣦⠀⠀⣴⣫⣍⣽⣦⠀⠀⡴⠄⣡⣾⣫⣼⠟⠀⣠⣴⣶⠲⣹⠏⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠠⠓⠀⠚⢤⡿⢉⣿⠃⠀⠉⠻⣾⣿⣦⣺⡀⠀⠻⠿⠿⠿⠟⠀⢠⣇⣴⣿⡟⠿⠁⠀⠈⢿⣽⣿⡿⠿⠚⠚⠄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡞⠁⡄⣠⠾⠤⣀⢳⣾⠃⠀⠀⣀⣠⣿⣿⣿⣿⣿⣭⠶⠛⠛⠻⢦⣴⣿⣿⣟⣿⣿⢄⣀⠀⠀⠈⢻⡋⢀⣄⣴⣒⢄⠀⢠⠀⠀⠀⠀
⠀⠀⠀⠀⠏⠀⠀⣠⡤⣤⠈⢋⣜⡤⣾⣿⣏⣿⣿⣿⣎⠻⣾⣿⣿⣦⣤⣴⣿⣿⣿⠟⣫⣿⡟⣼⢹⣿⡗⢤⣫⡽⢋⠀⡀⠀⠉⠀⠻⠀⠀⠀⠀
⠀⠀⠀⠀⡔⠀⡀⠠⢤⡸⠣⡼⢠⣿⣿⣿⣿⣿⡿⣧⡹⣷⣌⡛⠿⢿⡿⠿⡟⠛⣡⡾⣯⣿⡟⢻⣿⣿⢿⣼⠘⣤⠞⠉⠉⠛⠂⠀⣜⠀⠀⠀⠀
⠀⠀⠀⢴⡇⡀⡠⣿⣿⣷⣴⠇⢸⣿⣻⣿⣿⣿⣻⣞⠷⣮⢙⠿⣷⣦⣬⣽⡶⠿⡋⣾⡿⢋⣇⣿⣼⣿⣽⣿⡄⢭⣰⡶⠴⠶⠀⠀⣿⡣⠀⠀⠀
⠀⠀⣼⡘⣧⠢⠀⠈⢿⣿⢿⣄⣼⡏⣿⣯⢜⣿⣿⣽⣿⠾⣷⣦⣤⣢⠍⢥⣲⣿⠿⢋⢇⢌⣾⣿⡉⣹⣽⢹⡇⢸⡷⣴⣦⣤⠠⠚⣜⠇⣧⠀⠀
⠀⢠⣻⡕⠑⠲⣆⣔⣿⣫⣾⣿⣿⡇⢸⣿⣿⣿⡿⡷⣻⣔⡚⡿⣟⡿⣿⢿⣋⣥⣴⣎⣽⢿⡿⣿⣿⣿⡏⢸⣷⣿⣷⣝⢿⣽⣷⠾⢊⣺⣟⠄⠀
⢠⢿⡙⣿⣵⣤⣾⣷⢾⣿⣿⣿⣿⣇⣠⣿⣿⡻⣷⣷⣿⣻⣇⣧⣯⣿⠟⣭⣵⣧⣿⣿⣿⣼⡷⢿⣿⣿⣄⣸⣿⣿⣿⣿⣿⣶⣵⣤⣾⣿⢃⣿⠄
⢯⢊⢧⡙⢤⣝⢂⣴⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣶⣩⠿⣛⠿⠿⡻⠿⢽⠿⠿⠛⡿⠛⡋⠅⡾⣻⣯⣿⣿⣿⣿⣿⣿⣿⣿⣶⠯⢉⣤⢟⡼⢁⡸
⠈⣶⡑⠿⣷⣯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣽⣅⡀⢡⡙⢾⠉⣢⠔⣰⢊⣠⣦⣶⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣍⣶⠿⣁⣵⠋
⠀⠈⠉⠷⠶⠍⠉⣉⡿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⠙⠿⠿⣫⣉⠩⠶⠾⠋⠁⠀""")
    print("""
 _______    ______   ________  __   ______          ______   __    __   ______   _______  
|       \  /      \ |        \|  \ /      \        /      \ |  \  |  \ /      \ |       \ 
| $$$$$$$\|  $$$$$$\| $$$$$$$$| $$|  $$$$$$\      |  $$$$$$\| $$  | $$|  $$$$$$\| $$$$$$$\ 
| $$__/ $$| $$  | $$| $$__     \$ | $$___\$$      | $$___\$$| $$__| $$| $$  | $$| $$__/ $$
| $$    $$| $$  | $$| $$  \        \$$    \        \$$    \ | $$    $$| $$  | $$| $$    $$
| $$$$$$$\| $$  | $$| $$$$$        _\$$$$$$\       _\$$$$$$\| $$$$$$$$| $$  | $$| $$$$$$$ 
| $$__/ $$| $$__/ $$| $$_____     |  \__| $$      |  \__| $$| $$  | $$| $$__/ $$| $$      
| $$    $$ \$$    $$| $$     \     \$$    $$       \$$    $$| $$  | $$ \$$    $$| $$      
 \$$$$$$$   \$$$$$$  \$$$$$$$$      \$$$$$$         \$$$$$$  \$$   \$$  \$$$$$$  \$$                                                                           """)
    print(f"{'Cash: ' + green + '$' + str(ps.cash) + reset}")
    #gives the player a choice to buy, gamble, or go to the next fight
    colorize("""Press [a] to buy things
Press [s] to gamble
Press [d] to fight next opponent""", yellow)
    x = input()
    #displays the store shelves
    if x == "a":
        j = 5
        p = False
        while p == False:
            delete_lines(j)
            print(f"{'Cash: ' + green + '$' + str(ps.cash) + reset}")
            print("[1]Whipped Cream - $75")
            print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            if tms == False:
                print("[2]Toy Mouse - $250")
                print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            else:
                print("[2]SOLD OUT")
                print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            if cbbs == False:
                print("[3]Cardboard Box - $350")
                print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            else:
                print("[3]SOLD OUT")
                print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            print("[4]Scratching Post - $300")
            print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            print("[5]Ball of Yarn - $250")
            print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            print("[0]Next Fight")
            j = 12
            #checks what the player wants to buy
            sell = input()
            sell = int(sell)
            #tells the player about the item and asks if their sure
            if sell == 1:
                delete_lines(12)
                print("""A quick and reliable can of foamy pale cream [Heals 1 HP]""")
                buy = input("Buy?[y/n] ")
                #checks if they are sure and can afford it
                if buy == "y" and ps.cash >= 75:
                    delete_lines(1)
                    inventory["Whipped Cream"] += 1
                    ps.cash -= 75
                    typewriter_effect("You got +1 Whipped Cream!", yellow)
                    time.sleep(1)
                    j = 3
                else:
                    delete_lines(1)
                    typewriter_effect("[Boe] Yuh aint got the cash", blue)
                    time.sleep(1)
                    j = 3
            #tells the player about the item and asks if their sure
            elif sell == 2 and tms == False:
                delete_lines(12)
                print("""A rubber gray mouse toy with an excessivly long tail [Deals Extra Damage]""")
                buy = input("Buy?[y/n] ")
                #checks if they are sure and can afford it
                if buy == "y" and ps.cash >= 250:
                    tms = True
                    delete_lines(1)
                    inventory["Toy Mouse"] += 1
                    ps.cash -= 250
                    typewriter_effect("You got +1 Toy Mouse!", yellow)
                    time.sleep(1)
                    j = 3
                else:
                    delete_lines(1)
                    typewriter_effect("[Boe] Yuh aint got the cash", blue)
                    time.sleep(1)
                    j = 3
            elif sell == 2 and tms == True:
                delete_lines(1)
                typewriter_effect("[Boe] Ir only gots one mice", blue)
                time.sleep(1)
                delete_lines(1)
            #tells the player about the item and asks if their sure
            elif sell == 3 and cbbs == False:
                delete_lines(12)
                print("""A small rugged cardboard box [Extra Protection]""")
                buy = input("Buy?[y/n] ")
                #checks if they are sure and can afford it
                if buy == "y" and ps.cash >= 550:
                    delete_lines(1)
                    inventory["Cardboard Box"] += 1
                    ps.cash -= 550
                    cbbs = True
                    typewriter_effect("You got +1 Cardboard Box!", yellow)
                    time.sleep(1)
                    j = 3
                else:
                    delete_lines(1)
                    typewriter_effect("[Boe] Yuh aint got the cash", blue)
                    time.sleep(1)
                    j = 3
            elif sell == 3 and cbbs == True:
                delete_lines(1)
                typewriter_effect("[Boe] Out uv boxes", blue)
                time.sleep(1)
                delete_lines(1)
            #tells the player about the item and asks if their sure
            elif sell == 4:
                delete_lines(12)
                print("""A tall post wrapped in very worn down carpet [x2 Damage for a turn]""")
                buy = input("Buy?[y/n] ")
                #checks if they are sure and can afford it
                if buy == "y" and ps.cash >= 300:
                    tms = True
                    delete_lines(1)
                    inventory["Scratching Post"] += 1
                    ps.cash -= 300
                    typewriter_effect("You got +1 Scratching Post!", yellow)
                    time.sleep(1)
                    j = 3
                else:
                    delete_lines(1)
                    typewriter_effect("[Boe] Yuh aint got the cash", blue)
                    time.sleep(1)
                    j = 3
            #tells the player about the item and asks if their sure
            elif sell == 5:
                delete_lines(12)
                print("""A scrangly ball of tangled pink yarn [Distracts Opponent/Resets Charge]""")
                buy = input("Buy?[y/n] ")
                #checks if they are sure and can afford it
                if buy == "y" and ps.cash >= 300:
                    tms = True
                    delete_lines(1)
                    inventory["Ball of Yarn"] += 1
                    ps.cash -= 300
                    typewriter_effect("You got +1 Ball of Yarn!", yellow)
                    time.sleep(1)
                    j = 3
                else:
                    delete_lines(1)
                    typewriter_effect("[Boe] Yuh aint got the cash", blue)
                    time.sleep(1)
                    j = 3
            #starts next fight
            elif sell == 0:
                delete_lines(13)
                fight(fighters[0])
            #misinput
            elif sell not in range(0,8):
                delete_lines(13)
                print("error: unknown input")
            else:
                delete_lines(1)
                typewriter_effect("[Boe] Yuh aint got the cash")
                time.sleep(1)
                j = 13
    #makes sure you have money to gamble
    elif x == "s" and ps.cash <= 0:
        typewriter_effect("[Boe] Yurr out of monee", blue)
        time.sleep(1.5)
        delete_lines(1)
        shop()
    #starts slot machine
    elif x == "s":
        delete_lines(38)
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⠤⠤⠤⠤⠤⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⣉⡡⠤⣖⣒⣒⣒⣒⣒⡒⠤⠤⣉⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⡡⣖⣭⡶⠾⠛⠛⠯⠉⠉⠉⠙⠟⠛⠷⢶⣭⣲⢌⡑⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠉⡠⣪⣾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣝⢦⡈⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠉⠉⠉⠉⠁⠀⠈⠉⠁⣀⣴⣮⣾⣿⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣝⡢⣀⠈⠉⠐⠒⠂⠈⠉⠉⠉⠑⠢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⠀⠀⡴⣩⣿⣿⣭⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣌⣒⣂⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣒⣪⣾⣿⣿⣿⣿⣷⣯⣥⣶⣶⣶⣶⣿⣭⣢⠀⠀⢱⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⠀⠀⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠇⠀⢸⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢣⣀⣘⣟⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣟⣀⣠⠋⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠎⠀⠉⡝⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠈⠀⠈⠉⠉⠉⠉⠉⠹⡍⠀⠑⡄⠀⠀⠀⠀
⠀⠀⠀⡜⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⢱⠀⠀⠀⠀
⠀⠀⠀⠇⠀⠀⡇⣥⠖⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⣲⢀⠗⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⢲⠹⡒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠛⢏⠙⡄⠀⠈⡆⠀⠀⠀
⠀⠀⢸⠀⠀⢰⢡⡟⣲⡺⠯⠭⠭⠭⠭⠭⠭⠩⢽⣩⡟⠳⣸⡖⣶⣩⠭⠭⠭⠭⠭⠭⠭⠭⠽⣭⡕⢺⡆⡗⣶⣶⠾⠭⠭⠭⠵⠥⠭⠤⠿⣶⣶⠺⣇⡇⠀⠀⢣⠀⠀⠀
⠀⠀⡄⠀⠀⢸⣼⢃⠇⠈⣣⠠⠒⠈⠉⠉⠒⢴⡋⠀⡇⡇⣿⠁⡇⠈⣳⠠⠒⠊⠉⠉⠑⠢⡋⠀⢹⢸⡇⢁⢧⠀⢑⡄⠔⠂⠈⠉⠐⠢⣜⠁⠈⡇⣿⢱⠀⠀⢸⠀⠀⠀
⠀⠀⡇⠀⠀⣿⣿⢸⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⡧⡇⣿⢰⠖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠈⠓⠾⠘⣿⢸⠸⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠑⠢⢧⢹⣿⠀⠀⠘⡆⠀⠀
⠀⠀⡇⠀⠀⣿⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢹⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣿⢸⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡿⠀⠀⠀⡇⠀⠀
⠀⠀⡇⠀⠀⣿⣇⠈⠀⠀⣾⣷⠀⠀⠀⠀⣾⣷⠀⠀⠡⢸⣿⢸⠀⠀⢰⣿⡆⠀⠀⠀⢰⣿⡆⠀⠀⡇⣿⠸⠀⠀⠀⣾⣷⠀⠀⠀⠀⣾⣷⠀⠀⢸⢸⡇⡇⠀⠀⡇⠀⠀
⠀⠀⡇⠀⠀⣿⣏⠀⠀⢀⣀⣀⠀⢷⠞⠀⣀⣀⠀⠀⢰⢸⡗⢸⠀⠀⢀⣀⠀⠺⡾⠃⢀⣀⡀⠀⠀⡇⣿⢀⠀⠀⠀⣀⣀⠀⠶⡾⠂⣀⣀⠀⠀⢸⢸⡇⡇⠀⠀⡇⠀⠀
⠀⠀⡇⠀⠀⣿⣿⢰⠘⠛⠋⠙⠤⠊⠣⠔⠉⠛⠛⠀⡀⢸⣿⢸⠀⠻⠛⠋⠣⠜⠙⠤⠊⠙⠛⠗⠀⡇⣿⢸⢀⠀⠟⠛⠙⠤⠚⠑⠤⠋⠙⠛⠃⢸⢸⣷⠇⠀⠀⡇⠀⠀
⠀⠀⡇⠀⠀⣿⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠄⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣿⢸⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⣿⠀⠀⢰⠇⠀⠀
⠀⠀⢁⠀⠀⢸⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢀⣿⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⣼⣿⠀⠀⢸⠀⠀⠀
⠀⠀⢸⠀⠀⢸⣿⡎⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⡘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⡟⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣿⡟⠀⠀⣸⠀⠀⠀
⠀⠀⠈⡄⠀⠀⣿⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢠⢻⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⡇⣧⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢱⣿⡇⠀⠀⡇⠀⠀⠀
⠀⠀⠀⢇⠀⠀⢻⣿⣘⣦⣤⣤⣀⣀⣀⣀⣀⣠⣤⣤⣜⣸⢹⣇⣑⣤⣤⣄⣀⣀⣀⣀⣀⣤⣤⣴⣃⣾⣇⣇⣦⣤⣄⣀⣀⣀⣀⣀⣀⣠⣤⣤⣋⣼⣿⠁⠀⢰⠃⠀⠀⠀
⠀⠀⠀⠸⡀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⡏⠀⠀⡞⠀⠀⠀⠀
⠀⠀⠀⡠⠛⠛⣻⣫⣍⣩⣿⣭⣿⣿⣍⣉⣩⣭⣉⣉⣉⣩⠗⣻⣉⣹⣯⣉⣉⣉⣉⣉⣽⣍⣉⣉⣉⡗⡟⠛⣍⣉⣹⣯⣉⣉⣽⣯⣭⣿⡯⣉⣉⣁⣻⡛⠛⢧⠀⠀⠀⠀
⠀⢀⠞⠀⢀⡔⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣹⣿⡿⢀⢧⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣏⣩⣿⣷⠱⡀⢫⣿⣿⣷⣧⣿⣿⣿⣿⣿⣿⣿⣍⣽⣷⡕⡄⠀⠑⡄⠀⠀
⡴⠁⠀⠀⠚⠚⠛⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠥⠇⠸⠼⠭⠭⠭⠭⠭⠭⠭⠍⠉⠉⠉⠉⠉⠉⠁⠇⠘⠽⠯⠭⠭⠭⠭⠭⠭⠉⠉⠙⠉⠉⠛⠛⠚⠂⠀⠈⢆⠀
⠋⠛⠛⠓⠒⠒⠒⠒⠒⠒⠲⠶⠶⠶⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠴⠶⠶⠒⠒⠒⠒⠒⠒⠒⢒⣒⡛⠛⠋⠉⡆
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡇⠀⠀⠀⡇
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠤⠇⠀⠀⢰⠃
⠐⢤⠤⠤⠤⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⡤⠤⠤⡤⠞⠀
⠀⠀⡆⠀⠀⠀⠀⡖⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⡇⠀⠀""")
        print(f"{'Cash: ' + green + '$' + str(ps.cash) + reset}")
        #gets amount the player wants to bet
        amount = int(input("How much would you like to bet? (0 to cancel) "))
        z = 0.5
        #checks that they have the money
        if amount >= 1 and amount <= ps.cash:
            ps.cash -= amount
            #randomly chooses slot outcome
            c = random.choices(gamble, weights, k=3)
            #checks and displays slot outcome
            for char in c:
                print(char, end='', flush=True)
                time.sleep(z)
                z += 0.5
            #calculates winnings depending on outcome
            print()
            gambleM = 1
            for i in c:
                if i == "🐶":
                    gambleM -= 1
                elif i == "😿":
                    gambleM -= 0.5
                elif i == "🐭":
                    gambleM += 0.25
                elif i == "🧶":
                    gambleM += 0.5
                elif i == "😸":
                    gambleM += 1
            #Checks for jackpot
            if gambleM == 4:
                ps.cash += amount * 5
                typewriter_effect("YOU WON THE x5 JACKPOT!", bright_yellow)
            else:
                if gambleM > 3:
                    gambleM = 3
                if gambleM < 0:
                    gambleM = 0
                #gives player winnings from slot machine
                ps.cash += round(amount * gambleM)
                winnings = round(amount * gambleM)
                winnings = str(winnings)
                time.sleep(1)
                #checks if player won or lost
                if int(winnings) > amount:
                    typewriter_effect("You Won $" + winnings, bright_yellow)
                else:
                    typewriter_effect("You Lost", red)
            time.sleep(2)
            shop()
    #goes to next fight
    elif x == "d":
        invSave.update(inventory)
        fight(fighters[0])

#Initial input/home screen
start_choice = input("Press [y] to start: ")
if start_choice == "y":
    delete_lines(1)
    fight(fighters[0])
    #shop()
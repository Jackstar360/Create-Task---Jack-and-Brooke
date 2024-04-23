import time
import sys
import random

#deletes lines and moves the cursor up
def delete_lines(length):
    for i in range(length):
        sys.stdout.write('\x1b[1A')  
        sys.stdout.write('\r')        
        sys.stdout.write(' ' * 120)
        sys.stdout.write('\r')

#typewriter effects
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

#Player Stats
class ps:
    hp = float(5.0) #health points
    maxhp = float(5.0)
    atk = float(1.0) #attack damage
    prot = float(0.05) #armor multiplier
    oprot = float(0.05)
    td = False #turn finished
#Opponent's Stats
class cs:
    name = "Catrick"
    hp = float(4.0)
    maxhp = 4.0 #highest health points allowed
    atk = float(0.8)
    prot = float(0)
    oprot = float(0)
class js:
    name = "Jessicat"
    hp = float(5.0)
    maxhp = 5.0
    atk = float(1.0)
    prot = float(0.1)
    oprot = float(0.1)
bleh = "g"
#opponents list
fighters = [cs, js]
roster = [cs, js]

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
def inventoryUi(hp):
    while fighters[0].hp > 0 and ps.hp > 0:
        healthbar()#displays opponent health
        ps.hp = round(ps.hp, 2) #rounds and colors health
        hpclr = green
        if ps.hp <= (ps.maxhp * 1/5):
            hpclr = red
        elif ps.hp <= (ps.maxhp * 2.5/5):
            hpclr = bright_yellow
        #displays inventory, health, and cash
        print(f"{'Health: ' + hpclr + str(hp) + reset}")

#checks if the player or opponent is dead
def death():
    global fighters
    if ps.hp <= 0:
        typewriter_effect("You Died", bright_red)
    if fighters[0].hp <= 0 and ps.hp > 0: #checks if opponent is dead
        typewriter_effect("You Won!", bright_yellow)
        fighters.pop(0) #removes current opponent from list
        time.sleep(2)
        ps.hp = ps.maxhp #resets player hp
        fight(fighters[0])

#calculates damage
def damage(atk, per):
    sign = random.randint(1, 2) #randomly increases or decreases damage
    multiplier = round(random.uniform(0.00, 0.50), 2)
    if sign == 1:
        critAtk = (atk - multiplier)
    else:
        critAtk = (atk + multiplier)
    if critAtk < 0:
        critAtk = 0 #makes sure the damage isn't a negative int
    float(critAtk)
    critAtk = round(critAtk, 2) #rounds damage
    return(critAtk)

#runs the main game, displays your opponent, lets both sides take their turn
def fight(opponent):
    global bleh
    #makes sure no one is already dead
    death()
    #makes sure everything is reset from the last round
    nprot = ps.prot
    fighters[0].oprot = fighters[0].prot
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
    #displays inventory and battle options
    while ps.hp > 0 and fighters[0].hp > 0:
        inventoryUi(ps.hp)
        ps.td = False
        colorize("""Press [a] to Attack
Press [d] to Defend""", bright_cyan)
        menuSelect = input()
        bleh = menuSelect
        #player's attack
        if menuSelect == "a":
            delete_lines(7)
            dmg = damage(ps.atk, fighters[0].prot)
            dmg = round(dmg, 2)
            fighters[0].hp = fighters[0].hp - dmg
            inventoryUi(ps.hp)
            typewriter_effect3("You dealt ", str(dmg), " damage", red)
            ps.td = True
        #player's block
        elif menuSelect == "d":
            delete_lines(7)
            inventoryUi(ps.hp)
            typewriter_effect2("You ", "Blocked", black)
            ps.prot += 0.6
            ps.td = True
        #using an item
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
            death()
            typewriter_effect(f"{fighters[0].name}{'s Turn'}", yellow)
            time.sleep(1.5)
            delete_lines(5)
            #checks what the player did
            if menuSelect == "a":
                #chooses opponent's move
                aord = random.randint(1, 2)
                #opponent atk
                if aord == 1:
                    oppdmg = damage(fighters[0].atk, ps.prot)
                    typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage", red)
                    ps.hp -= oppdmg
                    time.sleep(1)
                    delete_lines(1)
                else:
                    #opponent block
                    typewriter_effect2(fighters[0].name, ' Blocked', black )
                    fighters[0].prot += 0.4
                    time.sleep(1)
                    delete_lines(1)
            else:
                #deals the opponent's damage to the player
                oppdmg = damage(fighters[0].atk, ps.prot)
                typewriter_effect3(f"{fighters[0].name}{' dealt '}", oppdmg, " Damage", red )
                ps.hp -= oppdmg
                time.sleep(1)
                delete_lines(1)
                ps.prot = nprot
    death()
    return
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
time.sleep(3)
fight(fighters[0])
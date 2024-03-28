#Requirements:
#user input
#function w/ params, conditional, and loop
#list or dictionary
import curses
import time
import sys
import random

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

def delete_lines(length):
    for i in range(length):
        sys.stdout.write('\x1b[1A')  
        sys.stdout.write('\r')        
        sys.stdout.write(' ' * 120)
        sys.stdout.write('\r')

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
    

#Makes the middle of a sentence colored
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


class cLines:
    whippedCream = ["you still feel empty","it fill you with Determination","you can feel it evaporate before even reaching your stomach","and leave none for the next person!","it's just what you need to heal the open wounds"]
    toyMouse = ["and begin swinging it around like a maniac","you opponent seemed to get quite excited","it reminds you that you forgot to eat lunch","you wonder if this will actually be an effective weapon"]

#Player Stats
class pS:
    hp = float(5.0)
    atk = float(5.0)
    prot = float(0.05)
    cash = 200
    tM = False
    wpLvl = 1
    tD = False
class cS:
    name = "Catrick"
    hp = float(4.0)
    maxhp = 4.0
    atk = float(0.8)
    prot = float(0)
    payout = 40
class jS:
    name = "Jessicat"
    hp = float(5.0)
    maxhp = 5.0
    atk = float(1.0)
    prot = float(0.1)
    payout = 70

fighters = [cS, jS, "Mattmew", "Tabbytha", "Cleocatra", "Pawl", "Mewlious Caesar"]
inventory = {
    "Whipped Cream":4, #heals
    "String":0, 
    "Toy Mouse":1, #offensive Item
    "Cardboard Box": 0, #defensive item
    "Scratching Post":0, #bonus atk
    "Ball of Yarn":0, #distracts opponent for a turn, resets charges
    "Catnip":0, #heals + bonus atk
    "Bullets":0, #ammo for gun
    "Gun":0, #strongest offensive item, requires bullets
    "Stripped Tophat":0, #strongest defensive item + bonus atk
    } 
items = ["Whipped Cream","String","Toy Mouse","Cardboard Box","Scratching Post","Ball of Yarn","Catnip","Bullets","Gun","Stripped Tophat"]

playerInv = []

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

def colorize(text, color):
    print(f'{color}{text}{reset}')

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

def invEmpty():
    tempInv = 0
    for i in inventory.values():
        if int(i) >= 1:
            tempInv += 1
    if tempInv == 0:
        return True
    else:
        return False
    
    
def healthbar():
    if fighters[0].hp <= (fighters[0].maxhp * 1/8):
        print("""⢠⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 2/8):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 3/8):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 4/8):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 5/8):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 6/8):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    elif fighters[0].hp <= (fighters[0].maxhp * 7/8):
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠷⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⠃""")
    else:
        print("""⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠃""")
        

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
                    inv.append(str(invLoc2) + (") ") + i + (" X") + str(inventory.get(i)))
                else:
                    inv.append(str(invLoc2) + (") ") + i)
                if invLoc == 9:
                    break
            invLoc = invLoc + 1

    print(f"{'Health: ' + green + str(pS.hp) + reset}{'  Cash: ' + green + '$' + str(pS.cash) + reset}")
    print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    print(inv)
    print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")



    

def death():
    if pS.hp <= 0:
        typewriter_effect("You Died", bright_red)
    if fighters[0].hp <= 0 and pS.hp > 0:
        typewriter_effect("You Won!", bright_yellow)
        prize = (fighters[0].payout * pS.hp)
        pS.cash += prize
        countUpTo(prize, bright_green)
        fighters.pop(0)
        time.sleep(2)
        shop()


def damage(atk, per):
    sign = random.randint(1, 2)
    multiplier = round(random.uniform(0.00, 0.50), 2)
    if sign == 1:
        critAtk = (atk - multiplier)
    else:
        critAtk = (atk + multiplier)
    critAtk = (critAtk - (critAtk * per))
    float(critAtk)
    return(critAtk)

    
def item(menuSelected):
    x = (int(menuSelected) - 1)
    it = playerInv[x]
    if it == "Whipped Cream":
        pS.hp += 1
        inventory["Whipped Cream"] -= 1
        delete_lines(11)
        inventoryUi()
        typewriter_effect4("You guzzle the airy white foam, ", random.choices(cLines.whippedCream), yellow)
    elif it == "Toy Mouse":
        pS.tM = True
        inventory["Toy Mouse"] -= 1
        delete_lines(11)
        inventoryUi()
        typewriter_effect4("You reveal a rubbery toy of a gray mouse, ", random.choices(cLines.toyMouse), yellow)
    elif it == "Cardboard Box":
        print("uh")
    time.sleep(2)
    tD2 = False
    while tD2 == False:
        colorize("""Press [a] to Attack
Press [d] to Defend""", bright_cyan)
        menuSelect = input()
        if menuSelect == "a":
            delete_lines(11)
            dmg = damage(pS.atk, fighters[0].prot)
            if pS.tM == True:
                    dmg = dmg * 1.2
            fighters[0].hp = fighters[0].hp - dmg
            typewriter_effect3("You dealt ", str(dmg), " damage", red)
            pS.tD = True
            tD2 = True
        elif menuSelect == "d":
            delete_lines(11)
            typewriter_effect2("You ", "Blocked", black)
            pS.prot += 0.6
            pS.tD = True
            tD2 = True
        elif menuSelect == "1" or menuSelect == "2" or menuSelect == "3" or menuSelect == "4" or menuSelect == "5" or menuSelect == "6" or menuSelect == "7" or menuSelect == "8" or menuSelect == "9" or menuSelect == "0":
            item("error: you already used an item this turn")
            time.sleep(1.5)
            delete_lines(4)
        else:
            print("error: unknown input")
            time.sleep(1.5)
            delete_lines(4)



def fight(opponent):
    if pS.hp <= 0 or fighters[0].hp <= 0:
        death()
        return
    nprot = pS.prot
    oprot = fighters[0].prot
    if opponent == cS:
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
  _  __     _        _      _    
 | |/ /__ _| |_ _ __(_) ___| | __
 | ' // _` | __| '__| |/ __| |/ /
 | . \ (_| | |_| |  | | (__|   < 
 |_|\_\__,_|\__|_|  |_|\___|_|\_\                          
""")
    elif opponent == jS:
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣞⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
  \___/ \___||___/___/_|\___\__,_|\__|                              
""")
    while pS.hp > 0 and fighters[0].hp > 0:
        inventoryUi()
        pS.tD = False
        colorize("""Press [a] to Attack
Press [d] to Defend
Press [1-10] to select Items""", bright_cyan)
        menuSelect = input()
        if menuSelect == "a":
            delete_lines(11)
            dmg = damage(pS.atk, fighters[0].prot)
            if pS.tM == True:
                dmg += (0.25 + pS.wpLvl * 0.25)
            fighters[0].hp = fighters[0].hp - dmg
            typewriter_effect3("You dealt ", str(dmg), " damage", red)
            pS.tD = True
        elif menuSelect == "d":
            delete_lines(11)
            typewriter_effect2("You ", "Blocked", black)
            pS.prot += 0.6
            pS.tD = True
        elif menuSelect == "1" or menuSelect == "2" or menuSelect == "3" or menuSelect == "4" or menuSelect == "5" or menuSelect == "6" or menuSelect == "7" or menuSelect == "8" or menuSelect == "9" or menuSelect == "0":
            item(menuSelect)
        else:
            print("error: unknown input")
            time.sleep(1.5)
            delete_lines(4)
            
        if pS.tD == True:
            time.sleep(1)
            #opponent's turn
            fighters[0].prot = oprot
            delete_lines(1)
            if fighters[0].hp <= 0:
                death()
                return
            typewriter_effect("Opponent's Turn", yellow)
            if menuSelect == "a":
                aord = random.randint(0, 1)
                if aord == 0:
                    dmg = damage(fighters[0].atk, pS.prot)
                    typewriter_effect3("Opponent dealt ", dmg, " Damage", red)
                    pS.hp -= dmg
                    time.sleep(1)
                    delete_lines(2)
                else:
                    typewriter_effect2("Opponent ", "Blocked", black)
                    fighters[0].prot += 0.4
                    oppTempShield = True
                    time.sleep(1)
                    delete_lines(2)
            else:
                dmg = damage(fighters[0].atk, pS.prot)
                typewriter_effect3("Opponent dealt ", dmg, " Damage", red )
                pS.hp -= dmg
                time.sleep(1)
                delete_lines(2)
                pS.prot = nprot
    return

gamble = ["📦","🐭","🐱","🧶","😸"]
weights = [0.37, 0.28, 0.18, 0.13, 0.04]

def shop():
    mB = False
    delete_lines(30)
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
    colorize("""Press [a] to buy things
Press [s] to gamble
Press [d] to fight next opponent""", yellow)
    x = input()
    if x == "a":
        print("Whipped Cream - $100")
        print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
        print("Toy Mouse - $350")
        print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    elif x == "s":
        delete_lines(30)
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
        amount = int(input("How much would you like to bet? (0 to cancel) "))
        z = 0.5
        if amount >= 1 and amount <= pS.cash:
            pS.cash -= amount
            c = random.choices(gamble, weights, k=3)
            for char in c:
                print(char, end='', flush=True)
                time.sleep(z)
                z += 0.5
            print()
            win = False
            if c == "📦📦📦":
                winnings = amount * 1.5
                pS.cash += winnings
                win = True
            elif c == "🐭🐭🐭":
                winnings = amount * 2
                pS.cash += winnings
                win = True
            elif c == "🐱🐱🐱":
                winnings = amount * 3
                pS.cash += winnings
                win = True
            elif c == "🧶🧶🧶":
                winnings = amount * 5
                pS.cash += winnings
                win = True
            elif c == "😸😸😸":
                winnings = amount * 10
                pS.cash += winnings
                win = True
            else:
                for i in gamble:
                    if c.count(gamble[str(i)]) == 2:
                        pS.cash += amount
                        typewriter_effect("Money Back!")
                        mB = True
            if win == True:
                typewriter_effect("You Won $" + winnings, bright_yellow)
            elif win == True and mB == False:
                typewriter_effect("You Lost")
            time.sleep(2)
            shop()
            
    elif x == "d":
        fight(fighters[0])



start_choice = input("Press [y] to start: ")
if start_choice == "y":
    delete_lines(1)
    #fight(fighters[0])
    shop()
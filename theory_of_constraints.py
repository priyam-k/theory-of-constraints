import random
from time import sleep
import pygame

pygame.init()
dis_width = 1100
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.update()
pygame.display.set_caption("Theory of Constraints Simulator, by Priyam K.")

labels = ["RP", "M1", "M2", "M3", "M4", "M5", "FG"]
inventory = [0, 0, 0, 0, 0, 0]
inv_stages = [[[0, 0, 0, 0, 0, 0], 1, 0, 0, 0]]

days = 30 + 1

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

dice = pygame.image.load("theory-of-constraints/sides-of-dice.png")
empty_bowl = pygame.image.load("theory-of-constraints/empty-bowl.png")
empty_bowl = pygame.transform.scale(empty_bowl, (110, 80))
match_bowl = pygame.image.load("theory-of-constraints/bowl-with-matches.png")
match_bowl = pygame.transform.scale(match_bowl, (150, 120))

font_style = pygame.font.SysFont("consolas", 30)
def message(msg, color, x=dis_width/2-100, y=dis_height/2):
    sendMsg = font_style.render(msg, True, color)
    dis.blit(sendMsg, [x, y])

def list_to_str(arr):
    return " ".join(list(map(str, arr)))

def format_line(inventory):
    return "{}     {}     {}     {}     {}     {}".format(
        str(inventory[0])+" "*(4-len(str(inventory[0]))),
        str(inventory[1])+" "*(4-len(str(inventory[1]))),
        str(inventory[2])+" "*(4-len(str(inventory[2]))),
        str(inventory[3])+" "*(4-len(str(inventory[3]))),
        str(inventory[4])+" "*(4-len(str(inventory[4]))),
        str(inventory[5])+" "*(4-len(str(inventory[5])))
        )


for i in range(days):
    for k in range(0, min(i, 6))[::-1]:
        dice_roll = random.randint(1, 6)
        if k != 0:
            adj_roll = min(dice_roll, inventory[k-1])
            inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll]) ###
        else:
            inv_stages.append([inventory.copy(), i, k, dice_roll, dice_roll]) ###
        #format_line(inventory, i, dice_roll) ###
        
        if k != 0:
            adj_roll = min(dice_roll, inventory[k-1])
            inventory[k] += adj_roll
            #inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll]) ###
            #format_line(inventory, i) ###
            inventory[k-1] -= adj_roll

            inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll])
            #inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll]) ###
        else:
            inventory[k] += dice_roll
            inv_stages.append([inventory.copy(), i, k, dice_roll, dice_roll]) ###
            #format_line(inventory, i) ###

    #format_line(inventory, i)

pygame.key.set_repeat(500, 100) # key repetition
count = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                count = min(count+1, len(inv_stages)-1)
            if event.key == pygame.K_LEFT:
                count = max(count-1, 0)

    dis.fill(white)

    # showing the info:
    message(f"Day: {inv_stages[count][1]}, Roll: {inv_stages[count][3]}", black, 400, 20)

    roll_txt = ["", "", "", "", "", ""]
    if inv_stages[count][4] != 0:
        roll_txt[inv_stages[count][2]] = f"+{inv_stages[count][4]}"
        if inv_stages[count][2] != 0:
            roll_txt[inv_stages[count][2]-1] = f"-{inv_stages[count][4]}"
    
    message(format_line(roll_txt), black, 225, 350) # adding and subtracting signs
    #message(f"roll: {inv_stages[count][3]}", black, 20, 175)

    # detecting when the die will roll
    #if count %2 == 1:
        #message("new roll!", black, 20, 160)
    
    for i in range(6):
        if inv_stages[count][0][i]:
            dis.blit(match_bowl, (180+150*i, 220))
        else:
            dis.blit(empty_bowl, (200+150*i, 250))

    message("∞", black, 90, 200)
    dis.blit(match_bowl, (30, 220))
    message("{}      {}       {}       {}       {}       {}       {}".format(*labels), black, 80, 175)
    message(format_line(inv_stages[count][0]), black, 230, 200) # bowl values

    # showing sides of dice
    if inv_stages[count][3] == 1:
        dis.blit(dice, (500, 75), (20, 55, 60, 60))
    elif inv_stages[count][3] == 2:
        dis.blit(dice, (500, 75), (80, 55, 60, 60))
    elif inv_stages[count][3] == 3:
        dis.blit(dice, (500, 75), (140, 55, 60, 60))
    elif inv_stages[count][3] == 4:
        dis.blit(dice, (500, 75), (20, 115, 60, 60))
    elif inv_stages[count][3] == 5:
        dis.blit(dice, (500, 75), (80, 115, 60, 60))
    elif inv_stages[count][3] == 6:
        dis.blit(dice, (500, 75), (140, 115, 60, 60))
    pygame.display.update()

### old

## import random
## from time import sleep
## import pygame
## 
## pygame.init()
## dis_width = 900
## dis_height = 700
## dis = pygame.display.set_mode((dis_width, dis_height))
## 
## pygame.display.update()
## pygame.display.set_caption("Theory of Constraints Simulator, by Priyam K.")
## 
## labels = ["Day", "M1", "M2", "M3", "M4", "M5", "FG"]
## inventory = [0, 0, 0, 0, 0, 0]
## inv_stages = [[[0, 0, 0, 0, 0, 0], 1, 0, 0, 0]]
## 
## #days = min(9999, int(input("Number of days of simulation: ")))
## #sleep_time = float(input("Time between actions: "))
## days = 10 + 1
## 
## red = (255, 0, 0)
## green = (0, 255, 0)
## blue = (0, 0, 255)
## white = (255, 255, 255)
## black = (0, 0, 0)
## 
## font_style = pygame.font.SysFont("consolas", 30)
## def message(msg, color, x=dis_width/2-100, y=dis_height/2):
##     sendMsg = font_style.render(msg, True, color)
##     dis.blit(sendMsg, [x, y])
## 
## def list_to_str(arr):
##     return " ".join(list(map(str, arr)))
## 
## def print_line(inventory, i, roll=False):
##     #print("\r", end="")
##     #if roll:
##         #print("Dice roll: {}  ".format(roll), end="")
##     return "  {}   {}   {}   {}   {}   {}   {}  ".format(
##         str(i)+" "*(4-len(str(i))),
##         str(inventory[0])+" "*(4-len(str(inventory[0]))),
##         str(inventory[1])+" "*(4-len(str(inventory[1]))),
##         str(inventory[2])+" "*(4-len(str(inventory[2]))),
##         str(inventory[3])+" "*(4-len(str(inventory[3]))),
##         str(inventory[4])+" "*(4-len(str(inventory[4]))),
##         str(inventory[5])+" "*(4-len(str(inventory[5])))
##         )
##     #if roll:
##     #    sleep(sleep_time)
## 
## #print(".________________________________________________.")
## #print("| {}  | {}   | {}   | {}   | {}   | {}   | {}   |".format(*labels))
## #print("+------+------+------+------+------+------+------+")
## 
## #i = 0
## #while True:
##     
## 
## 
## #'''
## for i in range(days):
##     for k in range(0, min(i, 6))[::-1]:
##         dice_roll = random.randint(1, 6)
##         if k != 0:
##             adj_roll = min(dice_roll, inventory[k-1])
##             inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll]) ###
##         else:
##             inv_stages.append([inventory.copy(), i, k, dice_roll, dice_roll]) ###
##         #print_line(inventory, i, dice_roll) ###
##         #adj_roll = 0
##         if k != 0:
##             adj_roll = min(dice_roll, inventory[k-1])
##             inventory[k] += adj_roll
##             #inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll]) ###
##             print_line(inventory, i, dice_roll) ###
##             inventory[k-1] -= adj_roll
## 
##             inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll])
##             #inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll]) ###
##         else:
##             inventory[k] += dice_roll
##             inv_stages.append([inventory.copy(), i, k, dice_roll, dice_roll]) ###
##             print_line(inventory, i, dice_roll) ###
##         #if k != 0:
##         #    inv_stages.append([inventory.copy(), i, k, dice_roll, adj_roll]) ###
##     print_line(inventory, i)
##     #print(" "*100)
## #print("+------+------+------+------+------+------+------+")
## #'''
## #print(inventory)
## #print(inv_stages)
## 
## count = 0
## while True:
## 
##     for event in pygame.event.get():
##         if event.type == pygame.QUIT:
##             pygame.quit()
##         if event.type == pygame.KEYDOWN:
##             if event.key == pygame.K_RIGHT:
##                 count = min(count+1, len(inv_stages)-1)
##             if event.key == pygame.K_LEFT:
##                 count = max(count-1, 0)
## 
##     dis.fill(white)
##     message("| {}  | {}   | {}   | {}   | {}   | {}   | {}   |".format(*labels), black, 20, 20)
##     message(print_line(inv_stages[count][0], inv_stages[count][1]), black, 20, 50)
##     roll_txt = ["", "", "", "", "", ""]
##     if inv_stages[count][4] != 0:
##         roll_txt[inv_stages[count][2]] = f"+{inv_stages[count][4]}"
##         if inv_stages[count][2] != 0:
##             roll_txt[inv_stages[count][2]-1] = f"-{inv_stages[count][4]}"
##     message(print_line(roll_txt, ""), black, 20, 100)
##     message(f"roll: {inv_stages[count][3]}", black, 20, 130)
##     
##     if count %2 == 1:
##         message("new roll!", black, 20, 160)
##     #message(f"{list_to_str(inv_stages[count][0])} day: {inv_stages[count][1]+1} k: {inv_stages[count][2]} roll: {inv_stages[count][3]}", black, 20, 50)
##     pygame.display.update()
## 
##
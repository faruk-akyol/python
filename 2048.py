from operator import truediv
from turtle import end_fill
import random
from pynput import keyboard
import time


table = [[" "," "," "," "],
         [" "," "," "," "],
         [" "," "," "," "],
         [" "," "," "," "]]


def printTable(table):
    
    for rows in table:
        for numbers in rows:
        
            max=0
            if numbers==" ":
                continue
            if numbers>max:
                max=numbers
        
    #for i in range(10):
     #   print("\n")
     
    for rows in table:
        spaceNumber=len(str(max))
        print("+",end="")
        for i in range(4):
            
            print("-"*(spaceNumber+2)+"+",end="")
            print("\n")
        for elements in rows:
            format = str(elements).center(len(str(elements))+2)
            print("|"+format,end="")
        if elements == rows[3]:
            print("|")
        
        
        
    if rows == table[3]:
        print("+---+---+---+---+")
        
        
        



def newNumber(table):
    numbers={}
    n=0
    for i in range(len(table)):
        for j in range(len(table)):
            if(table[i][j]==" "):
                list2=[]
                list2.append(i)
                list2.append(j)
                
                numbers[str(n)]=list2
                n+=1
                
    random_choice =random.choice(list(numbers.keys()))
    
    new_number_row,new_number_column=numbers[random_choice]
    
    table[new_number_row][new_number_column]=2
def tableControl(new_list):
    for elements in new_list:
        if not elements==" ":
            return False
    return True

def tableControlVertical(j,first_i,last_i):
    for number in range(last_i-first_i-1):
        if  not table[number+1][j]==" ":
            return False
    return True

def operation(player_move):
    if player_move=="a":
        for i in range(len(table)):
            for j in range(len(table[0])):
                '''
                for k in range(len(table)-j-1):
                    if table[i][j]==table[i][k+1] and not(table[i][j]==" "):
                        if(table[i][j]==" "):
                            continue
                        table[i][j]*=2
                        table[i][k+1]=" "
                '''
                for k in range(3-j):
                    if(table[i][j] == table[i][j+k+1]) and (tableControl(table[i][(j+1):(j+k+1)])) and  (not table[i][j]==" "):
                        table[i][j]*=2
                        table[i][j+k+1]=" "
                        break
                    
                    
    if player_move=="w":
        for j in range(len(table)):
            for i in range(len(table[0])):
                for k in range(3-i):
                    if(table[i][j] == table[i+k+1][j]) and (tableControlVertical(j,(i+1),(i+k+1))) and  (not table[i][j]==" "):
                        table[i][j]*=2
                        table[i+k+1][j]=" "
                        break
    if player_move=="d":
        for i in range(len(table)):
            for j in range(len(table[0])):
                for k in range(3-j):
                    if(table[i][3-j] == table[i][3-j-k-1]) and (tableControl(table[i][(3-j-k):(3-j)])) and  (not table[i][3-j]==" "):
                        table[i][3-j] *=2
                        table[i][3-j-k-1]=" "
                        break
    if player_move=="s":
        for j in range(len(table)):
            for i in range(len(table)):
                for k in range(3-i):
                    if(table[3-i][j] == table[3-i-k-1][j]) and (tableControlVertical(j,(3-i-k),(3-i))) and  (not table[3-i][j]==" "):
                        table[3-i][j] *=2
                        table[3-i-k-1][j]=" "
                        break
    
                    
                     
                        
def spaceSkip(player_move):
    if player_move=="a":
        for i in range(len(table)):
            for j in range(len(table[0])):
                    space=0
                    for k in range(j):
                        
                        
                        if table[i][j-k-1]==" " and  (not table[i][j]==" "):
                            space+=1
                    if  not space == 0:
                        table[i][j-space]=table[i][j]
                        table[i][j]=" "
    if player_move=="w":
        for j in range(len(table)):
            for i in range(len(table[0])):
                    space=0
                    for k in range(i):
                        
                        
                        if table[i-k-1][j]==" " and  (not table[i][j]==" "):
                            space+=1
                    if  not space == 0:
                        table[i-space][j]=table[i][j]
                        table[i][j]=" "
                        
    if player_move=="d":
        for i in range(len(table)):
            for j in range(len(table[0])):
                    space=0
                    for k in range(j):
                        
                        
                        if table[i][3-j+k+1]==" " and  (not table[i][3-j]==" "):
                            space+=1
                    if  not space == 0:
                        table[i][3-j+space]=table[i][3-j]
                        table[i][3-j]=" "
                        
    if player_move=="s":
        for j in range(len(table)):
            for i in range(len(table[0])):
                    space=0
                    for k in range(i):
                        
                        
                        if table[3-i+k+1][j]==" " and  (not table[3-i][j]==" "):
                            space+=1
                    if  not space == 0:
                        table[3-i+space][j]=table[3-i][j]
                        table[3-i][j]=" "
    
                    
                        
    
                    
def gameOverCondition():
    for i in range(len(table)):
        for j in range(len(table[0])):   
            if table[i][j]==" ":
                return False
            if table[i][j]==table[i-1][j] or table[i][j]==table[i][j-1] or table[i][j]==table[i][j+1] or table[i][j]==table[i+1][j]:
                return False
    return True
    
        
while True:
    gameOverCondition()
    newNumber(table)
    printTable(table)
    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char('s'):
            player_move="s"
        elif event.key == keyboard.KeyCode.from_char('w'):
            player_move="w"
            
        elif event.key == keyboard.KeyCode.from_char('a'):
            player_move="a"
        elif event.key == keyboard.KeyCode.from_char('d'):
            player_move="d"
            
        time.sleep(0.4)
    operation(player_move)
    spaceSkip(player_move)
    
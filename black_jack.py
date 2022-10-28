print( """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
import random
Point_sys=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player=[]
computer=[]
target=21
def player_takes_card():
    card=random.choice(Point_sys)
    player.append(card)
    Point_sys.remove(card)
def computer_takes_card():
    card=random.choice(Point_sys)
    computer.append(card)
    Point_sys.remove(card)
def blackjack():
    for i in range(4):
        if i>1:
            player_takes_card()
        else:
            computer_takes_card()
    print(f"Your Card:{player}\tYour score:{sum(player)}")
    while sum(player)<21:
        rep_pl = input("\nEnter 'y' for new card or press any key to stop.")
        if rep_pl=='y':
            player_takes_card()
            print(f"Your Card:{player}\tYour score:{sum(player)}")
        else:
            break
    while sum(computer)<21:
        rep_cp = random.choice(["y","n"])
        if rep_cp=='y':
            computer_takes_card()
        else:
            break
    if sum(player)>21 and 11 in player:
        player[player.index(11)]=1
    if sum(computer)>21 and 11 in computer:
        computer[computer.index(11)]=1
    print(f"\n\nYour Cards:{player}\tYour score:{sum(player)}\nComputer's Cards:{computer}\tComputer's score:{sum(computer)}")
    if sum(player)>21 and sum(computer)<=21 :
        print("You lose")
    elif sum(computer)>21 and sum(player)<=21:
         print("You win")
    elif 21-sum(player)<21-sum(computer):
        print("You win")
    elif sum(player)==sum(computer) or sum(computer)>21 and sum(player)>21:
        print("Draw")
    else:
        print("You lose")
blackjack()
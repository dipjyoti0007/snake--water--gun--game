'''
SNAKE, WATER, GUN GAME!!!!
-1 -> Water
0 -> Gun
1 -> Snake 

'''
import random


computer_choice = random.choice([-1, 0 , 1])
#print(computer_choice)


computer_dict = {1 : "snake", 0 : "gun", -1 : "water"}
game_dict = {"snake" : 1, "gun" : 0, "water" : -1}


user_choice = input("ENTER YOUR CHOICE IN THE GAME : ")


if user_choice not in game_dict:
    print("INVALID INPUT!")
    exit()



c_choice = computer_dict[computer_choice]
u_choice = game_dict[user_choice]
#print(u_choice)




print(f"Computer's Choice -> {c_choice}")
print(f"User's Choice -> {user_choice}")




if(computer_choice == u_choice):
    print("DRAW!!")
else:
    if(computer_choice == -1 and u_choice == 1):
        print("USER WINS!")
    elif(computer_choice == -1 and u_choice == 0):
        print("COMPUTER WINS!")
    elif(computer_choice == 0 and u_choice == 1):
        print("COMPUTER WINS!")
    elif(computer_choice == 0 and u_choice == -1):
        print("USER WINS!")    
    elif(computer_choice == 1 and u_choice == 0):
        print("USER WINS!")
    elif(computer_choice == 1 and u_choice == -1):
        print("COMPUTER WINS!")

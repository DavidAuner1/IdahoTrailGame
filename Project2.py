#David Auner
#11/14/2020
#game that has has dice game, slots, and story line that has a credit system included
import random
from random import randint


def roll(num_sides):
    """finds random number for the number of sides"""
    number = random.randint(1,num_sides)
    if (num_sides > 64):
         print ("Error")
         return -1
    else:
         return number

def play_dice_game():
    """rng game that determines winner based on highest score and is able to rule a tie breaker """
    for score in range (6):
        player_one = roll(6)
        player_two = roll(6)
        
        if (player_one > player_two):
            print("Your roll: ")
            print(player_one)
            print("Enemy roll: ")
            print(player_two)
            return "player_one" 
            
        else:
            print("Your roll: ")
            print(player_one)
            print("Enemy roll: ")
            print(player_two)
            return "player_two"
            
    

def slots_board1():
    board = ['' , '' , '']
    items = ["$","@","*"]
    for i in range (0,3):
       board[i]= random.choice(items)
    return board
    
    
        


def play_slots_game():
    
    board = slots_board1()
    print(board)
    return board


def check_win(board):
    board_set= set(board)
    if len(board_set) == 2:
        return "half_win"
    if len(board_set) == 1:
        return "win"
    elif len(board_set) > 1 or len(board_set) < 1:
        return "lose"
    

def print_board(board):

    """This function will print a board to the console"""
    #sometimes retunrs none which i dont know why
    print(board)
    for index, row in enumerate(board):

        print('|'.join(row))

        if index < 2:

            print('-----')

    

def create_adventure():
    
    
    
    print("- - You have entered the old west - -")
    print("Bob is traveling and asks if you need a ride to the town north or south")
    set = input("Choose your direction: N or S: ").upper()
    if set == "N":
        print("North is two day trip do you want to still go north?")
        ask = input("Y/N ").upper()
        if ask == "Y":
            print ("Then we will travel north")
            print("- - It is now night - -")
            print ("When you are sleeping you wake up to growling")
            night= input("You see it is a wolf do you want to fight or run").upper()
            if night == "FIGHT":
                print("You were able to kill the wolf")
                print("the man is very happy and you travek into town")
                print("- - two days - -")
                town = input("Do you want to enter the casino: Y/N").upper()
                if town =="Y":
                    return "end"

                if town == "N":
                    print("you walk around town and find a gambling game")
                    print("the game requires you to pick the letter hidden under the cup")
                    cup = input("pick a,b,c").upper()
                    if cup == "A":
                        print("you have picked a that means you are able to return home ")
                        return "end"
                    if cup =="B":
                        print("option b was a bad choice")
                        print("* you are hit over the head with a stick *")
                        print("you wake up in a fighting pit you have to fight the biggest guy")
                        punch = input("you are puched what is your dodge: L or R").upper()
                        if punch =="L":
                            print("you are punched right in the face and knocked out")
                            return "die"
                        if punch == "R":
                            print("you dodge the punch and return a fatal punch to your opponent")
                            print(" you are praised by everyone and as a victory you enter a casino")
                            return "end"
                    if cup== "C":
                        print("option c was correct you must complete another task before your reward")
                        task = input("choose 1 or 2 your choice will determine your future")
                        if task == "1":
                
                            print("great choice before your reward please tell me where your from")
                            reward = input("from the N or S").upper()
                            if reward == "N":
                                print("there is no town in the north you are caught and killed")
                                return "die"
                            if reward == "S":
                                print("you are wlecomed in and given a tip about a casino")
                                welcome = input("do you want to enter the casino: Y/N").upper()
                                if welcome=="Y":
                                    return "end"

                                if welcome =="N":
                                    print("you walk three steps and die from a heart attack")
                                    return "die"
                        

                        

                        if task == "2":
                            print("Wrong choice which means you will have to get me my favorite green vase")
                            print("you enter the vase shop and have to persuade the shop owner ")
                            print("Shop owner - hello the green vase is not for sale")
                            print(" to buy this vase you have to risk you life for it")
                            print("you must sneak in the house of my rival and bring me his watch")
                            risk = input("you arrive at trhe house but will you run in the house or sneak: run or sneak").upper()
                            if risk =="RUN":
                                print ("Great choice you stole the watch and now you can get the green vase")
                                print("the man is very happy and lets you into the casino as a reward")
                                return "end"
                            if risk =="SNEAK":
                               print("you took to long and where caught")
                               return "die"



            if night == "RUN":
                print ("you run away succesfully but cant find Bob you must now survive")
                print ("your hunger sets in and you see some berries")
                berry= input("Do you eat the berries: Y/N").upper()
                if berry == "Y":
                    print("The berries where poisonous")
                    return "die"
                road =input("You find a road do you want to follow the path: left or right").upper()
                
                if road== "LEFT":
                    print("You travel for a mile and find yourself back at the city")
                    print("You enter the casino to play dice or slots")
                    return "end"
                if road == "RIGHT":
                    print("The road is very long and dry")
                    print("You die of heat exaustion")
                    return "die"

                


    if set == "S" or ask == "N":
        print("Then we will travel south")
            
    
        print ("- - 2 days have past - -")
        print("You enter a new town and you see a sherriff for higher poster with a hanging sherriff next to it")
        job= input("Do you want to become the sherriff: Y/N").upper()
        if job == "Y":
            print("You have now become the sherriff and are told about frequent robberys")
            print("- - A week has gone by- - ")
            rob = input("A robbery has occured and you confront the robber \n you have the robber at gunpoint do you shoot? Y/N ").upper()
            if rob == "Y":
                print("You are the towns hero and given a medal")
                print("The new talk of sherriff has led to a target being put on your head")
                print("You respond to a murder but do not know who teh killer is")
                inv = input("Do u want to check for clues you have to act fast because the house is on fire: Y/N").upper()
            if rob =="N":
                print("You arrest the robber and win a medal")
                casino = input("do u want to enter the casino: Y/N").upper()
                if casino == "Y":
                    return "end"
                if casino =="N":
                    print("You hear a bandit is in town and investigate")
                    print("You confront the robber and he pulls a gun")
                    print("the robber catches you off gaurd and shoots")
                    return "die"

                if inv== "Y":
                    print("You find a hat and the murdered person does not wear hats and the hat is custom made")
                    print("You walk around town into the hat shop and ask the owner who owns the hat")
                    find = input("the owner gives you an adress to the house of who owns the hat: should you travel to the \nhouse or look for more eveidence: Y/N").upper()
                    if find == "Y":
                        print("You go to the adress and knock on the door")
                        knock = input("Do you confront the man about the murder: Y/N").upper()
                        if knock == "Y": 
                            print("The man opens the door pointing a revolver and shoots you")
                            return "die"
                        if knock == "N":
                            print("You dont find any clues and the case is a dead end")
                            print("As the sherriff there are no crimes so you enter the casino")
                            return "end"
                    if find =="N":
                        print("You dont find any clues and the case is a dead end")
                        print("As the sherriff there are no crimes so you enter the casino")
                        return "end"
                if inv == "N":
                    print("You dont find any clues and the case is a dead end")
                    print("As the sherriff there are no crimes so you enter the casino")
                    return "end"
                
                    

             

        
        if job == "N":
            print("You travel around town and walk into a casino")
            return "end"
    
            
            
    
    





if __name__ == "__main__":
    

    name = input('What is your name?')
    print ("Welcome " + name + " to Retro Arcade!!!")

    keep_playing = True
    
    credit = 200
    

    

    while keep_playing:
        print("Credit Amount: "+str(credit) + " ")

        
        game_select = input("What is your desired path? \n(D)ice, (S)lots, (C)hoose your own adventure, or (Q)uit \ntype your choice using the capital letter inside (_): ").upper()
        
        if game_select == "D":
            print("Good luck roll higher than \nyour opponent to win credits,\nif you loose it will cost you")
            
            winner = play_dice_game()
            if winner =="player_one":
                credit += 30
                print ("- - Winner Winner Chicken Dinner - -")
            

            if winner =="player_two":
                credit -= 20
                print ("- - Looser - -")
            if credit <0:
                print ("Thank you for playing!!!")
                keep_playing = False
                
        if game_select == "S":
            board = play_slots_game()
            check = check_win(board)
            if check == "half_win":
               print("- - Winner - -")
               credit += 50
            if check =="win":
                print("* * Jack Pot * *")
                credit +=100
            elif check == "lose":
                credit -=25




            if credit <=0:
                print("Thank you for playing!!!")
                keep_playing = False

        if game_select == "C": 
            set = create_adventure()
            if set == "die":
             
                print ("Thank you for playing!!!")
                keep_playing = False
                break   
           
                

           
            


            

        if game_select == "Q":
            print ("Thank you for playing!!!")
            keep_playing = False



import random

# rules
print("Come let's play rock paper scissors with me!")
print("Rules are:")
print("0 for rock")
print("1 for paper")
print("2 for scissors")


## variables for emoji
rock = '🤜'
paper = '✋'
scissors = '✌'

# user participation
game_images=[rock,paper,scissors]
user_choice = int(input("Enter your choice: "))

# for invalid entry

if user_choice > 2 or user_choice < 0:
    print("Invalid choice")
    
#   GAME 
else:
    print("You chose:",game_images[user_choice])  #prints user's choice 
    my_choice = random.randint(0,2)  #generates computer's choice
    print("I chose:",game_images[my_choice]) #prints computer's choice

    if(my_choice == user_choice): #draw
        print("IT'S A TIE!")

    elif my_choice == 0 and user_choice == 2: #when user chose scissors and system choose rock 
        print("YOU LOSE! BETTER LUCK NEXT TIME")
        
    elif user_choice == 0 and my_choice == 2: #when system chose scissors and user choose rock
        print("HURRAY! YOU WON!!")
        
    # when system choses paper(1) and user chooses rock(0)
    # when system chooses scissors(2) and user chooses paper(1)
    
    elif my_choice > user_choice:
        print("YOU LOSE! BETTER LUCK NEXT TIME")


    # when user choses paper(1) and system chooses rock(0)
    # when user chooses scissors(2) and system chooses paper(1)
    
    elif user_choice > my_choice:
        print("HURRAY! YOU WON!!")
    

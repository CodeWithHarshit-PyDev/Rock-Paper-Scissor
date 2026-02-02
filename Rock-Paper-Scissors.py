import random
print("Welcome to the ROCK-PAPER-SCISSIOR GAME!!!")
print(
    "The rules are simple:\n"
    "• Rock crushes scissors\n"
    "• Scissors cut paper\n"
    "• Paper covers rock\n\n"
    "If both players choose the same shape,\n"
    "it's a tie and the round is replayed."
)
a=["Rock","Paper","Scissor"]
#taking random choice of computer
b=random.choice(a)

c=input("Should we start the game?(Yes or No)\n " \
" ")
i=50
#creating a loop so that player can play as per there choices
for i in range(i+1):
    if c=="yes" or c=="Yes" or c=="YES":
        print("Okay!! Great Choice!!")
        #rock paper or scissor from user
        d=input("Choose Rock,Paper or Scissiors!!➼➼")
        #if tie
        if d.lower()==b.lower():
            print(f"the computer has selected: {b}")
            
            print("it is an tie!!")
            #if user selected rock comparing with the computer for the winner or loser 
        elif d=="Rock"or d=="rock" or d=="ROCK":
            print(f"You have selected:{d}!")
            print(f"the computer has selected: {b}")
            if b=="Paper":
                print("U Lost!!!!!")
            else:
                print("U Won!")
                 #if user selected scissor comparing with the computer for the winner or loser 
        elif d=="Scissor"or d=="SCISSOR" or d=="scissor" or d=="scissors" or d=="SCISSORS" or d=="Scissors":
            print(f"You have selected:{d}!")
            print(f"the computer has selected: {b}")
            if b=="Rock":
                print("U Lost!!!!!")
            else:
                print("U Won!")
                 #if user selected paper comparing with the computer for the winner or loser 
        elif d=="Paper"or d=="paper" or d=="PAPER":
            print(f"You have selected:{d}!")
            print(f"the computer has selected: {b}")
            if b=="Scissor":
                print("U Lost!!!!!")
            else:
                print("U Won!")
        else:
            print("Please Choose valid object!!")
    elif c=="no" or c=="NO" or c=="No":
        print("Okay! No Problem u can quit!")
        break
    else:
        print("Please select yes or no")
    print("\n\n\n")
    l=input("Do u want to play again?")
    if l=="YES" or l=="Yes" or l=="yes":
        print("Okay let's start again!!")
        i=i+1
    else:
        print("ok see u next time!")
        break


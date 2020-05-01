'''Stone Paper Scissors E-Game by SARWAR ALI(github.com/sarwar1227) using Python
           Technologies Required To Run this Code : Pyhton(32/64 bit) version 2/3+
INSTRUCTIONS TO PLAY THIS GAME :
1.Computer Randomly chose between ston/paper/scissors
2.You are asked to chose your option
3.Based on some camparisons Winner of the game is decided
GOOD LUCK FOR THE GAME !!'''
import random,os,sys
name=input("Enter Your Name : ")
choices=['stone','paper','scissors']
def display():
    print("Hello",name,",Welcome To Stone Paper Scissors Game")
    comp_choice=random.choice(choices)
    try:
        x=int(input("Choices Available\n1.Stone\n2.Paper\n3.Scissors\nEnter Your Choice:"))
    except ValueError:
        print("Only integer Value Allowed !!")
        input()
        play_again()
    if (x==1):
        user_choice='stone'
    elif (x==2):
        user_choice='paper'
    elif (x==3):
        user_choice='scissors'
    else:
        print("Invalid Choice")
    if (comp_choice=='stone' and user_choice=='scissors') or (comp_choice=='paper' and user_choice=='stone') or (comp_choice=='scissors' and user_choice=='paper'):
        print("Computer Choice:",comp_choice,"\n",name,"Choice:",user_choice,"\nBad Luck....Computer Wins !!")
        if comp_choice=='stone':
            print("Computer's Stone Crushed Your Scissors !!")
        elif comp_choice=='paper':
            print("Computer's Paper Blocked Your Stone")
        elif comp_choice=='scissors':
            print("Computer's Scissors Cut Down Your Paper")
        input()
        play_again()
    elif (user_choice=='stone' and comp_choice=='scissors') or (user_choice=='paper' and comp_choice=='stone') or (user_choice=='scissors' and comp_choice=='paper'):
        print("Computer Choice:",comp_choice,"\n",name,"Choice:",user_choice,"\nCongratulations ",name,"!!  You Won the Game !!")
        if user_choice=='stone':
            print("Your Stone Crushed Computer's Scissors !!")
        elif user_choice=='paper':
            print("Your Paper Blocked Computer's Stone")
        elif user_choice=='scissors':
            print("Your Scissors Cut Down Computer's Paper")
        input()
        play_again()
def play_again():
    ch=input("Want to play again? (y/Y) for Yes (n/N) for No:")
    if ch in ['y','Y']:
        os.system("cls")
        display()
    elif ch in ['n','N']:
        print("Thanks For Playing...The Game!!\nPress Any Key To End...........")
        input()
        sys.exit("Thank For Playing !!")
    elif ch not in ['y','Y','n','N']:
        print("Invalid Input")
        play_again()
display()

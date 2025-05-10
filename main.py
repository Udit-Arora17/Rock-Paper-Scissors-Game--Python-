#main.py
print("Let's play a game of ROCK , PAPER and SCISSORS")
print("You have to enter Rock , Paper or Scissors")
import random
computer = random.choice([1,2,3])
user=input("Enter:")
userDict={"Rock":1,
          "Paper":2,
          "Scissors":3}
reverseDict={1:"Rock",
             2:"Paper",
             3:"Scissors"}
print(f"You chose {user}\nComputer chose {reverseDict[computer]}")
result=userDict[user]  #{} are used for assigning dictionaries and [] are used for calling any key of dictionary
if (computer==1 and result==2):
    print("You win!")
elif (computer==1 and result==3):
     print("You lost, Computer win\nBetter luck next time")
elif (computer==1 and result==1):
    print('Draw')
elif (computer==2 and result==3):
    print("You win!")
elif (computer==2 and result==1):
    print("You lost, Computer win\nBetter luck next time")
elif (computer==2 and result==2):
     print('Draw')
elif (computer==3 and result==2):
    print("You lost, Computer win\nBetter luck next time")
elif (computer==3 and result==1):
     print("You win")
elif (computer==3 and result==3):
    print('Draw')

import random 
'''
1 for snake 
-1 for water 
0 for gun
'''
computer = random.choice([0, -1, 1]) #random choice for computer from 1 , 0 and -1
youstr = input("Enter your choice: ")    #taking input from the player

youDict = {"s" : 1 , "w" : -1 , "g" : 0}
you = youDict[youstr]
reverseDict={1: "snake", -1: "water", 0: "gun"}

print(f"you chose {reverseDict[you]} \n computer chose {reverseDict[computer]}")

if(computer== you):
    print("Its a draw!!")

    # the below logic is written on the basis of the value of computer - you  
else:
    if ((computer - you)== 2 or (computer - you)== -1 ):
        print ("You win!!")
    else :
        print ("You win!!")
'''
else:
   if(computer == -1 and you == 1):(computer - you)= -2
    print("You Win!! ")

   elif(computer == -1 and you == 0):(computer - you)= -1
    print("You Lose!!")

   elif(computer == 1 and you == -1):(computer - you)= 2
    print("You Lose!!")

   elif(computer == 1 and you == 0):(computer - you)= 1
    print("You Win!!")

   elif(computer == 0 and you == 1):(computer - you)= -1
    print("You Lose!!")

   elif(computer == 0 and you == -1):(computer - you)= 1
    print("You Win!!")

   else:
    print("Something went wrong")
''' 



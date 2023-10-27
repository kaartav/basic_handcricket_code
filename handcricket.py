import random
print("Time for toss for the T1(1over match) match \n because any longer would be boring\nONLY NUM IN[1,6]")
toss=input("Enter heads(H) or tails(T):\n")
coin=["H","T"]
ranum=[1,2,3,4,5,6]
bowlingspeeds=["144.5kmph","c m/s","96.5kmph","62mph","112 kmph","60kmph","111.11kmph","150.6kmph"]
userscore=0
comscore=0

randomtoss=random.choice(coin)
print(f"And its {randomtoss}\n")
if(toss==randomtoss):
    a=input("you won the toss,choose B1 to bat or b1 to bowl\n")
else:
    a="b1"
    print("Comuter chooses to bat \n")
if(a=="B1"):
    for i in range(1,7):
        speed=random.choice(bowlingspeeds)
        userval=int(input(f"{7-i} balls left ## Some useless info i am bowling at {speed} ##\nInput your batting value:\n"))
        comvalue=random.choice(ranum)
        if(userval != comvalue):
            userscore=userscore+userval
            print("\n")
            continue
        if(userval == comvalue):
            print(f"Your out!!!                    Your score is {userscore}")
            break
    else:
        print(f"you have batted well,Your score is {userscore}")
    print("I ready to bat\n")
    for i in range(1,7):
        userval=int(input(f"{7-i} balls left \nInput your bowling value:\n"))
        comvalue=random.choice(ranum)
        if(userscore<comscore):
            break
        if(userval != comvalue):
            
            comscore=comscore+comvalue
            print(f" My input is {comvalue},com 2 have {userscore-comscore} to score")
            if(userscore-comscore<=0):
                break
            
            print("\n")
            continue
        if(userval == comvalue):
            print(f"I am out!!!                 My score is {comscore}")
            break
    if(userscore>comscore):
        print("SO YOU WIN!!!")
    elif(userscore<comscore):
        print(f"You lost,cause I scored {comscore}")
    else:
        print("its a draw")
##########################################################################################
if(a=="b1"):
    for i in range(1,7):
        
        userval=int(input(f"Input your bowling value,              {7-i} balls left\n"))
        comvalue=random.choice(ranum)
        if(userval != comvalue):
            comscore=comscore+comvalue
            print(f"My batting value is {comvalue}")
            print("\n")
            continue
        if(userval == comvalue):
            print(f"I am out!!!                My score is {comscore}")
            break
    else:
        print(f"I have batted well,My score is {comscore}")
    print("I need to bowl now\n")
    for i in range(1,7):
        speed=random.choice(bowlingspeeds)
        print(f"I am bowling at a speed of {speed}")
        userval=int(input(f"Input your batting value,              {7-i} balls left\n"))
        comvalue=random.choice(ranum)
   
        if(userval != comvalue):
            userscore=userscore+userval
            print(f"You have {comscore-userscore} to score and my input was {comvalue}")
            if(comscore-userscore<=0):
                break
            print("\n")
            continue

        if(userval == comvalue):
            print(f"You are out!!!                 Your score is {userscore}")
            break
    if(userscore>comscore):
        print("SO You WIN!!!")
    elif(userscore<comscore):
        print(f"YOU LOST,cause I scored {comscore}")
    else:
        print("its a draw")
        
    
        
        
    
    
    
    

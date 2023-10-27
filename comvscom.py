import random
ranum=[1,2,3,4,5,6]
com2score=0
com1score=0
wincom1=0
wincom2=0
draws=0
li=[]
#com1 always bats first
for y in range(0,10):
    list=[]
    for i in range(1,7):
            com1val=random.choice(ranum)
            com2val=random.choice(ranum)
            list.append(com1val)
            
            if(com1val != com2val):
                com1score=com1score+com1val
                
                continue
            if(com1val == com2val):
                
                break
    
            

    for i in range(1,7):
            com2val=random.choice(ranum)
        
            com1val=random.choice(ranum)
            
            if(com1val != com2val):
                
                com2score=com2score+com2val
               
                if(com1score-com2score<=0):
                    break
               
                continue
            if(com1val == com2val):
                
                break
    if(com1score>com2score):
            
            wincom1=wincom1+1
            li.append(list)
    elif(com1score<com2score):
            
            wincom2=wincom2+1
    else:
        draws=draws+1
print(wincom1,wincom2,draws)

for i in range(0,len(li)):
    for j in range(0,len(li)):
        if(li[i]==li[j] and i<j):
            print(li)
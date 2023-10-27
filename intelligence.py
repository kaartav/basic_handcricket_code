def comvscom(target,balls,howmanytimes):
    import random
    ranum=[1,2,3,4,5,6]
    
    comscore=0
    win=0
    loss=0
    draws=0
    li=[]
    for y in range(0,howmanytimes):
        list=[]
        comscore=0

        for i in range(1,balls):
            com2val=random.choice(ranum)
        
            com1val=random.choice(ranum)
            
            if(com1val != com2val):
                list.append(com1val)
                
                comscore=comscore+com1val
               
                if(comscore-target<=0):
                    break
               
                continue
            if(com1val == com2val):
                
                break
        if(comscore>target):
            
            win=win+1
            li.append(list)
        elif(comscore<target):
            
            loss=loss+1
        else:
            draws=draws+1
    return(li)
def batting(runsrequired,balls):
    print("hi")#################################################
print(comvscom(5,4,7))
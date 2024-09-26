def demand(p) :
    return 10-(1.05*p) 

def supply(p) :
    return 1+(1.06*p) 

def dominates(demand,d_domination,supply,s_domination) :
    if(demand > supply ) :
        d_domination = True
        # return d_domination
    # elif(demand == supply) :
    #     return 1  
        return True
    else :
        s_domination = True
        # return s_domination 
        return True
    
    return False
    
def process(d_domination,s_domination,p,initial): 
    p += 0.5*p 
    prev = initial
    target = 0
    if(prev == d_domination ) :
        target = s_domination 
    else :
        target = d_domination 
    flag = 0
    while(dominates(demand(p),d_domination,supply(p),s_domination)):
        if(target == True) :
            flag = 1 
            break 
        p += 0.5*p  

    if(flag == 1) :
        print("equlilirium  cannot be achieved") 
        return -1 
    
    return p 

    



def main() :
    d_domination = False 
    s_domination = False 
    ## initially 
    p = 1 
    state = dominates(demand(p),d_domination,supply(p),s_domination)
    # if(state == False) :
    #     return p 
    if(d_domination == True) :
        print(process(d_domination,s_domination,p,d_domination))

    else :
        print(process(d_domination,s_domination,p,s_domination))
     










    
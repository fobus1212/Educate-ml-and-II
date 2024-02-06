n=int(input()) 

def guess(n): 
    if n/2<1: 
        b=(n) 
    elif n>0 :   
        for i in range(n+1): 
            if i*i== n :  
                b=i  
                i+=1  
                if b is not None: 
                    return b 
            elif i==n: 
                b="Сложно , сложно , не могу"

                
    return b  
    
 
a=guess(n)  
print(a)

                        



 


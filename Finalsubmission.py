import math

l40=["Nancy Pollock","Mary Doyle","Doug Redpath","Jill Brown","Trevor Chappell","Peter","Jack Holmes"]
while True:    
    name1 = input("Enter first person name[Please spell correctly with first alphabet in upper case]\n")
    name2 = input("Enter second person name[Please spell correctly with first alphabet in upper case]\n")
    if name1 not in l40 or name2 not in l40:
        print("Please spell correctly with first alphabet in upper case\n")
        continue
    else:
        break



def getSimilarity(name1,name2): #getSimilarity function
    f=open("C:/Users/prana/.spyder-py3/reviews.txt","r")
    d5 = {}
    d5=eval(f.read())  #Reading Dictionary
    
    
    
    k1 = d5.keys()
    v1 = d5.values()
    
    
   
    namekeys = list(d5.keys()) #converting into list for processing
    
    
    namevalues = list(d5.values())

    #############################
    
    
    
    nindex=0
    while nindex<len(namekeys):
        if name1 == namekeys[nindex]: #getting name index
            break
        nindex=nindex+1
        
        
        
        
    nindex2=0
    while nindex2<len(namekeys):
        if name2 == namekeys[nindex2]:
            break
        nindex2=nindex2+1
            
            
            
    l0=[] #list of keys for expected persons
    v0=[]   #list of values for expected persons
            
            
            
            ################
            #creating list of movie names for desired people and passing it for further processing
            
            
    if nindex == 0 or nindex2 == 0:
        l1=list(namevalues[0].keys())
        l0.append(l1)
                
                
                
    if nindex == 1 or nindex2 == 1:
        l2=list(namevalues[1].keys())
        l0.append(l2)
                    
    if nindex == 2 or nindex2 == 2:
        l3=list(namevalues[2].keys())
        l0.append(l3)
                        
                        
    if nindex == 3 or nindex2 == 3:
        l4=list(namevalues[3].keys())
        l0.append(l4)
                            
                            
    if nindex == 4 or nindex2 == 4:
        l5=list(namevalues[4].keys())
        l0.append(l5)
                                
                                
    if nindex == 5 or nindex2 == 5:
        l6=list(namevalues[5].keys())
        l0.append(l6)
                                    
                                    
    if nindex == 6 or nindex2 == 6:
        l7=list(namevalues[6].keys())
        l0.append(l7)






        #creating list of movie review values for desired people and passing it for further processing


    if nindex == 0 or nindex2 == 0:
        v1=list(namevalues[0].values())
        v0.append(v1)


    if nindex == 1 or nindex2 == 1:
        v2=list(namevalues[1].values())
        v0.append(v2)


    if nindex == 2 or nindex2 == 2:
        v3=list(namevalues[2].values())
        v0.append(v3)


    if nindex == 3 or nindex2 == 3:
        v4=list(namevalues[3].values())
        v0.append(v4)


    if nindex == 4 or nindex2 == 4:
        v5=list(namevalues[4].values())
        v0.append(v5)


    if nindex == 5 or nindex2 == 5:
        v6=list(namevalues[5].values())
        v0.append(v6)


    if nindex == 6 or nindex2 == 6:
        v7=list(namevalues[6].values())
        v0.append(v7)


#Processing

    length1=len(l0)
    
    total=[]
    k=0
    while k<length1:
       
        m=0
        subtotal=0
        sqtotal=0
        while m<len(l0[k]):
            temp1 = l0[k][m]
            
            k1=0
            while k1<length1:
                m1=0
                while m1 < len(l0[k1]):
                    if temp1 == l0[k1][m1]:
                        total.append(namekeys[k])
                        total.append(l0[k1][m1])
                        total.append(namekeys[k1])
                        subtotal = subtotal + ((v0[k][m] - v0[k1][m1])**2)
                        sqtotal=math.sqrt(subtotal)
                        total.append(sqtotal)
                                  
                    m1 = m1+1    
                        
                k1 = k1+1
            m=m+1
                        
        k=k+1
                        
        return total[-1]




#####Function2
z=[]

def getSimilarities(name1):   #getSimilarities
    f=open("C:/Users/prana/.spyder-py3/reviews.txt","r")
    d5 = {}
    d5=eval(f.read())  #Reading Dictionary
    
    
    
    k1 = d5.keys()
    v1 = d5.values()
    
    
   
    namekeys = list(d5.keys()) #converting into list for processing
    
    
    namevalues = list(d5.values())

    #############################
    
    
    
    nindex=0
    while nindex<len(namekeys):
        if name1 == namekeys[nindex]: #getting name index
            break
        nindex=nindex+1
        
        
    nindex2=0       
    while nindex2 < 7:
        if nindex2 == nindex:
            nindex2=nindex2+1
            continue
        l0=[] #list of keys for expected persons
        v0=[]   #list of values for expected persons
            ################
            #creating list of movie names for desired people and passing it for further processing

        if nindex == 0 or nindex2 == 0:
            l1=list(namevalues[0].keys())
            l0.append(l1)
           
                
                
        if nindex == 1 or nindex2 == 1:
            l2=list(namevalues[1].keys())
            l0.append(l2)
            
        if nindex == 2 or nindex2 == 2:
            l3=list(namevalues[2].keys())
            l0.append(l3)
            
                        
        if nindex == 3 or nindex2 == 3:
            l4=list(namevalues[3].keys())
            l0.append(l4)
          
                            
        if nindex == 4 or nindex2 == 4:
            l5=list(namevalues[4].keys())
            l0.append(l5)
           
                                
        if nindex == 5 or nindex2 == 5:
            l6=list(namevalues[5].keys())
            l0.append(l6)
           
                                    
        if nindex == 6 or nindex2 == 6:
            l7=list(namevalues[6].keys())
            l0.append(l7)
            





        #creating list of movie review values for desired people and passing it for further processing


        if nindex == 0 or nindex2 == 0:
            v1=list(namevalues[0].values())
            v0.append(v1)
           

        if nindex == 1 or nindex2 == 1:
            v2=list(namevalues[1].values())
            v0.append(v2)
            

        if nindex == 2 or nindex2 == 2:
            v3=list(namevalues[2].values())
            v0.append(v3)
           

        if nindex == 3 or nindex2 == 3:
            v4=list(namevalues[3].values())
            v0.append(v4)
            

        if nindex == 4 or nindex2 == 4:
            v5=list(namevalues[4].values())
            v0.append(v5)
          

        if nindex == 5 or nindex2 == 5:
            v6=list(namevalues[5].values())
            v0.append(v6)
           

        if nindex == 6 or nindex2 == 6:
            v7=list(namevalues[6].values())
            v0.append(v7)
            

#Processing

        length1=len(l0)
    
        total=[]
        k=0
        while k<length1:
       
            m=0
            subtotal=0
            sqtotal=0
            while m<len(l0[k]):
                temp1 = l0[k][m]
            
                k1=0
                while k1<length1:
                    m1=0
                    while m1 < len(l0[k1]):
                        if temp1 == l0[k1][m1]:
                            total.append(namekeys[k])
                            total.append(l0[k1][m1])
                            total.append(namekeys[k1])
                            subtotal = subtotal + ((v0[k][m] - v0[k1][m1])**2)
                            sqtotal=math.sqrt(subtotal)
                            total.append(sqtotal)
                                  
                        m1 = m1+1    
                        
                    k1 = k1+1
                m=m+1
                        
            k=k+1
            
            
            
        #print(total[-1])                
        z.append(total[-1])
        nindex2=nindex2+1
    
    return z,namekeys 






print("\nComparison between two") 
print(getSimilarity(name1,name2)) #result statement for comparison between 2 




print("\nComparison between one and remaining all")
answers,namekeys3=getSimilarities(name1)   

h=0
while h<7:
    if namekeys3[h] == name1:
        deleteindex=h
    h=h+1
 

namekeys3.pop(deleteindex)

a=0
while a < 6:
    print(name1,"\t",namekeys3[a],"\t",answers[a]) #result for comparison between one and remaining all 
    a=a+1        


                                      
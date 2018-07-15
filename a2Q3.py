#Method b Net score of each file.
import string
import os
os.chdir("C:/Users/prana/Desktop/Python/HW2/yelp100")
import glob as glob
files1 = glob.glob("*.txt")
t1=[]

f=open("C:/Users/prana/Desktop/Python/HW2/positive.txt")
pos=f.read()
p1=pos.split()
plength=len(p1)
#print(p1)
#print(plength)

f1=open("C:/Users/prana/Desktop/Python/HW2/negative.txt")
neg=f1.read()
p2=neg.split()
#print(p2)
plength2=len(p2)
#print(plength2)


for fo in files1:
    with open(fo) as infile:
        text1=infile.read()
        t1=text1.split()
        n=len(t1)
        i=0
        positive=0
        print("File",fo,end=",")
        while i < n:
            j = 0
            while j < plength:
                exclude1 = set(string.punctuation)
                t1[i] = ''.join(ch for ch in t1[i] if ch not in exclude1)
                if t1[i] == p1[j]:
                    #print(t1[i])
                    positive=positive + 1
                    #print(positive)
        
                j=j+1
        
            i=i+1
        
        k=0
        negative=0
        while k < n:
            l=0
            while l < plength2:
                exclude2 = set(string.punctuation)
                t1[k] = ''.join(ch for ch in t1[k] if ch not in exclude2)
                if t1[k] == p2[l]:
                    #print(t1[k])
                    negative=negative-1
                    #print(negative)
        
                l=l+1
        
            k=k+1
        
        score=positive+negative        # positive = positive + (-negative)
        #print("-------------")
        print(" Net Score is",score)
        
        
        
 ##############################################   
    
#Method C
from textblob import TextBlob 
import os
os.chdir("C:/Users/prana/Desktop/Python/HW2/yelp100")
import glob as glob
files1 = glob.glob("*.txt")
for fo in files1:
    with open(fo) as infile:
        text=infile.read()
        b = TextBlob(text)
        print("Sentiment score of ",fo,"is:",b.sentiment)
        
        
        
        
        

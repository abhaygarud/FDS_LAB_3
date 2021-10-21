a=[]#student play cricket
b=[]#student play badminton
c=[]#studet play football

#code to apped the palyer in the list
#code for cricket
for i in range (int(input("enter the number of student playing 'cricket' :"))):
    a.append(input("enter the name of the player :"))
print("listof cricket:",a)

#code for badminton
for i in range (int(input("enter the number of student playing 'badminton' :"))):
    b.append(input("enter the name of the player :"))
print("list of badminton :",b)

#code for football
for i in range (int(input("enter the number of student playing 'footbal' :"))):
    c.append(input("enter the name of the player :"))
print("list of football :",c)

#student who plays both cricket and badminton
def a1(a,b):
    temp=[]
    for i in a:
        if i in b:
            temp.append(i)
    print("No of student who play both 'cricket' and ' badminton' are :",temp)
# student who play either cricker of footbal but not both
def b1(a,b):
    temp=[]
    for i in a:
        if i not in b:
            temp.append(i)
    for j in b:
        if j not in a:
            temp.append(j)
    
    print("student who play either cricker of footbal but not both :",temp)

# student who play neither cricket nor badminton
def c1(a,b,c):
    X=[]
    Y=[]
    for i in c:
        X.append(i)
    for j in b:
        Y.append(j)
    for k in a: 
        if k not in b:
            Y.append(k)
    for i in Y:
        if i in X:
            X.remove(i)
    print("student who play neither cricket nor badminton",X) 

#student who play cricket and football but not badminton        
   
def d(a,b,c):
    X=[]
    Y=[]
    for i in a:
        X.append(i)
    for k in c:
        X.append(k)
    for j in b:
        if j in X:
            X.remove(j)
    print("student who play cricket and football but not badminton",X)




b1(a,b)
a1(a,b)
c1(a,b,c)
d(a,b,c)
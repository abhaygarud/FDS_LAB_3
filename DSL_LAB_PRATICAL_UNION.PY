def main():
    a = [] # student playing cricket
    b = [] # student playing badminton
    c = [] # student playing football

    for i in range(int(input("number of student playing 'cricket' are :"))):
        a.append(input("name of the student playing cricket :"))
    print("cricket :",a)
    for j in range (int(input("number of student playing 'badminton' are :"))):
        b.append(input("name of the student playing badminton :"))
    print("badminton :",b)
    for k in range (int(input("number of student playing 'football' are :"))):
        c.append(input("name of the student playing football :"))   
    print("footbal :",c)
    print(f"name of student playing both cricket and badminton : {(union(a,b))}")
    print(f"name of student play either cricket and badminton but not both : {(y(a,b))}")
    print(f"name of student neither playing cricket nor footballl :{(z(a,b,c))}")
    print(f"number of student neither playing cricket nor footballl :{len(z(a,b,c))}")
    print(f"Number of students who play Cricket and Football but not badminton : {x(a,b,c)}")
def union(a,b):
    a_b=list(a)
    for i in b:
        if i not in a:
            a_b.append(i)
    return a_b

def y(a,b):
    a_b=[]
    for i in  a:
        if i not in b:
           a_b.append(i)
    for j in b:
        if j not in a:
            a_b.append(j)
    return a_b
def z(a,b,c):
    X=[]
    Y=[]
    for i in a:
        X.append(i)
    for j in b:
        if j not in X:
            Y.append(j)
    for k in c:
        if k not in X:
            Y.append(k)
    return Y
def x(a,b,c):
    X=[]
    Y=[]
    for i in a:
        if i not in c:
            X.append(i)
    for j in b:
        if j in X:
            X.remove(j)


main()


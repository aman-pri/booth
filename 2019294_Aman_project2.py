a1=int(input("enter first number in decimal format: \n"))
a2=int(input("enter second number in decimal format: \n"))
a3=abs(a1)
a4=abs(a2)
if a3<a4:
    b1="{0:b}".format(a4)
    b2="{0:b}".format(a3)
else:
    b1="{0:b}".format(a3)
    b2="{0:b}".format(a4)
p1=b1.find("1")
p2=b2.find("1")
b1=str(b1)[p1:]
b2=str(b2)[p2:]
l1=len(b1)
l2=len(b2)
if(l1>l2):
    d=l1-l2
    b2=("0"*d)+b2
    l=l1
else:
    d=l2-l1
    b1=("0"*d)+b1
    l=l2
if l<4:
  x=4-l
  l=4
  b1=x*"0"+b1
  b2=x*"0"+b2
sb1='0'
sb2='0'

if a1<0:
    sb1='1'
if a2<0:
    sb2='1'
    
    
print("FIRST BINARY NUMBER IS: ",sb1, b1)
print("SECOND BINARY NUMBER IS: ",sb2, b2)

a="0"*l
n=l
m=b1
q=b2
qn='0'
print(a, "\t", q, "\t", qn)

f=a+q

def rightshift():
    print("\t\t\t\tPERFORMING RIGHT SHIFT\n")
   
    global q
    global a
    global qn
    global l
    #print("a, q",a, q)
    f=a+q
    fl=len(f)
    res=""
    rstr=f[::-1]
    first=rstr[0]
    qn=first
    rstr=rstr[1:]
    f=rstr[::-1]
    f=(first+f)
    a=f[:l]
    q=f[l:]
    print(a, "\t", q, "\t", qn)


def add():
    global f
    global a
    global q
    global qn
    global b1
    global l
    
    print("\t\t\t\tA=A+M\n")
    #print("a, m", a, b1)
    sum = bin(int(a,2) + int(b1,2))
    a=sum
    a=a[2:]
    if len(a)!=l:
        ab=a[::-1]
        ab=ab[0:l]
        a=ab[::-1]
    
    print(a, "\t", q, "\t", qn)


def twoscomp(str): 
    n = len(str) 
  
    
    i = n - 1
    while(i >= 0): 
        if (str[i] == '1'): 
            break
  
        i -= 1
  
    
    if (i == -1): 
        return '1'+str
  
    
    k = i - 1
    while(k >= 0): 
          
        
        if (str[k] == '1'): 
            str = list(str) 
            str[k] = '0'
            str = ''.join(str) 
        else: 
            str = list(str) 
            str[k] = '1'
            str = ''.join(str) 
  
        k -= 1
  
   
    return str






def subtract():
    global f
    global a
    global q
    global qn
    global m
    global l

    a=f[:l]
    print("\t\t\t\tA=A-M\n")
    m=twoscomp(m)
    sum = bin(int(a,2) + int(m,2))
    a=sum
    
    a=a[2:]
    la=len(a)
    if la<l:
        diffe=l-la
        a=diffe*"0"+a
    print(a, "\t", q, "\t", qn)

while n>0:
        print(q)
        rq=q[::-1]
        ql=rq[0]
        print("Q=",ql)
        print("Q-1=",qn)
        if (ql=='0') and (qn=='0'):
            (rightshift())
        elif (ql=='1') and (qn=='1'):
            (rightshift())
        elif (ql=='1') and (qn=='0'):
            subtract()
            (rightshift())
        elif (ql=='0') and (qn=='1'):
            (add())
            (rightshift())
        else:
            break
        n=n-1
t=a1*a2
t1="{0:b}".format(t)
lt=len(t1)

ans=a+q
#pos=ans.find("1")
#ans=ans[pos:]
if lt>len(ans):
    ans=ans[::-1]
    ans=ans[:lt]
    ans=ans[::-1]
else:
    pos=ans.find("1")
    ans=ans[pos:]
sb='0'
if a1*a2<0:
    sb='1'
    print("\nFINAL ANSWER MULTIPLYING:  \n", b1,"and", b2,"  IS\n",sb,ans,"  = -", int(ans, 2))
elif a1*a2>0:
    sb='0'
    print("\nFINAL ANSWER MULTIPLYING:  \n", b1,"and", b2,"  IS\n",sb,ans,"  = ", int(ans, 2))
elif a1*a2==0:
    ans="0"
    print("\nFINAL ANSWER MULTIPLYING:  \n", b1,"and", b2,"  IS\n",sb,ans,"  = ", int(ans, 2))
print("MOST SIGNIFICANT BIT IS SIGNED BIT")


    




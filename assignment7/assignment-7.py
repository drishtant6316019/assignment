# #1. area of circle
 def area():
    r=int(input("enter r"))
    a=3.14*r*r
    print(a)
area()
#fx.perfect and prove it perfect


def    perfect(x)
 perfect(n):
    sum = 0
    for i in range (1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
         print("perfect number:",n)

for x in range(1,1001):
   perfect(x)

#print multiplication table of 12 using reccursion
def table(n,i):
    print (n*i)
    i=i+1
    if i<=10:
        table(n,i)
table(12,1)

#write a fx. to cal the power
def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
print(power(6,2))



#5. write a fx. to find a fact.
n=5
def rec(x):
    if (x==1 or x==0):
        return 1        #base case
    else:
        f= x*rec(x-1)   #reccase
        return f
fact=rec(n)
print(fact)
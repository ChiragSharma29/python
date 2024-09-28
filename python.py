age =int(input("enter a number"))
if(age>18)
def xyz(num,*args):
    print(num)
    print("----")
    print(args)
    xyz(1,2,3,4,5,6,7,8,9)
sum=10
def xyz(a,b):
    global sum
    sum=a+b
    return sum
abc=xyz(1,2)
print(abc)
print(sum)
def add(n):
    sum=0
    while(n>0):
        sum+=n 
        n-=1
        return sum

def add(n):#recursion
    if (n==1):
        return 1
    return (n)+add(n-1)
print(add(10))

def fac(n):#factorial
    if (n==1):
        return 1
    return (n)*fac(n-1)
print(fac(5))

def fib(n):#fibonacci series
    if n<=0:
        return "positive integer"
    elif n ==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
xyz =fib(10)
for i in range(1,11):
    print(fib(i),end=' ')

square =lambda x:x**2 #square using lambda function
print(square(5))

add =lambda a,b:a+b 
print (add(1,2))

add =lambda a,b:a if a>b else b 
print(add(1,2))

def abc(function):
    def wrapper():
        function()

    return wrapper
@abc
def xyz():
    print("ouiuhljkj")
xyz()
//////////////#
def abc(function):
    def wrapper():
        function()

    return wrapper()
@abc
def xyz():
    print("ouiuhljkj")

import time 
# print(time.time())

def timemeasure(func):
    def wrapper():
        start =time.time()
        result=func()
        end=time.time()
        print(end-start)
        return result
    return wrapper
        
@timemeasure
def pause():
        time.sleep(2)
        print("pause function ended")

@timemeasure
def quick():
    print("quick function ended")    

pause()
quick()

import time 
def timemeasure(func):
    def wrapper(args,*kwargs):
        start =time.time()
        result=func(args,*kwargs)
        end=time.time()
        print(end-start)
        return result
    return wrapper
@timemeasure
def sum(n):
 if n<=1:
    return 1
 return n+sum(n-1)
print(sum(10))

xyz=(1,3,4,6,7,8)
print(len(xyz))#length function
print(type(xyz))#datatype function
xx="15453"
num=int(xx)
print(type(num))
print(len(xx))
yy=146643
str=str(yy)
print(type(yy))
List=[1,4,6,7,9,9,5,2,0]
print(sum(list))
yy=list.sort()#it doesnt return the list
yy=sorted(list)

print(min(List))
print(max(List))

import vaderSentiment 
analyzer= vaderSentiment.sentimentIntensityAnalyzer()

def analyze(text):
     try:
        sentiment=analyzer.polarity_scores(text)
       # print(sentiment)

     if sentiment["compound"]>=0.05:
        print("positive")
     elif sentiment["compound"]<=-0.05:
        print("negative")
     else:
        print("neutral")

     expect; 
     Exception as e:
     print(e)
    
text=input("please enter a text")
analyze(text)

1
22
333
4444
x=int(input("Enter a value"))
for i in range(1,x+1):
 for j in range(1,i+1):
  print(i,end="")
  
Palindrome:
n=int(input("Enter a value:"))
temp=n
rev=0
while n!=0:
 rem=n%10
 rev=rev*10+rem
 n=int(n/10)
if rev == temp:
 print("It is a palindrome")
else:
 print("It is not a palindrome")
 
 Amstrong Number:
 n=int(input("Enter a value:"))
 a=len(n)
 temp=n
 sum=0
 while n>0:
  rem=n%10
  sum=sum+rem**a
  n=n/10
 if temp==sum:
  print("Number is an amstrong")
 else:
  print("Number is not an amstrong")
  
  
  Area of triangle,square,rectangle
l=int(input())
b=int(input())
h=int(input())
area_t=0.5*b*h
print(area_t)
area_r=l*b
print(area_r)
s=int(input())
area_s=s*s
print(area_s)



swap 3 numbers:
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))
if a>b:
  a,b=b,a
if a>c:
  a,c=c,a
if b>c:
  b,c=c,b
print(a,"is lessthan",b,"is lessthan",c)

Fibonacci series:
a=0
b=1
n=int(input())
if n>=2:
 print(a,b)
 for i in range(n-2):
  c=a+b
  a=b
  b=c
 print(c)
else:
 print("Enter a valid number")


 
  
  

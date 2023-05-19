son=int(input("son kiriting "))
if son%2==0 and son!=0:
    print("juft")
elif son==0 :
    print("0 kiritildi")
else: 
    print("toq")


son=int(input("son kiriting "))
if son%5==0 and son%3==0:
    print("Fizz Buzz")
elif son%5==0:
    print("Fizz")
elif son%3==0:
    print("Buzz")
else :
    print("zzuBzziF") 

a=int(input("1-son kiriting "))
b=int(input("2-son kiriting "))
c=int(input("3-son kiriting "))
if a>b:
    print(a,"-max")
elif a>c:
    print(a,"-max")
elif c>a:
    print(c,"-max")
elif c>b:
    print(c,"-max")
elif b>a:
    print(b,"-max")
elif b>c:
    print(b,"-max")
    

a=1500
while a<2700:
    if a%5==0 and a%7==0:
        print(a)
    a+=1
    

son=int(input("son kiriting  "))
a=1
while a<=son:
    print("*"*a)
    a+=1


son=int(input("son kiriting  "))
a=0
s=1
while s<=son:
    a=a+s
    s=s+a
    print(a,end=" ")
    if s<=60:
     print(s,end=" ")


soz=str()
mol=str()
while True:
 mol=input(">>")
 if mol=="stop":
      soz=soz+"."
      break  
 soz=soz+" "+mol
 print(soz)
print(soz)

soz=input("yozing")
a=0
b=0
i=0
while a<=len(soz):
 if soz[i].isalpha():
    a+=1
 elif soz[i].isdigit():
    b+=1

 i+=1
print(a)
print(b)

#  amaliyot


soz=input("yozing: ")
a=str()
s=str()
d=str()
f=str()
for i in  range(len(soz) ) :
    if soz[i].islower():
        a+=soz[i]
    elif  soz[i].isupper():
        s+=soz[i]
    elif  soz[i].isdigit():
        d+=soz[i]      
    else:
       f+=soz[i]  

print("lower: ", a)
print("upper: ", s)
print("number: ", d)
print("symbol: ", f)


soz=input("yozing: ")
   
soz=soz.title()
print(soz)










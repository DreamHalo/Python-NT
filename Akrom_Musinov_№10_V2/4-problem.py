


def intrect(sozlar=str()):
 for i in sozlar.split():     
    a=i
    b=i[0]
    i=i.replace(b, i[len(i)-1], 1)
    i=i[::-1].replace(i[len(i)-1], b, 1)[::-1]
    sozlar=sozlar.replace(a, i)
 print(sozlar)

intrect(input(">>> "))
matem = input(">>>  ")
plus=0; minus=0; kop=0; dot=0; prosent=0;  skobka=0; alf=0
for i in matem:
    if i =="+":
        plus+=1
    elif i=="-":
        minus+=1
    elif i=="*":
        kop+=1
    elif i=="/":
        dot+=1
    elif i=="%":
        prosent+=1
    elif i=="(" or i==")":
        skobka+=1
    else : alf+=1  

print("+ belgisi ",plus ,"ta" )
print("- belgisi ",minus ,"ta" )
print("* belgisi ",kop ,"ta" )        
print("/ belgisi ",dot ,"ta" )
print(" % belgisi ",prosent ,"ta" )
print("() belgisi ",skobka ,"ta")
 


def almashtirish(sozlar=str()):
 for i in sozlar.split():
    a=i
    b=i[0]
    i=i.replace(b, i[len(i)-1], 1)
    i=i[::-1].replace(i[len(i)-1], b, 1)[::-1]
    sozlar=sozlar.replace(a, i)
 print(sozlar)

almashtirish(input(">>> "))

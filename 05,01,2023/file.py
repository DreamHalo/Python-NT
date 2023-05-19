s=open("upper.txt","w+")
t=open("lower.txt","w+")
f=open("tajribe.txt","w+")

for i in range(int(input(">> "))):
    f.write(input(">>> ")+" ")
f.seek(0)
for i in f.read().split():
    if i==i.upper():
        s.write(i)
    else:
        t.write(i)


f.close()
t.close()
s.close()



z=open("tajriba.txt","w+")
q=open("juft.txt","w+")
a=open("toq.txt","w+")
r=open("null.txt","w+")

for i in range(int(input("nechta son: "))):
    z.write(input(">>> ")+" ")
z.seek(0)
for i in z.read().split():
    if int(i)%2==0:
        q.write(i)
    else:
        a.write(i) 


z.close()
a.close()
q.close() 


p=open("polindrom.txt","w+")   
soz=open("sozlar.txt","r")

for i in soz.read().split("\n"):
    for g in i.split():
        if g==g[::-1]:
            p.write(i+"\n")
            break



p.close()
soz.close()


j= open("cinema.txt", "r")
k = int(input("Soat nechada boshlansin"))
for i in j.readlines():
    for g in i.split(","):
        if g.startswith(str(k)+":"):
             print(i)

j.close()



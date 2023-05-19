def almashtirish(sozlar=str()):
 for i in sozlar.split():
    a=i
    b=i[0]
    i=i.replace(b, i[len(i)-1], 1)
    i=i[::-1].replace(i[len(i)-1], b, 1)[::-1]
    sozlar=sozlar.replace(a, i)
 print(sozlar)

almashtirish(input(">>> "))

 
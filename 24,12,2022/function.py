# 1  

def chet(s:str):
    dct={}
    for i in s:
       dct.update(dict([(i,s.count(i))]))
    return dct
print(chet("w3resource"))


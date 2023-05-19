# тапл=(1,2,3,4,5)
# привет=0
# for i in тапл:
#     привет+=i
# print(привет)

# тапл=(1,2,3,4,5)
# привет=0
# макс=0
# мин=0
# for i in тапл:
#     if макс<i:
#         макс=i
#     if мин >i:
#         мин=i
# куры=макс-мин
# print(куры)
 




# lst=[(1,3),(0,2,0),(1,1,1),(0,4),(1,9)]
# b=[]
# for i in lst:
    
#     b+=i
# print("  ",b)
# print(lst)



# амалийот


# lst=[[1,5,6],[9,4,5],[6,5,2]]
# lst.sort()
# print(lst)



# lst=[
#     ["Iphone",1200,"13Pro"],
#     ["Samsung",1000,"S10 Note"],
#     ["Honor",1100,"X"]
# ]
# lst.sort(key=lambda x: x[1])
# print(lst)


# lst=[[1,5,6],[9,4,5],[6,5,2]]
# for i in lst:
#     i.sort()

# print(lst)



# lst = [[1,5,6],[9,4,5],[6,5,2]]
# st={1}
# for i in lst:
#     for j in i:
#      st.add(j)\\\\

# print(st)




lst=[
    ["Iphone",1200,"13Pro"],
    ["Samsung",1000,"S10 Note"],
    ["Honor",1100,"X"]
]
sld = input(">>  ")
for i in lst:
    if sld==i[0]:
        lst.remove(i)
print(lst)


# phones=["Iphone","Samsung","ReadMi","LG"]
# asd=""
# while asd!=4: 
#     asd=int(input("1-korish:  \n 2-qoshish: \n 3-olib tashlash: \n 4-tugatish: \n >>>  "))
#     if asd==1:
#         print(phones)
#     if asd==2:
#         phones.append(input(">>> "))
#         print(phones)
#     if asd==3:
#         phones.remove(input(">>> "))
#         print(phones)

#     if asd==4:
#         print("Tugadi!") 
  
# user={
#     "ism" : input("Ismingizni kiriting : "),
#     "fam" : input("familiyangizni kiriting : "),
#     "tell": input("Telefon raqamingizni kiritiing : "),
#     "summa": input("Balansingizni kiriting : "),
#     "Stamatolog": {
#             "Valiev":{
#             1:["9:00 10:00","10:00 11:00","11:00 12:00","14:00 15:00","15:00 16:00"]
#             }
#             }
    
#     }
# toqqiz="" 
# on=""
# onbir=""
# ikki=""  
# uch=""  


# print(*user["Stamatolog"]["Valiev"][1])
# if input("Vaqti tanlang ")=="9:00":
#     print(user["ism"],"siz 9:00 dan 10:00 gacha band kildingiz ")
#     toqqiz=user["Stamatolog"]["Valiev"][1].pop(0)
# elif input("Vaqti tanlang ")=="10:00":
#     print(user["ism"],"siz 10:00 dan 11:00 gacha band kildingiz ")
#     on=user["Stamatolog"]["Valiev"][1].pop(0)
# elif input("Vaqti tanlang ")=="11:00":
#     print(user["ism"],"siz 11:00 dan 12:00 gacha band kildingiz ")
#     onbir=user["Stamatolog"]["Valiev"][1].pop(0)
# elif input("Vaqti tanlang ")=="14:00": 
#     print(user["ism"],"siz 14:00 dan 15:00 gacha band kildingiz ")
#     ikki=user["Stamatolog"]["Valiev"][1].pop(0)
# elif input("Vaqti tanlang ")=="15:00":
#     print(user["ism"],"siz 15:00 dan 16:00 gacha band kildingiz ")
#     uch=user["Stamatolog"]["Valiev"][1].pop(0)

# else :
#     print("bu xaqt band")

# print(user["Stamatolog"]["Valiev"][1])
    
    

print("SHifoxonaga xush kelibsiz!!!:")
ism=input("ismingizni kiriting:")
familiya=input("familiyangizni kiriting:")
tel=str(input("telefon raqamingizni kiriting:"))
summa=int(input("qancha pulingiz bor!!"))
print("tabriklaymiz siz ruyhatdan utdingiz!!!")

print("""
    <<<SHIFOXONA>>>
    1)Stomatolog
    2)Terapevt
    3)Xerurg
    4)Dermatolog
    5)Pulmanolog
""")
son=int(input(">>>"))
while True:
    for j in range(1):
        if son==1:
            print("a)Valiyev Sardor\n b)Asrorov Azam\n c)Ibodov Nodir")
            h1=input(">>>")
            
            print("1-band\n2-info")
            h2=int(input(">>>"))
            if h2==2 and h1=="a":
                print("""
                    "ismi":"Sardor",
                    "familiya":"Valiyev",
                    "yoshi":34,
                    "tajriba":"Oliy",
                    "tarif":100000
                """)
            elif h2==2 and h1=="b":
                print("""
                 "ismi":"Azam",
                 "familiya":"Asrorov",
                 "yoshi":30,
                 "tajriba":"Oliy",
                 "tarif":90000,
                 """)
            elif h2==2 and h1=="c":
                print("""
                "ismi":"Nodir",
                "familiya":"Ibatov",
                "yoshi":28,
                "tajriba":"Oliy",
                "tarif":95000
                """)

            

    dct={"9:00": '9:00  10:00',
    '10:00' : '10:00  11:00',
    '11:00' : '11:00 12:00',
    '14:00' : '14:00 15:00',
    '15:00' : '15:00 16:00',}
    print("Vaqtlarni kiriting:")
    print("""
        1) 9:00   10:00
        2) 10:00  11:00
        3) 11:00  12:00
        4) 14:00  15:00
        5) 15:00  16:00
    """)
    son=int(input(">>>"))
    popbulim=[]
    sonlar=0
    for i in range(1):

        if son==1:
            print(dct['9:00'])
            sonlar=dct.pop(dct["9:00"])
        elif son==2:
            print(dct['10:00'])
            sonlar=dct.pop(dct["10:00"])
        elif son==3:
           print(dct['11:00'])
           sonlar=dct.pop(dct["11:00"])
        elif son==4:
            print(dct['14:00'])
            sonlar=dct.pop(dct["14:00"])
        elif son==5:
            print(dct['15:00'])
            sonlar=dct.pop(dct["15:00"])
    break
print(sonlar)
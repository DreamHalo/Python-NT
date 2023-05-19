class Employee:
    def __init__(self, name, familiya, age, oylik, tajriba):
        self.ism = name
        self.familiya = familiya
        self.yosh = age
        self.maosh = oylik
        self.tajriba = tajriba
    
    def full_name(self):
        return f"{self.ism} {self.familiya}"
    
    def __str__(self):
        return f"""
Ism_sharif: {self.full_name()}
Yosh: {self.yosh}       
Tajriba: {self.tajriba}        
Maoshi: {self.maosh}
"""

class Developer(Employee):
    def __init__(self, ism, familiya,age, oylik, tajriba, prog_lang):
        super().__init__(ism, familiya, age, oylik, tajriba)
        self.prog_lang = prog_lang

    def __str__(self):
        return f"""
{super().__str__()}
Dasturlash tili: {self.prog_lang}"""

class Manager(Employee):
    def __init__(self, name, familiya, age, oylik, tajriba, royxat=None):
        super().__init__(name, familiya, age, oylik, tajriba)
    self.ishchilar_soni = 0
        if royxat == None:
            self.ishchilar_ruyxati = [] 
        else:
            self.ishchilar_ruyxati = royxat

    def add_employee(self, emp):
        if emp.full_name() not in self.ishchilar_ruyxati:
            self.ishchilar_ruyxati.append(emp.full_name())
            self.ishchilar_soni += 1 

    def delete_employee(self, emp):
        try:
            self.ishchilar_ruyxati.remove(emp.full_name())
            self.ishchilar_soni -= 1 
        except:
            print("Mavjud bo'lmagan inson!!!")

    def all_employees(self):
        for i in self.ishchilar_ruyxati:
            print(i)

    def __str__(self):
        return f"""   
{super().__str__()}
Ishchilar soni: {self.ishchilar_soni }        
        """

dev1 = Developer("Hoshim", "Haydarov", 18, 500, 1, 'Python')
dev2 = Developer("Eshmat", "Toshmatov", 25, 1000, 1, "GO")
dev3 = Developer("Ivan", "Vasiliy", 56, 10000, 30, "Swift")
dev4 = Developer("Akshey", "Kumat", 23, 800, 2, "JavaScript")

m1 = Manager("Ilhom", "Islomov", 19, 2000, 0)
print(m1)

m1.add_employee(dev2)
m1.add_employee(dev4)

m1.all_employees()
m1.delete_employee(dev4)

print(m1)


class Gamer:
    weapons=[
        [
    {
        'id': 1,
        "nomi": "ak-74",
        "patron": 100,
        "kuchi": 10,
        "narxi": 150
    },
    {
        'id': 2,
        "nomi": "mk",
        "patron": 100,
        "kuchi": 10,
        "narxi": 150
    },
    {
        'id': 3,
        "nomi": "pistolet",
        "patron": 60,
        "kuchi": 5,
        "narxi": 50
    },
    {
        'id': 4,
        "nomi": "sniper",
        "patron": 6,
        "kuchi": 10,
        "narxi": 350
    },
    {
        'id': 5,
        "nomi": "Plimot",
        "patron": 100,
        "kuchi": 20,
        "narxi": 250
    }
]
    ]
    def __init__(self,name,commands):
        pass

    def fire(self,who,possision):
        pass

    def heart(self):
        pass

    def weapon(self):
        pass

    def heal(self):
        pass


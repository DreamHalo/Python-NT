# import sys
# import os
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


# class Oyna(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.listname = []
#         self.latatron()

#     def latatron(self):
#         self.input1 = QLineEdit(self)
#         self.input1.setGeometry(10, 20, 400, 50)
#         self.setStyleSheet(
#             "background-color: wheat; border : 2px solid blue; border-radius: 1px;")
#         self.input1.setFont(QFont("PGothic", 15))
#         self.input1.setStyleSheet(
#             "background-color: white; border : 2px solid blue; border-radius: 1px;")

#         self.send = QPushButton(self)
#         self.send.setGeometry(450, 20, 100, 30)
#         self.send.setFont(QFont("PGothic", 7))

#         self.send.setText("+")
#         self.send.setStyleSheet(
#             "background-color: green; border : 2px silod blue; border-radius: 1px;")
#         self.send.clicked.connect(self.qosh)

#         self.clear = QPushButton(self)
#         self.clear.setGeometry(450, 60, 100, 30)
#         self.clear.setFont(QFont("PGothic", 7))
#         self.clear.setText("CLS")
#         self.clear.setStyleSheet(
#             "background-color: red; border : 2px silod blue; border-radius: 1px;")
#         self.clear.clicked.connect(self.cleared)


#         self.list = QListWidget(self)
#         self.list.setGeometry(10, 140, 200, 600)
#         self.list.setFont(QFont("MC PGothic", 15))
#         self.list.setStyleSheet(
#             "background-color: white; border: 3px solid green; border-radius: 12px;")
#         self.yozuv = QLabel("Kitob oqish", self)
#         self.yozuv.setGeometry(80, 100, 60, 15)
#         self.yozuv.setStyleSheet(
#             "background-color: wheat; border: 3px solid wheat;")
    
#         self.list2 = QListWidget(self)
#         self.list2.setGeometry(220, 140, 200, 600)
#         self.list2.setFont(QFont("MC PGothic", 15))
#         self.list2.setStyleSheet(
#             "background-color: white; border: 3px solid green; border-radius: 12px;")
#         self.yozuv2 = QLabel("Bajarish", self)
#         self.yozuv2.setGeometry(240, 100, 60, 15)
#         self.yozuv2.setStyleSheet(
#             "background-color: wheat; border: 3px solid wheat;")
#         self.list3 = QListWidget(self)
#         self.list3.setGeometry(430, 140, 200, 600)
#         self.list3.setFont(QFont("MC PGothic", 15))
#         self.list3.setStyleSheet(
#             "background-color: white; border: 3px solid green; border-radius: 12px;")
#         self.yozuv3 = QLabel("Tugatish", self)
#         self.yozuv3.setGeometry(450, 100, 60, 15)
#         self.yozuv3.setStyleSheet(
#             "background-color: wheat; border: 3px solid wheat;")
#         self.list.clicked.connect(self.push)

#     def qosh(self):
#         a = self.input1.text()
  
#         if a  and a+" "not in self.listname:
#             self.listname.append(a + " ")
#             self.input1.setText("")
        
#             self.render()

#     def render(self):
#         a = 1
#         self.list.clear()
#         for i in range(len(self.listname)-1, -1, -1):
#             self.list.insertItem(0, str(i+1)+")" + self.listname[i])
#             a += 1

#     def cleared(self):
#         if len(self.listname):
#             self.list.clear()
#             self.listname = []

#     def push(self):
#         print(self.list.currentItem().text())


# apk = QApplication(sys.argv)
# man = Oyna()
# man.setGeometry(250, 50, 640, 750)
# man.setWindowTitle("Main")
# man.setWindowIcon(QIcon("C:\\Users\\ASUS\\OneDrive\\Изображения\\IMG_1493"))

# man.show()
# sys.exit(apk.exec_())



# ############################




from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class Oyna(QMainWindow):

 def __init__(self):
         super().__init__()
         self.setWindowTitle("Калькулятор ")
         self.setGeometry(100, 100, 360, 350)
         self.method()
         self.show()
  
 
  
 def method(self):
         self.label = QLabel(self)
         self.label.setGeometry(5, 5, 350, 70)
         self.label.setWordWrap(True)
         self.label.setStyleSheet("QLabel"
                                  "{"
                                  "border : 4px solid black;"
                                  "background : white;"
                                  "}") 
         self.label.setFont(QFont('Arial', 15))
         push1 = QPushButton("1", self)
         push1.setGeometry(5, 150, 80, 40)
         push2 = QPushButton("2", self)
         push2.setGeometry(95, 150, 80, 40)
         push3 = QPushButton("3", self)
         push3.setGeometry(185, 150, 80, 40)
         push4 = QPushButton("4", self)
         push4.setGeometry(5, 200, 80, 40)
         push5 = QPushButton("5", self)
         push5.setGeometry(95, 200, 80, 40)
         push6 = QPushButton("5", self)
         push6.setGeometry(185, 200, 80, 40)
         push7 = QPushButton("7", self)
         push7.setGeometry(5, 250, 80, 40)
         push8 = QPushButton("8", self)
         push8.setGeometry(95, 250, 80, 40)
         push9 = QPushButton("9", self)
         push9.setGeometry(185, 250, 80, 40)
         push0 = QPushButton("0", self)
         push0.setGeometry(5, 300, 80, 40)
         push_barobar = QPushButton("=", self)
         push_barobar.setGeometry(275, 300, 80, 40)
         push_plus = QPushButton("+", self)
         push_plus.setGeometry(275, 250, 80, 40)
         push_minus = QPushButton("-", self)
         push_minus.setGeometry(275, 200, 80, 40)
         push_kopaytir = QPushButton("*", self)
         push_kopaytir.setGeometry(275, 150, 80, 40)
         push_boluv = QPushButton("/", self)
         push_boluv.setGeometry(185, 300, 80, 40)
         push_nuqta = QPushButton(".", self)
         push_nuqta.setGeometry(95, 300, 80, 40)
         push_clear = QPushButton("Clear", self)
         push_clear.setGeometry(5, 100, 200, 40)
         push_ochir = QPushButton("Del", self)
         push_ochir.setGeometry(210, 100, 145, 40)
         push_minus.clicked.connect(self.minus)
         push_barobar.clicked.connect(self.barobar)
         push0.clicked.connect(self.nul)
         push1.clicked.connect(self.bir)
         push2.clicked.connect(self.ikki)
         push3.clicked.connect(self.uch)
         push4.clicked.connect(self.tor)
         push5.clicked.connect(self.besh)
         push6.clicked.connect(self.olti)
         push7.clicked.connect(self.yetti)
         push8.clicked.connect(self.sakkis)
         push9.clicked.connect(self.toqqis)
         push_boluv.clicked.connect(self.boluv)
         push_kopaytir.clicked.connect(self.kopaytir)
         push_plus.clicked.connect(self.plus)
         push_nuqta.clicked.connect(self.nuqta)
         push_clear.clicked.connect(self.clear)
         push_ochir.clicked.connect(self.ochir)
  
def barobar(self):
         teng = self.label.text()
         try:
             ans = eval(teng)
             self.label.setText(str(ans))
         except:
             self.label.setText("Xato")
  
def plus(self):
         text = self.label.text()
         self.label.setText(text + " + ")

def minus(self):
         text = self.label.text() 
         self.label.setText(text + " - ")

def boluv(self):
         text = self.label.text()
         self.label.setText(text + " / ")

def kopaytir(self):
         text = self.label.text()
         self.label.setText(text + " * ") 
def nuqta(self):
         text = self.label.text()
         self.label.setText(text + ".")

def nul(self):
     text = self.label.text()
     self.label.setText(text + "0")

def bir(self):
     text = self.label.text()
     self.label.setText(text + "1")

def ikki(self):
     text = self.label.text()
     self.label.setText(text + "2")

def uch(self):
     text = self.label.text()
     self.label.setText(text + "3")

def tor(self):
     text = self.label.text()
     self.label.setText(text + "4")

def besh(self):
     text = self.label.text()
     self.label.setText(text + "5")

def olti(self):
     text = self.label.text()
     self.label.setText(text + "6")

def yetti(self):
     text = self.label.text()
     self.label.setText(text + "7")

def sakkis(self):
     text = self.label.text()
     self.label.setText(text + "8")

def toqqis(self):2
     text = self.label.text()
     self.label.setText(text + "9")

def clear(self):
     self.label.setText("")
 
def ochir(self):

         text = self.label.text()
         print(text[:len(text)-1])
         self.label.setText(text[:len(text)-1])

App = QAplication(sys.argv)
oyna = Oyna()
sys.exit(App.exec())









# def partition(array, low, high):
#   pivot = array[high]


#   i = low - 1

#   for j in range(low, high):
#     if array[j] <= pivot:
#       i = i + 1

#       (array[i], array[j]) = (array[j], array[i])

#   (array[i + 1], array[high]) = (array[high], array[i + 1])

#   return i + 1

# def quickSort(array, low, high):
#   if low < high:
#     pi = partition(array, low, high)

#     quickSort(array, low, pi - 1) 

#     quickSort(array, pi + 1, high)


# data = [8, 7, 2, 1, 0, 9, 6]
# print("Unsorted Array")
# print(data)

# size = len(data)

# quickSort(data, 0, size - 1)

# print('Sorted Array in Ascending Order:')
# print(data)



# arr = [4,1,5,8,2,9,6,3]                                             
# output =[]
# for i in range(len(arr)):
#     count = 0 
#     for j in range(len(arr)):
#         if arr[i]>arr[j]:
#             count+=1
#     output.append(count)       
# print(output)   Т
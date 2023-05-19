# from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QPushButton,QListWidget
# import sys
# from PyQt5.QtGui import QIcon,QFont

# app = QApplication(sys.argv)
# oyna=QWidget()

# oyna.setWindowTitle("birinchi oyna")     
# oyna.setWindowIcon(QIcon("C:\\Users\\ASUS\\OneDrive\\Изображения\\IMG_1493"))
# oyna.setGeometry(250,200,500,300)
# oyna.move(0,100)
# oyna.setFixedSize(500,450)

# yozuv1 = QLabel("Akrom",oyna)
# yozuv2 = QLabel("Musinov",oyna)
# yozuv3 = QLabel("18",oyna)
# yozuv1.move(1, 10)
# yozuv2.move(1, 30)
# yozuv3.move(1, 50)
# yozuv1.setFont(QFont("Times",10))
# yozuv2.setFont(QFont("Times",10)) 
# yozuv3.setFont(QFont("Times",10))

# kiritish1=QLineEdit(oyna)
# kiritish2=QLineEdit(oyna)
# kiritish3=QLineEdit(oyna)
# kiritish1.move(1, 10)
# kiritish2.move(1, 40)
# kiritish3.move(1, 70)

# button1 = QPushButton("OK",oyna)
# button1.setGeometry(300, 100, 50,50)

# oyna.show()
# app.exec_()










# app = QApplication([])
# oyna=QWidget()
# oyna.setGeometry(650,600,400,300)
# oyna.setWindowTitle("Main")     
# oyna.setWindowIcon(QIcon("C:\\Users\\ASUS\\OneDrive\\Изображения\\IMG_1493"))

# kiritish1=QLineEdit(oyna)
# kiritish2=QLineEdit(oyna)
# kiritish3=QLineEdit(oyna)
# kiritish1.move(10,10)
# kiritish1.setPlaceholderText("Notes..")
# kiritish2.move(10,30)
# kiritish2.setPlaceholderText("Name..")
# kiritish2.setGeometry(10,40,60,20)
# kiritish3.move(40,30)
# kiritish3.setPlaceholderText("Surname..")
# kiritish3.setGeometry(80,40,63,20)

# button1 = QPushButton("Print", oyna)
# button2 = QPushButton("Clear", oyna)
# button1.setGeometry(170,5,50,30)
# button2.setGeometry(170,40,50,30)

# lst=QListWidget(oyna)
# lst.setGeometry(10,80,210,200)

# def add():
#     print(kiritish1.text(),kiritish2.text(),kiritish2.text())
#     lst.insertItem(0,kiritish2.text()+(" ")+kiritish3.text()+("\n")+kiritish1.text())

# oyna.show()
# sys.exit(app.exec_())



















from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit,
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QMessageBox, QCheckBox, QComboBox, QRadioButton
from PyQt5.QtGui import QFont, QIcon
class Window(QWidget):
    def __init__(self,count=0):
        self.count=count
        
        super().__init__()
        self.setGeometry(200,200,300,300)
        self.start()
    
    def OwnFont(self, obj, x, y):
        obj.setFont(QFont("Times", 15))
        obj.move(x,y)
    def start(self):
        self.yozuv = QLabel("Which club is the best?", self)
        self.OwnFont(self.yozuv, 30, 50)

        self.v1 = QRadioButton("Paxtakor",self)
        self.OwnFont(self.v1, 50, 80)

        self.v2 = QRadioButton("Nasaf", self)
        self.OwnFont(self.v2, 50, 110)

        self.v3 = QRadioButton("Navbaxor", self)
        self.OwnFont(self.v3, 50, 140)

        self.v4 = QRadioButton("AGMK", self)
        self.OwnFont(self.v4, 50, 170)

        self.v5 = QRadioButton("Turon", self)
        self.OwnFont(self.v5, 50, 200)

        self.lst = [self.v1, self.v2, self.v3, self.v4, self.v5]

        self.btn = QPushButton("->",self)
        self.OwnFont(self.btn, 150, 240)
        self.btn.clicked.connect(self.natija)
      
        if self.v1.isChecked():
            self.count+=1
    
    def natija(self):
        for i in self.lst:
            i.hide()
        self.btn.hide()
        self.nexte()

    def nexte(self):
        self.yozuv.setText("Who is Jamshid?")
        self.OwnFont(self.yozuv, 30, 50)
        
        self.v11 = QRadioButton("Friend",self)
        self.OwnFont(self.v11, 50, 80)
        self.v22 = QRadioButton("Stupid person", self)
        self.OwnFont(self.v22, 50, 110)
        self.v33 = QRadioButton("dog", self)
        self.OwnFont(self.v33, 50, 140)
        self.v44 = QRadioButton("someone", self)
        self.OwnFont(self.v44, 50, 170)
        self.lst2 = [self.v11, self.v22, self.v33, self.v44]
        for j in self.lst2:
            j.show()
         

        self.btn2 = QPushButton("-->",self)
        self.OwnFont(self.btn, 150, 240)
        self.btn.clicked.connect(self.natija)
        if self.v4.isChecked(): 
          self.count+=1

    
if __name__=="__main__":
    app = QApplication([])
    oyna = Window()
    oyna.setWindowTitle("birinchi oyna")     
    oyna.setWindowIcon(QIcon("C:\\Users\\ASUS\\OneDrive\\Изображения\\IMG_1493"))
    oyna.show()
    app.exec_()
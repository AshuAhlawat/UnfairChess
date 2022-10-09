from PyQt5 import QtCore, QtGui, QtWidgets
from algo.possibilities import possibilities



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 890)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(850, 900))
        MainWindow.setStyleSheet("background-color:black;")
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.b00 = QtWidgets.QPushButton(self.centralwidget)
        self.b00.setGeometry(QtCore.QRect(0, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b00.setFont(font)
        self.b00.setStyleSheet("background-color:rgb(75,40,40)")
        self.b00.setObjectName("b00")
        self.b00.clicked.connect(self.actionb00)
        
        self.b01 = QtWidgets.QPushButton(self.centralwidget)
        self.b01.setGeometry(QtCore.QRect(100, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b01.setFont(font)
        self.b01.setStyleSheet("background-color:rgb(220,190,130)")
        self.b01.setObjectName("b01")
        self.b01.clicked.connect(self.actionb01)
        
        self.b02 = QtWidgets.QPushButton(self.centralwidget)
        self.b02.setGeometry(QtCore.QRect(200, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b02.setFont(font)
        self.b02.setStyleSheet("background-color:rgb(75,40,40)")
        self.b02.setObjectName("b02")
        self.b02.clicked.connect(self.actionb02)
        
        self.b03 = QtWidgets.QPushButton(self.centralwidget)
        self.b03.setGeometry(QtCore.QRect(300, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b03.setFont(font)
        self.b03.setStyleSheet("background-color:rgb(220,190,130)")
        self.b03.setObjectName("b03")
        self.b03.clicked.connect(self.actionb03)
        
        self.b04 = QtWidgets.QPushButton(self.centralwidget)
        self.b04.setGeometry(QtCore.QRect(400, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b04.setFont(font)
        self.b04.setStyleSheet("background-color:rgb(75,40,40)")
        self.b04.setObjectName("b04")
        self.b04.clicked.connect(self.actionb04)
        
        self.b05 = QtWidgets.QPushButton(self.centralwidget)
        self.b05.setGeometry(QtCore.QRect(500, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b05.setFont(font)
        self.b05.setStyleSheet("background-color:rgb(220,190,130)")
        self.b05.setObjectName("b05")
        self.b05.clicked.connect(self.actionb05)
        
        self.b06 = QtWidgets.QPushButton(self.centralwidget)
        self.b06.setGeometry(QtCore.QRect(600, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b06.setFont(font)
        self.b06.setStyleSheet("background-color:rgb(75,40,40)")
        self.b06.setObjectName("b06")
        self.b06.clicked.connect(self.actionb06)
        
        self.b07 = QtWidgets.QPushButton(self.centralwidget)
        self.b07.setGeometry(QtCore.QRect(700, 0, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b07.setFont(font)
        self.b07.setStyleSheet("background-color:rgb(220,190,130)")
        self.b07.setObjectName("b07")
        self.b07.clicked.connect(self.actionb07)
        
        self.b11 = QtWidgets.QPushButton(self.centralwidget)
        self.b11.setGeometry(QtCore.QRect(100, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b11.setFont(font)
        self.b11.setStyleSheet("background-color:rgb(75,40,40)")
        self.b11.setObjectName("b11")
        self.b11.clicked.connect(self.actionb11)
        
        self.b20 = QtWidgets.QPushButton(self.centralwidget)
        self.b20.setGeometry(QtCore.QRect(0, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b20.setFont(font)
        self.b20.setStyleSheet("background-color:rgb(75,40,40)")
        self.b20.setText("")
        self.b20.setObjectName("b20")
        self.b20.clicked.connect(self.actionb20)
        
        self.b22 = QtWidgets.QPushButton(self.centralwidget)
        self.b22.setGeometry(QtCore.QRect(200, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b22.setFont(font)
        self.b22.setStyleSheet("background-color:rgb(75,40,40)")
        self.b22.setText("")
        self.b22.setObjectName("b22")
        self.b22.clicked.connect(self.actionb22)
        
        self.b24 = QtWidgets.QPushButton(self.centralwidget)
        self.b24.setGeometry(QtCore.QRect(400, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b24.setFont(font)
        self.b24.setStyleSheet("background-color:rgb(75,40,40)")
        self.b24.setText("")
        self.b24.setObjectName("b24")
        self.b24.clicked.connect(self.actionb24)
        
        self.b26 = QtWidgets.QPushButton(self.centralwidget)
        self.b26.setGeometry(QtCore.QRect(600, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b26.setFont(font)
        self.b26.setStyleSheet("background-color:rgb(75,40,40)")
        self.b26.setText("")
        self.b26.setObjectName("b26")
        self.b26.clicked.connect(self.actionb26)
        
        self.b31 = QtWidgets.QPushButton(self.centralwidget)
        self.b31.setGeometry(QtCore.QRect(100, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b31.setFont(font)
        self.b31.setStyleSheet("background-color:rgb(75,40,40)")
        self.b31.setText("")
        self.b31.setObjectName("b31")
        self.b31.clicked.connect(self.actionb31)
        
        self.b33 = QtWidgets.QPushButton(self.centralwidget)
        self.b33.setGeometry(QtCore.QRect(300, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b33.setFont(font)
        self.b33.setStyleSheet("background-color:rgb(75,40,40)")
        self.b33.setText("")
        self.b33.setObjectName("b33")
        self.b33.clicked.connect(self.actionb33)
        
        self.b37 = QtWidgets.QPushButton(self.centralwidget)
        self.b37.setGeometry(QtCore.QRect(700, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b37.setFont(font)
        self.b37.setStyleSheet("background-color:rgb(75,40,40)")
        self.b37.setText("")
        self.b37.setObjectName("b37")
        self.b37.clicked.connect(self.actionb37)
        
        self.b35 = QtWidgets.QPushButton(self.centralwidget)
        self.b35.setGeometry(QtCore.QRect(500, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b35.setFont(font)
        self.b35.setStyleSheet("background-color:rgb(75,40,40)")
        self.b35.setText("")
        self.b35.setObjectName("b35")
        self.b35.clicked.connect(self.actionb35)
        
        self.b40 = QtWidgets.QPushButton(self.centralwidget)
        self.b40.setGeometry(QtCore.QRect(0, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b40.setFont(font)
        self.b40.setStyleSheet("background-color:rgb(75,40,40)")
        self.b40.setText("")
        self.b40.setObjectName("b40")
        self.b40.clicked.connect(self.actionb40)
        
        self.b42 = QtWidgets.QPushButton(self.centralwidget)
        self.b42.setGeometry(QtCore.QRect(200, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b42.setFont(font)
        self.b42.setStyleSheet("background-color:rgb(75,40,40)")
        self.b42.setText("")
        self.b42.setObjectName("b42")
        self.b42.clicked.connect(self.actionb42)
        
        self.b44 = QtWidgets.QPushButton(self.centralwidget)
        self.b44.setGeometry(QtCore.QRect(400, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b44.setFont(font)
        self.b44.setStyleSheet("background-color:rgb(75,40,40)")
        self.b44.setText("")
        self.b44.setObjectName("b44")
        self.b44.clicked.connect(self.actionb44)
        
        self.b46 = QtWidgets.QPushButton(self.centralwidget)
        self.b46.setGeometry(QtCore.QRect(600, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b46.setFont(font)
        self.b46.setStyleSheet("background-color:rgb(75,40,40)")
        self.b46.setText("")
        self.b46.setObjectName("b46")
        self.b46.clicked.connect(self.actionb46)
        
        self.b51 = QtWidgets.QPushButton(self.centralwidget)
        self.b51.setGeometry(QtCore.QRect(100, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b51.setFont(font)
        self.b51.setStyleSheet("background-color:rgb(75,40,40)")
        self.b51.setText("")
        self.b51.setObjectName("b51")
        self.b51.clicked.connect(self.actionb51)
        
        self.b53 = QtWidgets.QPushButton(self.centralwidget)
        self.b53.setGeometry(QtCore.QRect(300, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b53.setFont(font)
        self.b53.setStyleSheet("background-color:rgb(75,40,40)")
        self.b53.setText("")
        self.b53.setObjectName("b53")
        self.b53.clicked.connect(self.actionb53)
        
        self.b55 = QtWidgets.QPushButton(self.centralwidget)
        self.b55.setGeometry(QtCore.QRect(500, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b55.setFont(font)
        self.b55.setStyleSheet("background-color:rgb(75,40,40)")
        self.b55.setText("")
        self.b55.setObjectName("b55")
        self.b55.clicked.connect(self.actionb55)
        
        self.b57 = QtWidgets.QPushButton(self.centralwidget)
        self.b57.setGeometry(QtCore.QRect(700, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b57.setFont(font)
        self.b57.setStyleSheet("background-color:rgb(75,40,40)")
        self.b57.setText("")
        self.b57.setObjectName("b57")
        self.b57.clicked.connect(self.actionb57)
        
        self.b60 = QtWidgets.QPushButton(self.centralwidget)
        self.b60.setGeometry(QtCore.QRect(0, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b60.setFont(font)
        self.b60.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b60.setObjectName("b60")
        self.b60.clicked.connect(self.actionb60)
        
        self.b62 = QtWidgets.QPushButton(self.centralwidget)
        self.b62.setGeometry(QtCore.QRect(200, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b62.setFont(font)
        self.b62.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b62.setObjectName("b62")
        self.b62.clicked.connect(self.actionb62)
        
        self.b64 = QtWidgets.QPushButton(self.centralwidget)
        self.b64.setGeometry(QtCore.QRect(400, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b64.setFont(font)
        self.b64.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b64.setObjectName("b64")
        self.b64.clicked.connect(self.actionb64)
        
        self.b66 = QtWidgets.QPushButton(self.centralwidget)
        self.b66.setGeometry(QtCore.QRect(600, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b66.setFont(font)
        self.b66.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b66.setObjectName("b66")
        self.b66.clicked.connect(self.actionb66)
        
        self.b71 = QtWidgets.QPushButton(self.centralwidget)
        self.b71.setGeometry(QtCore.QRect(100, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b71.setFont(font)
        self.b71.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b71.setObjectName("b71")
        self.b71.clicked.connect(self.actionb71)
        
        self.b73 = QtWidgets.QPushButton(self.centralwidget)
        self.b73.setGeometry(QtCore.QRect(300, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b73.setFont(font)
        self.b73.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b73.setObjectName("b73")
        self.b73.clicked.connect(self.actionb73)
        
        self.b75 = QtWidgets.QPushButton(self.centralwidget)
        self.b75.setGeometry(QtCore.QRect(500, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b75.setFont(font)
        self.b75.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b75.setObjectName("b75")
        self.b75.clicked.connect(self.actionb75)
        
        self.b77 = QtWidgets.QPushButton(self.centralwidget)
        self.b77.setGeometry(QtCore.QRect(700, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b77.setFont(font)
        self.b77.setStyleSheet("background-color:rgb(75,40,40);color:white")
        self.b77.setObjectName("b77")
        self.b77.clicked.connect(self.actionb77)
        
        self.b10 = QtWidgets.QPushButton(self.centralwidget)
        self.b10.setGeometry(QtCore.QRect(0, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b10.setFont(font)
        self.b10.setStyleSheet("background-color:rgb(220,190,130)")
        self.b10.setObjectName("b10")
        self.b10.clicked.connect(self.actionb10)
        
        self.b21 = QtWidgets.QPushButton(self.centralwidget)
        self.b21.setGeometry(QtCore.QRect(100, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b21.setFont(font)
        self.b21.setStyleSheet("background-color:rgb(220,190,130)")
        self.b21.setText("")
        self.b21.setObjectName("b21")
        self.b21.clicked.connect(self.actionb21)
        
        self.b23 = QtWidgets.QPushButton(self.centralwidget)
        self.b23.setGeometry(QtCore.QRect(300, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b23.setFont(font)
        self.b23.setStyleSheet("background-color:rgb(220,190,130)")
        self.b23.setText("")
        self.b23.setObjectName("b23")
        self.b23.clicked.connect(self.actionb23)
        
        self.b25 = QtWidgets.QPushButton(self.centralwidget)
        self.b25.setGeometry(QtCore.QRect(500, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b25.setFont(font)
        self.b25.setStyleSheet("background-color:rgb(220,190,130)")
        self.b25.setText("")
        self.b25.setObjectName("b25")
        self.b25.clicked.connect(self.actionb25)
        
        self.b27 = QtWidgets.QPushButton(self.centralwidget)
        self.b27.setGeometry(QtCore.QRect(700, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b27.setFont(font)
        self.b27.setStyleSheet("background-color:rgb(220,190,130)")
        self.b27.setText("")
        self.b27.setObjectName("b27")
        self.b27.clicked.connect(self.actionb27)
        
        self.b30 = QtWidgets.QPushButton(self.centralwidget)
        self.b30.setGeometry(QtCore.QRect(0, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b30.setFont(font)
        self.b30.setStyleSheet("background-color:rgb(220,190,130)")
        self.b30.setText("")
        self.b30.setObjectName("b30")
        self.b30.clicked.connect(self.actionb30)
        
        self.b32 = QtWidgets.QPushButton(self.centralwidget)
        self.b32.setGeometry(QtCore.QRect(200, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b32.setFont(font)
        self.b32.setStyleSheet("background-color:rgb(220,190,130)")
        self.b32.setText("")
        self.b32.setObjectName("b32")
        self.b32.clicked.connect(self.actionb32)
        
        self.b34 = QtWidgets.QPushButton(self.centralwidget)
        self.b34.setGeometry(QtCore.QRect(400, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b34.setFont(font)
        self.b34.setStyleSheet("background-color:rgb(220,190,130)")
        self.b34.setText("")
        self.b34.setObjectName("b34")
        self.b34.clicked.connect(self.actionb34)
        
        
        self.b36 = QtWidgets.QPushButton(self.centralwidget)
        self.b36.setGeometry(QtCore.QRect(600, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b36.setFont(font)
        self.b36.setStyleSheet("background-color:rgb(220,190,130)")
        self.b36.setText("")
        self.b36.setObjectName("b36")
        self.b36.clicked.connect(self.actionb36)
        
        self.b41 = QtWidgets.QPushButton(self.centralwidget)
        self.b41.setGeometry(QtCore.QRect(100, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b41.setFont(font)
        self.b41.setStyleSheet("background-color:rgb(220,190,130)")
        self.b41.setText("")
        self.b41.setObjectName("b41")
        self.b41.clicked.connect(self.actionb41)
        
        self.b43 = QtWidgets.QPushButton(self.centralwidget)
        self.b43.setGeometry(QtCore.QRect(300, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b43.setFont(font)
        self.b43.setStyleSheet("background-color:rgb(220,190,130)")
        self.b43.setText("")
        self.b43.setObjectName("b43")
        self.b43.clicked.connect(self.actionb43)
        
        self.b45 = QtWidgets.QPushButton(self.centralwidget)
        self.b45.setGeometry(QtCore.QRect(500, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b45.setFont(font)
        self.b45.setStyleSheet("background-color:rgb(220,190,130)")
        self.b45.setText("")
        self.b45.setObjectName("b45")
        self.b45.clicked.connect(self.actionb45)
        
        self.b47 = QtWidgets.QPushButton(self.centralwidget)
        self.b47.setGeometry(QtCore.QRect(700, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b47.setFont(font)
        self.b47.setStyleSheet("background-color:rgb(220,190,130)")
        self.b47.setText("")
        self.b47.setObjectName("b47")
        self.b47.clicked.connect(self.actionb47)
        
        self.b50 = QtWidgets.QPushButton(self.centralwidget)
        self.b50.setGeometry(QtCore.QRect(0, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b50.setFont(font)
        self.b50.setStyleSheet("background-color:rgb(220,190,130)")
        self.b50.setText("")
        self.b50.setObjectName("b50")
        self.b50.clicked.connect(self.actionb50)
        
        self.b52 = QtWidgets.QPushButton(self.centralwidget)
        self.b52.setGeometry(QtCore.QRect(200, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b52.setFont(font)
        self.b52.setStyleSheet("background-color:rgb(220,190,130)")
        self.b52.setText("")
        self.b52.setObjectName("b52")
        self.b52.clicked.connect(self.actionb52)
        
        self.b54 = QtWidgets.QPushButton(self.centralwidget)
        self.b54.setGeometry(QtCore.QRect(400, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b54.setFont(font)
        self.b54.setStyleSheet("background-color:rgb(220,190,130)")
        self.b54.setText("")
        self.b54.setObjectName("b54")
        self.b54.clicked.connect(self.actionb54)
        
        self.b56 = QtWidgets.QPushButton(self.centralwidget)
        self.b56.setGeometry(QtCore.QRect(600, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b56.setFont(font)
        self.b56.setStyleSheet("background-color:rgb(220,190,130)")
        self.b56.setText("")
        self.b56.setObjectName("b56")
        self.b56.clicked.connect(self.actionb56)
        
        self.b61 = QtWidgets.QPushButton(self.centralwidget)
        self.b61.setGeometry(QtCore.QRect(100, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b61.setFont(font)
        self.b61.setStyleSheet("background-color:rgb(220,190,130);color:white;")
        self.b61.setObjectName("b61")
        self.b61.clicked.connect(self.actionb61)
        
        self.b63 = QtWidgets.QPushButton(self.centralwidget)
        self.b63.setGeometry(QtCore.QRect(300, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b63.setFont(font)
        self.b63.setStyleSheet("background-color:rgb(220,190,130);color:white")
        self.b63.setObjectName("b63")
        self.b63.clicked.connect(self.actionb63)
        
        self.b65 = QtWidgets.QPushButton(self.centralwidget)
        self.b65.setGeometry(QtCore.QRect(500, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b65.setFont(font)
        self.b65.setStyleSheet("background-color:rgb(220,190,130);color:white")
        self.b65.setObjectName("b65")
        self.b65.clicked.connect(self.actionb65)
        
        self.b76 = QtWidgets.QPushButton(self.centralwidget)
        self.b76.setGeometry(QtCore.QRect(600, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b76.setFont(font)
        self.b76.setStyleSheet("background-color:rgb(220,190,130);color:white")
        self.b76.setObjectName("b76")
        self.b76.clicked.connect(self.actionb76)
        
        self.b70 = QtWidgets.QPushButton(self.centralwidget)
        self.b70.setGeometry(QtCore.QRect(0, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b70.setFont(font)
        self.b70.setStyleSheet("background-color:rgb(220,190,130);color:white")
        self.b70.setObjectName("b70")
        self.b70.clicked.connect(self.actionb70)
        
        self.b72 = QtWidgets.QPushButton(self.centralwidget)
        self.b72.setGeometry(QtCore.QRect(200, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b72.setFont(font)
        self.b72.setStyleSheet("background-color:rgb(220,190,130);color:white")
        self.b72.setObjectName("b72")
        self.b72.clicked.connect(self.actionb72)
        
        self.b74 = QtWidgets.QPushButton(self.centralwidget)
        self.b74.setGeometry(QtCore.QRect(400, 700, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b74.setFont(font)
        self.b74.setStyleSheet("background-color:rgb(220,190,130);color:white")
        self.b74.setObjectName("b74")
        self.b74.clicked.connect(self.actionb74)
        
        self.b67 = QtWidgets.QPushButton(self.centralwidget)
        self.b67.setGeometry(QtCore.QRect(700, 600, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b67.setFont(font)
        self.b67.setStyleSheet("background-color:rgb(220,190,130);color:white")
        self.b67.setObjectName("b67")
        self.b67.clicked.connect(self.actionb67)
        
        
        self.turnviewer = QtWidgets.QLabel(self.centralwidget)
        self.turnviewer.setGeometry(QtCore.QRect(0, 840, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.turnviewer.setFont(font)
        self.turnviewer.setStyleSheet("color:white;")
        self.turnviewer.setAlignment(QtCore.Qt.AlignCenter)
        self.turnviewer.setObjectName("turnviewer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(800, 0, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 100, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 200, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(800, 310, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 410, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(800, 500, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(800, 600, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(800, 700, 41, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(100, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:white")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(300, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:white")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:white")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(500, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:white")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(600, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:white")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(700, 800, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:white")
        self.label_16.setObjectName("label_16")
        
        self.b12 = QtWidgets.QPushButton(self.centralwidget)
        self.b12.setGeometry(QtCore.QRect(200, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b12.setFont(font)
        self.b12.setStyleSheet("background-color:rgb(220,190,130)")
        self.b12.setObjectName("b12")
        self.b12.clicked.connect(self.actionb12)
        
        self.b14 = QtWidgets.QPushButton(self.centralwidget)
        self.b14.setGeometry(QtCore.QRect(400, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b14.setFont(font)
        self.b14.setStyleSheet("background-color:rgb(220,190,130)")
        self.b14.setObjectName("b14")
        self.b14.clicked.connect(self.actionb14)
        
        self.b16 = QtWidgets.QPushButton(self.centralwidget)
        self.b16.setGeometry(QtCore.QRect(600, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b16.setFont(font)
        self.b16.setStyleSheet("background-color:rgb(220,190,130)")
        self.b16.setObjectName("b16")
        self.b16.clicked.connect(self.actionb16)
        
        self.b13 = QtWidgets.QPushButton(self.centralwidget)
        self.b13.setGeometry(QtCore.QRect(300, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b13.setFont(font)
        self.b13.setStyleSheet("background-color:rgb(75,40,40)")
        self.b13.setObjectName("b13")
        self.b13.clicked.connect(self.actionb13)
        
        self.b15 = QtWidgets.QPushButton(self.centralwidget)
        self.b15.setGeometry(QtCore.QRect(500, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b15.setFont(font)
        self.b15.setStyleSheet("background-color:rgb(75,40,40)")
        self.b15.setObjectName("b15")
        self.b15.clicked.connect(self.actionb15)
        
        self.b17 = QtWidgets.QPushButton(self.centralwidget)
        self.b17.setGeometry(QtCore.QRect(700, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b17.setFont(font)
        self.b17.setStyleSheet("background-color:rgb(75,40,40)")
        self.b17.setObjectName("b17")
        self.b17.clicked.connect(self.actionb17)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Unfair CHESS"))
        self.b00.setText(_translate("MainWindow", "bR"))
        self.b01.setText(_translate("MainWindow", "bKn"))
        self.b02.setText(_translate("MainWindow", "bB"))
        self.b03.setText(_translate("MainWindow", "bK"))
        self.b04.setText(_translate("MainWindow", "bQ"))
        self.b05.setText(_translate("MainWindow", "bB"))
        self.b06.setText(_translate("MainWindow", "bKn"))
        self.b07.setText(_translate("MainWindow", "bR"))
        self.b11.setText(_translate("MainWindow", "bP"))
        self.b60.setText(_translate("MainWindow", "wP"))
        self.b62.setText(_translate("MainWindow", "wP"))
        self.b64.setText(_translate("MainWindow", "wP"))
        self.b66.setText(_translate("MainWindow", "wP"))
        self.b71.setText(_translate("MainWindow", "wKn"))
        self.b73.setText(_translate("MainWindow", "wK"))
        self.b75.setText(_translate("MainWindow", "wB"))
        self.b77.setText(_translate("MainWindow", "wR"))
        self.b10.setText(_translate("MainWindow", "bP"))
        self.b61.setText(_translate("MainWindow", "wP"))
        self.b63.setText(_translate("MainWindow", "wP"))
        self.b65.setText(_translate("MainWindow", "wP"))
        self.b76.setText(_translate("MainWindow", "wKn"))
        self.b70.setText(_translate("MainWindow", "wR"))
        self.b72.setText(_translate("MainWindow", "wB"))
        self.b74.setText(_translate("MainWindow", "wQ"))
        self.b67.setText(_translate("MainWindow", "wP"))
        self.turnviewer.setText(_translate("MainWindow", "Turn Now: Black"))
        self.label.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "8"))
        self.label_9.setText(_translate("MainWindow", "A"))
        self.label_10.setText(_translate("MainWindow", "B"))
        self.label_11.setText(_translate("MainWindow", "C"))
        self.label_12.setText(_translate("MainWindow", "D"))
        self.label_13.setText(_translate("MainWindow", "E"))
        self.label_14.setText(_translate("MainWindow", "F"))
        self.label_15.setText(_translate("MainWindow", "G"))
        self.label_16.setText(_translate("MainWindow", "H"))
        self.b12.setText(_translate("MainWindow", "bP"))
        self.b14.setText(_translate("MainWindow", "bP"))
        self.b16.setText(_translate("MainWindow", "bP"))
        self.b13.setText(_translate("MainWindow", "bP"))
        self.b15.setText(_translate("MainWindow", "bP"))
        self.b17.setText(_translate("MainWindow", "bP"))
    

    def actionb00(self):
        self.clrsrc()
        if "x" in self.b00.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()
            
            self.active_pos = (0,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] == 1:
                        self.pos_color(i, j)
    
    def actionb01(self):
        self.clrsrc()
        if "x" in self.b01.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()
            
            self.active_pos = (1,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb02(self):
        self.clrsrc()
        
        if "x" in self.b02.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()
            
            self.active_pos = (2,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb03(self):
        self.clrsrc()
        
        if "x" in self.b03.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()
            
            self.active_pos = (3,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb04(self):
        self.clrsrc()
        
        if "x" in self.b04.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][4] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
        
    def actionb05(self):
        self.clrsrc()
   
        if "x" in self.b05.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][5] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j) 
        
    def actionb06(self):
        self.clrsrc()
    
        if "x" in self.b06.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][6] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (6,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j) 
    
    def actionb07(self):
        self.clrsrc()
        
        if "x" in self.b07.text():
            self.clrx()
            pos = self.position_array()
            
            pos[0][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (7,0)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb10(self):
        self.clrsrc()
        
        if "x" in self.b10.text():
            self.clrx()
            pos = self.position_array()
            
            pos[1][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (0,1)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                
    def actionb11(self):
        self.clrsrc()
        
        if "x" in self.b11.text():
            self.clrx()
            pos = self.position_array()
            
            pos[1][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (1,1)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb12(self):
        self.clrsrc()
        
        if "x" in self.b12.text():
            self.clrx()
            pos = self.position_array()
            
            pos[1][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (2,1)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb13(self):
        self.clrsrc()
        
        if "x" in self.b13.text():
            self.clrx()
            pos = self.position_array()
            
            pos[1][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (3,1)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb14(self):
        self.clrsrc()
        
        if "x" in self.b14.text():
            self.clrx()
            pos = self.position_array()
            
            pos[1][4]=pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,1)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb15(self):
        self.clrsrc()
        
        if "x" in self.b15.text():
            self.clrx()
            pos = self.position_array()
            
            pos[1][5]=pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,1)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb16(self):
        self.clrsrc()
        
        if "x" in self.b16.text():
            self.clrx()
            
            pos = self.position_array()
            
            pos[1][6]= pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
         self.clrx()
         pos = self.position_array()
         
        self.active_pos = (6,1)
        p = possibilities(pos,self.active_pos)
        for i in range(8):
            for j in range(8):
                if p[i][j] ==1:
                    self.pos_color(i,j)
    
    def actionb17(self):
        self.clrsrc()
        
        if "x" in self.b17.text():
            self.clrx()
            pos = self.position_array()
            
            pos[1][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (7,1)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb20(self):
        self.clrsrc()
        
        if "x" in self.b20.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (0,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb21(self):
        self.clrsrc()
        
        if "x" in self.b21.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (1,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    def actionb22(self):
        self.clrsrc()
        
        if "x" in self.b22.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (2,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    def actionb23(self):
        self.clrsrc()
        
        if "x" in self.b23.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (3,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb24(self):
        self.clrsrc()
        
        if "x" in self.b24.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][4] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb25(self):
        self.clrsrc()
        
        if "x" in self.b25.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][5] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb26(self):
        self.clrsrc()
        
        if "x" in self.b26.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][6] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (6,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
        
    def actionb27(self):
        self.clrsrc()
        
        if "x" in self.b27.text():
            self.clrx()
            pos = self.position_array()
            
            pos[2][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (7,2)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)  
                    
    def actionb30(self):
        self.clrsrc()
        
        if "x" in self.b30.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (0,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb31(self):
        self.clrsrc()
        
        if "x" in self.b31.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (1,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb32(self):
        self.clrsrc()
        
        if "x" in self.b32.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (2,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb33(self):
        self.clrsrc()
        
        if "x" in self.b33.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            
            self.active_pos = (3,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb34(self):
        self.clrsrc()
        
        if "x" in self.b34.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][4] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb35(self):
        self.clrsrc()
        
        if "x" in self.b35.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][5] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb36(self):
        self.clrsrc()
        
        if "x" in self.b36.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][6] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (6,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb37(self):
        self.clrsrc()
        
        if "x" in self.b37.text():
            self.clrx()
            pos = self.position_array()
            
            pos[3][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (7,3)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb40(self):
        self.clrsrc()
        
        if "x" in self.b40.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (0,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb41(self):
        self.clrsrc()
        
        if "x" in self.b41.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (1,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb42(self):
        self.clrsrc()
        
        if "x" in self.b42.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (2,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb43(self):
        self.clrsrc()
        
        if "x" in self.b43.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (3,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb44(self):
        self.clrsrc()
        
        if "x" in self.b44.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][4] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb45(self):
        self.clrsrc()
        
        if "x" in self.b45.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][5] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb46(self):
        self.clrsrc()
        
        if "x" in self.b46.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][6] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (6,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb47(self):
        self.clrsrc()
        
        if "x" in self.b47.text():
            self.clrx()
            pos = self.position_array()
            
            pos[4][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (7,4)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)  
                    
    def actionb50(self):
        self.clrsrc()
        
        if "x" in self.b50.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (0,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j) 
                    
    def actionb51(self):
        self.clrsrc()
        
        if "x" in self.b51.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (1,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb52(self):
        self.clrsrc()
        
        if "x" in self.b52.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (2,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb53(self):
        self.clrsrc()
        
        if "x" in self.b53.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (3,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                        
    def actionb54(self):
        self.clrsrc()
        
        if "x" in self.b54.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][4] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb55(self):
        self.clrsrc()
        
        if "x" in self.b55.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][5] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb56(self):
        self.clrsrc()
        
        if "x" in self.b56.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][6] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (6,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)   
                    
    def actionb57(self):
        self.clrsrc()
        pos = self.position_array()
        if "x" in self.b57.text():
            self.clrx()
            pos = self.position_array()
            
            pos[5][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            self.active_pos = (7,5)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)        
    
    def actionb60(self):
        self.clrsrc()
        
        if "x" in self.b60.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (0,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb61(self):
        self.clrsrc()
        
        if "x" in self.b61.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (1,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
        
    def actionb62(self):
        self.clrsrc()
        
        if "x" in self.b62.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (2,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb63(self):
        self.clrsrc()
        
        if "x" in self.b63.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (3,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb64(self):
        self.clrsrc()
        
        if "x" in self.b64.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][4] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                    
    def actionb65(self):
        self.clrsrc()
        
        if "x" in self.b65.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][5] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
        
    def actionb66(self):
        self.clrsrc()
        
        if "x" in self.b66.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][6] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (6,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb67(self):
        self.clrsrc()
        
        if "x" in self.b67.text():
            self.clrx()
            pos = self.position_array()
            
            pos[6][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (7,6)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb70(self):
        self.clrsrc()
        
        if "x" in self.b70.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][0] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (0,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb71(self):
        self.clrsrc()
        
        if "x" in self.b71.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][1] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (1,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb72(self):
        self.clrsrc()
        
        if "x" in self.b72.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][2] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (2,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb73(self):
        self.clrsrc()
        
        if "x" in self.b73.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][3] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (3,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb74(self):
        self.clrsrc()
        
        if "x" in self.b74.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][4] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (4,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    
    def actionb75(self):
        self.clrsrc()
        
        if "x" in self.b75.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][5] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (5,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
    def actionb76(self):
        self.clrsrc()
        
        if "x" in self.b76.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][6] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (6,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)
                        
    def actionb77(self):
        self.clrsrc()
        
        if "x" in self.b77.text():
            self.clrx()
            pos = self.position_array()
            
            pos[7][7] = pos[self.active_pos[1]][self.active_pos[0]]
            pos[self.active_pos[1]][self.active_pos[0]] = ""
            self.update_array(pos)
        else:
            self.clrx()
            pos = self.position_array()

            self.active_pos = (7,7)
            p = possibilities(pos,self.active_pos)
            for i in range(8):
                for j in range(8):
                    if p[i][j] ==1:
                        self.pos_color(i,j)             
                
    def position_array(self):
        self.position_arr = [
            [self.b00.text(),self.b01.text(),self.b02.text(),self.b03.text(),self.b04.text(),self.b05.text(),self.b06.text(),self.b07.text()],
            [self.b10.text(),self.b11.text(),self.b12.text(),self.b13.text(),self.b14.text(),self.b15.text(),self.b16.text(),self.b17.text()],
            [self.b20.text(),self.b21.text(),self.b22.text(),self.b23.text(),self.b24.text(),self.b25.text(),self.b26.text(),self.b27.text()],
            [self.b30.text(),self.b31.text(),self.b32.text(),self.b33.text(),self.b34.text(),self.b35.text(),self.b36.text(),self.b37.text()],
            [self.b40.text(),self.b41.text(),self.b42.text(),self.b43.text(),self.b44.text(),self.b45.text(),self.b46.text(),self.b47.text()],
            [self.b50.text(),self.b51.text(),self.b52.text(),self.b53.text(),self.b54.text(),self.b55.text(),self.b56.text(),self.b57.text()],
            [self.b60.text(),self.b61.text(),self.b62.text(),self.b63.text(),self.b64.text(),self.b65.text(),self.b66.text(),self.b67.text()],
            [self.b70.text(),self.b71.text(),self.b72.text(),self.b73.text(),self.b74.text(),self.b75.text(),self.b76.text(),self.b77.text()]
        ]   
        return self.position_arr
            
     
    def pos_color(self,i,j):
        update_color=[
            [self.b00,self.b01,self.b02,self.b03,self.b04,self.b05,self.b06,self.b07],
            [self.b10,self.b11,self.b12,self.b13,self.b14,self.b15,self.b16,self.b17],
            [self.b20,self.b21,self.b22,self.b23,self.b24,self.b25,self.b26,self.b27],
            [self.b30,self.b31,self.b32,self.b33,self.b34,self.b35,self.b36,self.b37],
            [self.b40,self.b41,self.b42,self.b43,self.b44,self.b45,self.b46,self.b47],
            [self.b50,self.b51,self.b52,self.b53,self.b54,self.b55,self.b56,self.b57],
            [self.b60,self.b61,self.b62,self.b63,self.b64,self.b65,self.b66,self.b67],
            [self.b70,self.b71,self.b72,self.b73,self.b74,self.b75,self.b76,self.b77]
         ]
        if update_color[i][j].setStyleSheet("background-color:rgb(75,40,40);"):
            if "w" in update_color[i][j].text():
                color = "white"
            else:
                color = "black"
            update_color[i][j].setStyleSheet("background-color:green;color:"+color+";")
            update_color[i][j].setText(update_color[i][j].text()+"x")
        else:
            if "w" in update_color[i][j].text():
                color = "white"
            else:
                color = "black"
            update_color[i][j].setStyleSheet("background-color:green;color:"+color+";")
            update_color[i][j].setText(update_color[i][j].text()+"x")
            
    def clrsrc(self):
        update_color=[
            [self.b00,self.b01,self.b02,self.b03,self.b04,self.b05,self.b06,self.b07],
            [self.b10,self.b11,self.b12,self.b13,self.b14,self.b15,self.b16,self.b17],
            [self.b20,self.b21,self.b22,self.b23,self.b24,self.b25,self.b26,self.b27],
            [self.b30,self.b31,self.b32,self.b33,self.b34,self.b35,self.b36,self.b37],
            [self.b40,self.b41,self.b42,self.b43,self.b44,self.b45,self.b46,self.b47],
            [self.b50,self.b51,self.b52,self.b53,self.b54,self.b55,self.b56,self.b57],
            [self.b60,self.b61,self.b62,self.b63,self.b64,self.b65,self.b66,self.b67],
            [self.b70,self.b71,self.b72,self.b73,self.b74,self.b75,self.b76,self.b77]
         ]
        for i in range(8):
            if i%2 ==0:
                for j in range(8):
                    if j%2 == 0:
                        color = "rgb(75,40,40)"
                    else:
                        color = "rgb(220,190,130)"
                    if "w" in update_color[i][j].text():
                        update_color[i][j].setStyleSheet("background-color:"+color+";color:white")
                    else:
                        update_color[i][j].setStyleSheet("background-color:"+color+";color:black")
                    
            else:
                for j in range(8):
                    if j%2 == 1:
                        color = "rgb(75,40,40)"
                    else:
                        color = "rgb(220,190,130)"
                    if "w" in update_color[i][j].text():
                        update_color[i][j].setStyleSheet("background-color:"+color+";color:white")
                    else:
                        update_color[i][j].setStyleSheet("background-color:"+color+";color:black")
                        
    def clrx(self):
        update_color=[
            [self.b00,self.b01,self.b02,self.b03,self.b04,self.b05,self.b06,self.b07],
            [self.b10,self.b11,self.b12,self.b13,self.b14,self.b15,self.b16,self.b17],
            [self.b20,self.b21,self.b22,self.b23,self.b24,self.b25,self.b26,self.b27],
            [self.b30,self.b31,self.b32,self.b33,self.b34,self.b35,self.b36,self.b37],
            [self.b40,self.b41,self.b42,self.b43,self.b44,self.b45,self.b46,self.b47],
            [self.b50,self.b51,self.b52,self.b53,self.b54,self.b55,self.b56,self.b57],
            [self.b60,self.b61,self.b62,self.b63,self.b64,self.b65,self.b66,self.b67],
            [self.b70,self.b71,self.b72,self.b73,self.b74,self.b75,self.b76,self.b77]
        ]
        for i in range(8):
            for j in range(8):
                if "x" in update_color[i][j].text():
                    update_color[i][j].setText(update_color[i][j].text().replace("x",""))
                
    def update_array(self,position_arr):
        self.position_arr = [
            [self.b00.setText(position_arr[0][0]),self.b01.setText(position_arr[0][1]),self.b02.setText(position_arr[0][2]),self.b03.setText(position_arr[0][3]),self.b04.setText(position_arr[0][4]),self.b05.setText(position_arr[0][5]),self.b06.setText(position_arr[0][6]),self.b07.setText(position_arr[0][7])],

            [self.b10.setText(position_arr[1][0]),self.b11.setText(position_arr[1][1]),self.b12.setText(position_arr[1][2]),self.b13.setText(position_arr[1][3]),self.b14.setText(position_arr[1][4]),self.b15.setText(position_arr[1][5]),self.b16.setText(position_arr[1][6]),self.b17.setText(position_arr[1][7])],
            
            [self.b20.setText(position_arr[2][0]),self.b21.setText(position_arr[2][1]),self.b22.setText(position_arr[2][2]),self.b23.setText(position_arr[2][3]),self.b24.setText(position_arr[2][4]),self.b25.setText(position_arr[2][5]),self.b26.setText(position_arr[2][6]),self.b27.setText(position_arr[2][7])],
            
            [self.b30.setText(position_arr[3][0]),self.b31.setText(position_arr[3][1]),self.b32.setText(position_arr[3][2]),self.b33.setText(position_arr[3][3]),self.b34.setText(position_arr[3][4]),self.b35.setText(position_arr[3][5]),self.b36.setText(position_arr[3][6]),self.b37.setText(position_arr[3][7])],
            
            [self.b40.setText(position_arr[4][0]),self.b41.setText(position_arr[4][1]),self.b42.setText(position_arr[4][2]),self.b43.setText(position_arr[4][3]),self.b44.setText(position_arr[4][4]),self.b45.setText(position_arr[4][5]),self.b46.setText(position_arr[4][6]),self.b47.setText(position_arr[4][7])],
            
            [self.b50.setText(position_arr[5][0]),self.b51.setText(position_arr[5][1]),self.b52.setText(position_arr[5][2]),self.b53.setText(position_arr[5][3]),self.b54.setText(position_arr[5][4]),self.b55.setText(position_arr[5][5]),self.b56.setText(position_arr[5][6]),self.b57.setText(position_arr[5][7])],
            
            [self.b60.setText(position_arr[6][0]),self.b61.setText(position_arr[6][1]),self.b62.setText(position_arr[6][2]),self.b63.setText(position_arr[6][3]),self.b64.setText(position_arr[6][4]),self.b65.setText(position_arr[6][5]),self.b66.setText(position_arr[6][6]),self.b67.setText(position_arr[6][7])],
            
            [self.b70.setText(position_arr[7][0]),self.b71.setText(position_arr[7][1]),self.b72.setText(position_arr[7][2]),self.b73.setText(position_arr[7][3]),self.b74.setText(position_arr[7][4]),self.b75.setText(position_arr[7][5]),self.b76.setText(position_arr[7][6]),self.b77.setText(position_arr[7][7])]
        ]
        for j in range(8):
            if position_arr[0][j]=="wP":
                if j==0:
                    self.b00.setText("wR")
                if j==7:
                    self.b07.setText("wR")
                if j==1:
                    self.b01.setText("wKn")
                if j==6:
                    self.b06.setText("wKn")
                if j==2:
                    self.b02.setText("wB")
                if j==5:
                    self.b05.setText("wB")
                if j==3:
                    self.b03.setText("wQ")
                if j==4:
                    self.b04.setText("wQ")
            if position_arr[7][j]=="bP":
                if j==0:
                    self.b70.setText("bR")
                if j==7:
                    self.b77.setText("bR")
                if j==1:
                    self.b71.setText("bKn")
                if j==6:
                    self.b76.setText("bKn")
                if j==2:
                    self.b72.setText("bB")
                if j==5:
                    self.b75.setText("bB")
                if j==3:
                    self.b73.setText("bQ")
                if j==4:
                    self.b74.setText("bQ")
        self.clrsrc()
                    

                
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import matchlatlong
from cal import Example
from time import strptime
global from_d, to_d

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 10, 181, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.an_71058 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.an_71058.setObjectName("an_71058")
        self.verticalLayout.addWidget(self.an_71058)
        self.an_9047 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.an_9047.setObjectName("an_9047")
        self.verticalLayout.addWidget(self.an_9047)
        self.an_7653 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.an_7653.setObjectName("an_7653")
        self.verticalLayout.addWidget(self.an_7653)
        self.q2_execute = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.q2_execute.setObjectName("q2_execute")
        self.q2_execute.clicked.connect(self.three_alarms)
        self.verticalLayout.addWidget(self.q2_execute)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 10, 218, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        spacerItem2 = QtWidgets.QSpacerItem(188, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.q2_execute_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.q2_execute_2.setObjectName("q2_execute_2")
        self.q2_execute_2.clicked.connect(self.pci_click)
        self.verticalLayout_2.addWidget(self.q2_execute_2)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        '''
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        '''
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.to_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.to_btn.setObjectName("to_btn")
        self.to_btn.clicked.connect(self.datok)
        self.gridLayout.addWidget(self.to_btn, 5, 2, 1, 1)
        self.q1_execute = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.q1_execute.setObjectName("q1_execute")
        self.q1_execute.clicked.connect(self.q1_exec)
        self.gridLayout.addWidget(self.q1_execute, 7, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.from_date_preview = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.from_date_preview.setObjectName("from_date_preview")
        self.gridLayout.addWidget(self.from_date_preview, 4, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 6, 1, 1, 1)
        '''
        self.to_date_preview = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.to_date_preview.setObjectName("to_date_preview")
        self.gridLayout.addWidget(self.to_date_preview, 5, 1, 1, 1)
        '''
        self.from_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.from_btn.setObjectName("from_btn")
        self.from_btn.clicked.connect(self.from_cal)
        self.gridLayout.addWidget(self.from_btn, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 240, 751, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.q1_execute_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.q1_execute_2.setObjectName("q1_execute_2")
        self.q1_execute_2.clicked.connect(self.faulty_count_click)
        self.horizontalLayout.addWidget(self.q1_execute_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        #lid=self.disp_lcd()
        lid=432
        self.lcdNumber.display(lid)
        self.horizontalLayout.addWidget(self.lcdNumber)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Query 2"))
        self.label_6.setText(_translate("MainWindow", "Select Alarm Numbers"))
        self.an_71058.setText(_translate("MainWindow", "71058"))
        self.an_9047.setText(_translate("MainWindow", "9047"))
        self.an_7653.setText(_translate("MainWindow", "7653"))
        self.q2_execute.setText(_translate("MainWindow", "Execute"))
        self.label_8.setText(_translate("MainWindow", "Query 3"))
        self.label_9.setText(_translate("MainWindow", "Supplementary info like \"%PCI%\""))
        self.q2_execute_2.setText(_translate("MainWindow", "Execute"))
        #self.label_2.setText(_translate("MainWindow", "Date OK"))
        self.label.setText(_translate("MainWindow", "Enter Date"))
        self.to_btn.setText(_translate("MainWindow", "Date OK"))
        self.q1_execute.setText(_translate("MainWindow", "Execute"))
        self.label_3.setText(_translate("MainWindow", "Date Picker"))
        self.from_btn.setText(_translate("MainWindow", "Select"))
        self.label_4.setText(_translate("MainWindow", "Query 1"))
        self.label_7.setText(_translate("MainWindow", "GET COUNT OF E-NODE_B with unresolved Alarms"))
        self.q1_execute_2.setText(_translate("MainWindow", "Get Count"))
    def disp_lcd(self):
        file = open("fault_count.txt", mode='r')
        num=file.read()
        file.close()
        return num
    def three_alarms():
        kk
    def from_cal(self):
        print("ty")
        self.window = QtWidgets.QWidget()
        self.ui = Example()
        self.ui.initUI()
        self.window.show()
    def datok(self):
        date=date_text()
        self.from_date_preview.setText(date)
    def faulty_count_click(self):
        fal_count=matchlatlong.count_faulty()
        file = open("fault_count.txt", mode='w')
        file.write('%s' %fal_count)
        file.close()
        print (fal_count)
        #return fal_count
    def pci_click(self):
        matchlatlong.supp_info_pci()
    def q1_exec(self):
        res1 = self.from_date_preview.text()
        matchlatlong.all_now(res1)
    def date_text():
        file = open("from.txt", mode='r')
        with open('from.txt') as f:
        list=[word for line in f for word in line.split()]
        mon=list[1]
        mon = strptime(str(mon),'%b').tm_mon
        if mon<10:
        mon = '0' + str(mon)
        date=list[3]+'-'+mon +'-'+ list[2]
        file.close()
        print (date)
        return date
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

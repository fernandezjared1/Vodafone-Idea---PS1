from PyQt5.QtWidgets import (QWidget, QCalendarWidget,QLabel, QApplication, QVBoxLayout,QPushButton)
from PyQt5.QtCore import QDate
import sys
global ap
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        vbox = QVBoxLayout(self)
        ap=''
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        vbox.addWidget(cal)
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.ok = QPushButton(self)
        self.ok.setText("OK")
        self.ok.clicked.connect(self.okay)
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.ok)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
    def showDate(self, date):
        self.lbl.setText(date.toString())
        #nonlocal ap
        ap= date.toString()
        file = open("from.txt", mode='w')
        file.write('%s' %ap)
        file.close()
        print(ap)
    def okay(self):
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #doot = QWidget()
    ex = Example()
    #ex.initUI(doot)
    #ex.show()
    sys.exit(app.exec_())

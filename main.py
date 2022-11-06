from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class clock(QMainWindow):
    def __init__(self):
        super().__init__()
        timer=QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle('clock')
        self.setGeometry(500,500,600,600)
        self.setStyleSheet('background:black;')
        self.Hpointer=QtGui.QPolygon([QPoint(4,7),QPoint(-4,7),QPoint(0,-50)])
        self.Mpointer=QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-70)])
        self.Spointer=QtGui.QPolygon([QPoint(1,1),QPoint(-1,1),QPoint(0,-90)])
        self.Bcolor=Qt.green
        self.Scolor=Qt.red
        self.Mcolor=Qt.blue
    def paintEvent(self,event):
        rec=min(self.width(),self.height())
        tik=QTime.currentTime()
        painter=QPainter(self)
        def drawPointer(color,rotation,pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2,self.height()/2)
        painter.scale(rec/200,rec/200)
        painter.setPen(QtCore.Qt.NoPen)
        drawPointer(self.Bcolor,(30*(tik.hour()+tik.minute()/60)),self.Hpointer)
        drawPointer(self.Mcolor,(6*(tik.minute()+tik.second()/60)),self.Mpointer)
        drawPointer(self.Scolor,(6*tik.second()),self.Spointer)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=clock()
win.show()
exit(app.exec_())

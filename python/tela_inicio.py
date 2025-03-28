from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

import fme

class Ui_Pag_inicial(object):
    def setupUi(self, Pag_inicial):
        if not Pag_inicial.objectName():
            Pag_inicial.setObjectName(u"Pag_inicial")
        Pag_inicial.resize(1002, 477)
        self.tela_inicial = QWidget(Pag_inicial)
        self.tela_inicial.setObjectName(u"tela_inicial")
        self.Home = QFrame(self.tela_inicial)
        self.Home.setObjectName(u"Home")
        self.Home.setGeometry(QRect(40, 40, 931, 411))
        self.Home.setFrameShape(QFrame.Shape.StyledPanel)
        self.Home.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_CineFilmes = QLabel(self.Home)
        self.txt_CineFilmes.setObjectName(u"txt_CineFilmes")
        self.txt_CineFilmes.setGeometry(QRect(10, 10, 171, 41))
        self.txt_CineFilmes.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";\n"
"font: 900 22pt \"Segoe UI\";")
        self.txt_Seu_Guia_de_Filmes_e_Series = QLabel(self.Home)
        self.txt_Seu_Guia_de_Filmes_e_Series.setObjectName(u"txt_Seu_Guia_de_Filmes_e_Series")
        self.txt_Seu_Guia_de_Filmes_e_Series.setGeometry(QRect(10, 120, 381, 51))
        self.txt_Seu_Guia_de_Filmes_e_Series.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 22pt \"Segoe UI\";")
        self.txt_Venha_conferir = QLabel(self.Home)
        self.txt_Venha_conferir.setObjectName(u"txt_Venha_conferir")
        self.txt_Venha_conferir.setGeometry(QRect(20, 170, 131, 16))
        self.txt_Venha_conferir.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 12pt \"Segoe UI\";")
        self.btn_Entrar = QPushButton(self.Home)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setGeometry(QRect(20, 220, 231, 31))
        self.btn_Entrar.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.tela_de_inicio = QLabel(self.Home)
        self.tela_de_inicio.setObjectName(u"tela_de_inicio")
        self.tela_de_inicio.setGeometry(QRect(-10, -10, 981, 451))
        self.tela_de_inicio.setPixmap(QPixmap(u":/fme/fme.jpg"))
        self.tela_de_inicio.setScaledContents(True)
        self.Img_inicio = QLabel(self.Home)
        self.Img_inicio.setObjectName(u"Img_inicio")
        self.Img_inicio.setGeometry(QRect(0, -1, 931, 421))
        self.Img_inicio.setPixmap(QPixmap(u":/icon 01/fme.jpg"))
        self.Img_inicio.setScaledContents(True)
        self.Img_inicio.raise_()
        self.tela_de_inicio.raise_()
        self.txt_CineFilmes.raise_()
        self.txt_Seu_Guia_de_Filmes_e_Series.raise_()
        self.txt_Venha_conferir.raise_()
        self.btn_Entrar.raise_()
        Pag_inicial.setCentralWidget(self.tela_inicial)

        self.retranslateUi(Pag_inicial)

        QMetaObject.connectSlotsByName(Pag_inicial)
    # setupUi

    def retranslateUi(self, Pag_inicial):
        Pag_inicial.setWindowTitle(QCoreApplication.translate("Pag_inicial", u"MainWindow", None))
        self.txt_CineFilmes.setText(QCoreApplication.translate("Pag_inicial", u"CineFilmes", None))
        self.txt_Seu_Guia_de_Filmes_e_Series.setText(QCoreApplication.translate("Pag_inicial", u"Seu Guia de Filmes e S\u00e9ries.", None))
        self.txt_Venha_conferir.setText(QCoreApplication.translate("Pag_inicial", u"Venha conferir.", None))
        self.btn_Entrar.setText(QCoreApplication.translate("Pag_inicial", u"Entrar", None))
        self.tela_de_inicio.setText("")
        self.Img_inicio.setText("")
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_inicio import Ui_Pag_inicial

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Pag_inicial()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

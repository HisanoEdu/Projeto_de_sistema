from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

import perfil

class Ui_tela_perfil(object):
    def setupUi(self, tela_perfil):
        if not tela_perfil.objectName():
            tela_perfil.setObjectName(u"tela_perfil")
        tela_perfil.resize(1004, 471)
        self.tela_Perfil_1 = QWidget(tela_perfil)
        self.tela_Perfil_1.setObjectName(u"tela_Perfil_1")
        self.tela_de_perfil = QFrame(self.tela_Perfil_1)
        self.tela_de_perfil.setObjectName(u"tela_de_perfil")
        self.tela_de_perfil.setGeometry(QRect(120, 10, 791, 401))
        self.tela_de_perfil.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.tela_de_perfil.setFrameShape(QFrame.Shape.StyledPanel)
        self.tela_de_perfil.setFrameShadow(QFrame.Shadow.Raised)
        self.barra = QFrame(self.tela_de_perfil)
        self.barra.setObjectName(u"barra")
        self.barra.setGeometry(QRect(0, 0, 811, 51))
        self.barra.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.barra.setFrameShape(QFrame.Shape.StyledPanel)
        self.barra.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Cine_filme = QLabel(self.barra)
        self.btn_Cine_filme.setObjectName(u"btn_Cine_filme")
        self.btn_Cine_filme.setGeometry(QRect(10, 10, 161, 41))
        self.btn_Cine_filme.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 900 22pt \"Segoe UI\";")
        self.btn_Filmes_e_Series = QPushButton(self.barra)
        self.btn_Filmes_e_Series.setObjectName(u"btn_Filmes_e_Series")
        self.btn_Filmes_e_Series.setGeometry(QRect(200, 20, 101, 24))
        self.btn_Filmes_e_Series.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(34, 31, 31);")
        self.btn_Recomendacao_aleatorio = QPushButton(self.barra)
        self.btn_Recomendacao_aleatorio.setObjectName(u"btn_Recomendacao_aleatorio")
        self.btn_Recomendacao_aleatorio.setGeometry(QRect(330, 20, 171, 24))
        self.btn_Recomendacao_aleatorio.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Recomendacao_aleatorio.raise_()
        self.btn_Cine_filme.raise_()
        self.btn_Filmes_e_Series.raise_()
        self.btn_Icon_perfil = QLabel(self.tela_de_perfil)
        self.btn_Icon_perfil.setObjectName(u"btn_Icon_perfil")
        self.btn_Icon_perfil.setGeometry(QRect(130, 150, 81, 81))
        self.btn_Icon_perfil.setPixmap(QPixmap(u":/perfil 1/icon_perfil.png"))
        self.btn_Icon_perfil.setScaledContents(True)
        self.tela_inscricao = QFrame(self.tela_de_perfil)
        self.tela_inscricao.setObjectName(u"tela_inscricao")
        self.tela_inscricao.setGeometry(QRect(240, 110, 391, 211))
        self.tela_inscricao.setStyleSheet(u"background-color: rgb(34, 31, 31);")
        self.tela_inscricao.setFrameShape(QFrame.Shape.StyledPanel)
        self.tela_inscricao.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_Nome = QLabel(self.tela_inscricao)
        self.txt_Nome.setObjectName(u"txt_Nome")
        self.txt_Nome.setGeometry(QRect(20, 20, 49, 16))
        self.txt_Nome.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Nome = QLineEdit(self.tela_inscricao)
        self.btn_Nome.setObjectName(u"btn_Nome")
        self.btn_Nome.setGeometry(QRect(20, 40, 321, 21))
        self.btn_Nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_E_mail = QLabel(self.tela_inscricao)
        self.txt_E_mail.setObjectName(u"txt_E_mail")
        self.txt_E_mail.setGeometry(QRect(20, 70, 49, 16))
        self.txt_E_mail.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_e_mail = QLineEdit(self.tela_inscricao)
        self.btn_e_mail.setObjectName(u"btn_e_mail")
        self.btn_e_mail.setGeometry(QRect(20, 90, 321, 21))
        self.btn_e_mail.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_Senha = QLabel(self.tela_inscricao)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(20, 120, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Senha = QLineEdit(self.tela_inscricao)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(20, 140, 321, 21))
        self.btn_Senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)
        tela_perfil.setCentralWidget(self.tela_Perfil_1)
        self.menubar = QMenuBar(tela_perfil)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1004, 33))
        tela_perfil.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(tela_perfil)
        self.statusbar.setObjectName(u"statusbar")
        tela_perfil.setStatusBar(self.statusbar)

        self.retranslateUi(tela_perfil)

        QMetaObject.connectSlotsByName(tela_perfil)
    # setupUi

    def retranslateUi(self, tela_perfil):
        tela_perfil.setWindowTitle(QCoreApplication.translate("tela_perfil", u"MainWindow", None))
        self.btn_Cine_filme.setText(QCoreApplication.translate("tela_perfil", u"CineFilmes", None))
        self.btn_Filmes_e_Series.setText(QCoreApplication.translate("tela_perfil", u"Filmes e S\u00e9ries", None))
        self.btn_Recomendacao_aleatorio.setText(QCoreApplication.translate("tela_perfil", u"Recomenda\u00e7\u00e3o aleat\u00f3rio", None))
        self.btn_Icon_perfil.setText("")
        self.txt_Nome.setText(QCoreApplication.translate("tela_perfil", u"Nome", None))
        self.txt_E_mail.setText(QCoreApplication.translate("tela_perfil", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("tela_perfil", u"Senha", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from tela_perfil import Ui_tela_perfil

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_perfil()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

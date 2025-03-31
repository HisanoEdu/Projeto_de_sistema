from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

# No meu não tem isso ksksk, era botão com cor estática

import fme
from cadastro import Ui_tela_Cadastro  
from login import Ui_login  

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
        
        # Logo "CineFilmes"
        self.txt_CineFilmes = QLabel(self.Home)
        self.txt_CineFilmes.setObjectName(u"txt_CineFilmes")
        self.txt_CineFilmes.setGeometry(QRect(10, 10, 171, 41))
        self.txt_CineFilmes.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";\n"
"font: 900 22pt \"Segoe UI\";")
        
        # Texto "Seu Guia de Filmes e Séries"
        self.txt_Seu_Guia_de_Filmes_e_Series = QLabel(self.Home)
        self.txt_Seu_Guia_de_Filmes_e_Series.setObjectName(u"txt_Seu_Guia_de_Filmes_e_Series")
        self.txt_Seu_Guia_de_Filmes_e_Series.setGeometry(QRect(10, 120, 381, 51))
        self.txt_Seu_Guia_de_Filmes_e_Series.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 22pt \"Segoe UI\";")
        
        # Texto "Venha conferir"
        self.txt_Venha_conferir = QLabel(self.Home)
        self.txt_Venha_conferir.setObjectName(u"txt_Venha_conferir")
        self.txt_Venha_conferir.setGeometry(QRect(20, 170, 131, 16))
        self.txt_Venha_conferir.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 12pt \"Segoe UI\";")
        
        # Botão "Entrar"
        self.btn_Entrar = QPushButton(self.Home)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setGeometry(QRect(20, 220, 231, 31))
        self.btn_Entrar.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        
        # Conectar o botão "Entrar" à função que abre a tela de login
        self.btn_Entrar.clicked.connect(lambda: self.abrir_tela_login(Pag_inicial))
        
        # Imagem de fundo (tela_de_inicio)
        self.tela_de_inicio = QLabel(self.Home)
        self.tela_de_inicio.setObjectName(u"tela_de_inicio")
        self.tela_de_inicio.setGeometry(QRect(-10, -10, 981, 451))
        self.tela_de_inicio.setPixmap(QPixmap(u":/fme/fme.jpg"))
        self.tela_de_inicio.setScaledContents(True)
        
        # Imagem adicional (Img_inicio)
        self.Img_inicio = QLabel(self.Home)
        self.Img_inicio.setObjectName(u"Img_inicio")
        self.Img_inicio.setGeometry(QRect(0, -1, 931, 421))
        self.Img_inicio.setPixmap(QPixmap(u":/icon 01/fme.jpg"))
        self.Img_inicio.setScaledContents(True)
        
        # Botão "Cadastrar"
        self.btn_Cadastrar = QPushButton(self.Home)
        self.btn_Cadastrar.setObjectName(u"btn_Cadastrar")
        self.btn_Cadastrar.setGeometry(QRect(740, 10, 171, 31))
        self.btn_Cadastrar.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        
        # Conectar o botão "Cadastrar" à função que abre a tela de cadastro
        self.btn_Cadastrar.clicked.connect(lambda: self.abrir_tela_cadastro(Pag_inicial))
        
        # Ordem de camadas
        self.Img_inicio.raise_()
        self.tela_de_inicio.raise_()
        self.txt_CineFilmes.raise_()
        self.txt_Seu_Guia_de_Filmes_e_Series.raise_()
        self.txt_Venha_conferir.raise_()
        self.btn_Entrar.raise_()
        self.btn_Cadastrar.raise_()
        
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
        self.btn_Cadastrar.setText(QCoreApplication.translate("Pag_inicial", u"Cadastrar", None))
    # retranslateUi

    def abrir_tela_cadastro(self, janela_atual):
        janela_atual.close()  # Fecha a tela inicial
        self.tela_cadastro = QMainWindow()
        self.ui_cadastro = Ui_tela_Cadastro()
        self.ui_cadastro.setupUi(self.tela_cadastro)
        self.tela_cadastro.show()

    def abrir_tela_login(self, janela_atual):
        janela_atual.close()  # Fecha a tela inicial
        self.tela_login = QMainWindow()
        self.ui_login = Ui_login()
        self.ui_login.setupUi(self.tela_login)
        self.tela_login.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Pag_inicial()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
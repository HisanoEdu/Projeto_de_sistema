from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy, QMessageBox,
    QWidget)
import mysql.connector  # Conector para MySQL
from mysql.connector import Error
#deu certo! ai como fica o email e senha do so usuario
#vou te explicar assim que eu fazer o login
import fme

class Ui_tela_Cadastro(object):
    def setupUi(self, tela_Cadastro):
        if not tela_Cadastro.objectName():
            tela_Cadastro.setObjectName(u"tela_Cadastro")
        tela_Cadastro.resize(1104, 509)
        self.Cadastro = QWidget(tela_Cadastro)
        self.Cadastro.setObjectName(u"Cadastro")
        self.Cadastrar = QFrame(self.Cadastro)
        self.Cadastrar.setObjectName(u"Cadastrar")
        self.Cadastrar.setGeometry(QRect(40, 10, 1031, 441))
        self.Cadastrar.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cadastrar.setFrameShadow(QFrame.Shadow.Raised)
        self.Tela_Cadastro = QFrame(self.Cadastrar)
        self.Tela_Cadastro.setObjectName(u"Tela_Cadastro")
        self.Tela_Cadastro.setGeometry(QRect(330, 30, 341, 391))
        self.Tela_Cadastro.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.Tela_Cadastro.setFrameShape(QFrame.Shape.StyledPanel)
        self.Tela_Cadastro.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_Cadastro = QLabel(self.Tela_Cadastro)
        self.txt_Cadastro.setObjectName(u"txt_Cadastro")
        self.txt_Cadastro.setGeometry(QRect(100, 30, 141, 31))
        self.txt_Cadastro.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 22pt \"Segoe UI\";")
        self.txt_Nome = QLabel(self.Tela_Cadastro)
        self.txt_Nome.setObjectName(u"txt_Nome")
        self.txt_Nome.setGeometry(QRect(20, 80, 49, 16))
        self.txt_Nome.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Email = QLabel(self.Tela_Cadastro)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setGeometry(QRect(20, 140, 49, 16))
        self.txt_Email.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Senha = QLabel(self.Tela_Cadastro)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(20, 200, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Senha = QLineEdit(self.Tela_Cadastro)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(20, 220, 301, 21))
        self.btn_Senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_Email = QLineEdit(self.Tela_Cadastro)
        self.btn_Email.setObjectName(u"btn_Email")
        self.btn_Email.setGeometry(QRect(20, 160, 301, 21))
        self.btn_Email.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Nome = QLineEdit(self.Tela_Cadastro)
        self.btn_Nome.setObjectName(u"btn_Nome")
        self.btn_Nome.setGeometry(QRect(20, 100, 301, 21))
        self.btn_Nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Cadastro = QPushButton(self.Tela_Cadastro)
        self.btn_Cadastro.setObjectName(u"btn_Cadastro")
        self.btn_Cadastro.setGeometry(QRect(80, 290, 171, 31))
        self.btn_Cadastro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.label = QLabel(self.Cadastrar) 
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1041, 471))
        self.label.setPixmap(QPixmap(u":/icon 01/fme.jpg"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.Tela_Cadastro.raise_()
        tela_Cadastro.setCentralWidget(self.Cadastro)
        self.menubar = QMenuBar(tela_Cadastro)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1104, 33))
        tela_Cadastro.setMenuBar(self.menubar)

        self.retranslateUi(tela_Cadastro)

        QMetaObject.connectSlotsByName(tela_Cadastro)

        self.btn_Cadastro.clicked.connect(lambda: self.cadastrar(tela_Cadastro))


    # setupUi

    def retranslateUi(self, tela_Cadastro):
        tela_Cadastro.setWindowTitle(QCoreApplication.translate("tela_Cadastro", u"MainWindow", None))
        self.txt_Cadastro.setText(QCoreApplication.translate("tela_Cadastro", u"Cadastrar", None))
        self.txt_Nome.setText(QCoreApplication.translate("tela_Cadastro", u"Nome", None))
        self.txt_Email.setText(QCoreApplication.translate("tela_Cadastro", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("tela_Cadastro", u"Senha", None))
        self.btn_Cadastro.setText(QCoreApplication.translate("tela_Cadastro", u"Cadastrar", None))
        self.label.setText("")
    # retranslateUi
    def cadastrar(self, janela_atual):
        # Obter os dados inseridos
        nome = self.btn_Nome.text()
        email = self.btn_Email.text()
        senha = self.btn_Senha.text()
        ###Seu banco de dados tem senha? não, a configuração ta certa? sim
        conn = None  # Inicializa conn como None fora do try
        try:
            # Conectar ao banco de dados MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",        # Ajuste para o seu host
                user="root",             # Ajuste para o seu usuário
                password="",         # Ajuste para a sua senha
                database="cinefilmes_db" # Ajuste para o nome do seu banco
            )# quando vc chegar na sala, caso vc tiver que ir pra outro computador ou algo assim, vc vai colocar o comando: create database cinefilmes_db, cria ele lá pra vc ver como é sim
            cursor = conn.cursor() # é nela que esta tanto o login como o cadastro, isso, ai vc cria no mysql,certo

            # Criar a tabela 'usuarios' se ela não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    senha VARCHAR(100) NOT NULL,
                    tipo_usuario enum('usuario','admin') DEFAULT 'usuario'
                )
            ''')# 

            # Inserir o usuário na tabela (senha em texto puro)
            cursor.execute('''
                INSERT INTO usuarios (nome, email, senha)
                VALUES (%s, %s, %s)
            ''', (nome, email, senha))
            conn.commit()

            # Exibir mensagem de sucesso
            QMessageBox.information(None, "Sucesso", "Usuário cadastrado com sucesso!")
            
            # Fechar a tela de cadastro e abrir a tela inicial
            janela_atual.close()
            self.abrir_tela_inicial()

        except mysql.connector.Error as err:
            if err.errno == 1062:  # Erro de duplicata (email já existe)
                QMessageBox.warning(None, "Erro", f"O email {email} já está cadastrado.")
            else:
                QMessageBox.critical(None, "Erro", f"Erro ao conectar ou inserir no MySQL: {err}")
        finally:
            # Fechar a conexão apenas se ela foi estabelecida
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()

    def abrir_tela_inicial(self):
        # Importar Tela_Inicio aqui para evitar importação circular no carregamento do módulo
        from tela_inicio import Ui_Pag_inicial
        self.tela_inicial = QMainWindow()
        self.ui_inicial = Ui_Pag_inicial()
        self.ui_inicial.setupUi(self.tela_inicial)
        self.tela_inicial.show()


import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from cadastro import Ui_tela_Cadastro

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_tela_Cadastro()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

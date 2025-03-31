
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget, QMainWindow, QMessageBox)


## Essa tela de login também deu erro, mas depois a gente volta nela pode ser? pode
#viu desculpa sem problemas

import mysql.connector
from mysql.connector import Error
from cadastro import Ui_tela_Cadastro
from Tela_home import MainWindow as TelaPrincipalMainWindow
from banco import CadastroImagem as TelaCadastroImagem  # Importando a tela de cadastro de imagens

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1089, 509)
        self.tela_login = QFrame(login)
        self.tela_login.setObjectName(u"tela_login")
        self.tela_login.setGeometry(QRect(70, 20, 981, 441))
        self.tela_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.tela_login.setFrameShadow(QFrame.Shadow.Raised)
        self.img_foto_fundo = QLabel(self.tela_login)
        self.img_foto_fundo.setObjectName(u"img_foto_fundo")
        self.img_foto_fundo.setGeometry(QRect(0, 0, 981, 441))
        self.img_foto_fundo.setPixmap(QPixmap(u":/fme/fme.jpg"))
        self.img_foto_fundo.setScaledContents(True)
        self.rtn_login = QFrame(self.tela_login)
        self.rtn_login.setObjectName(u"rtn_login")
        self.rtn_login.setGeometry(QRect(330, 30, 331, 391))
        self.rtn_login.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.rtn_login.setFrameShape(QFrame.Shape.StyledPanel)
        self.rtn_login.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_Email = QLineEdit(self.rtn_login)
        self.btn_Email.setObjectName(u"btn_Email")
        self.btn_Email.setGeometry(QRect(20, 130, 291, 21))
        self.btn_Email.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Senha = QLineEdit(self.rtn_login)
        self.btn_Senha.setObjectName(u"btn_Senha")
        self.btn_Senha.setGeometry(QRect(20, 200, 291, 21))
        self.btn_Senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_Senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_Entrar = QPushButton(self.rtn_login)
        self.btn_Entrar.setObjectName(u"btn_Entrar")
        self.btn_Entrar.setGeometry(QRect(80, 270, 161, 31))
        self.btn_Entrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(255, 0, 0);")
        self.txt_login = QLabel(self.rtn_login)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setGeometry(QRect(120, 30, 91, 41))
        self.txt_login.setStyleSheet(u"color: rgb(255, 0, 0);\n"
                                     "font: 22pt \"Segoe UI\";")
        self.txt_Email = QLabel(self.rtn_login)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setGeometry(QRect(20, 110, 49, 16))
        self.txt_Email.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.txt_Senha = QLabel(self.rtn_login)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(20, 180, 49, 16))
        self.txt_Senha.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_Cadastrese = QPushButton(self.rtn_login)
        self.btn_Cadastrese.setObjectName(u"btn_Cadastrese")
        self.btn_Cadastrese.setGeometry(QRect(120, 320, 75, 24))
        self.btn_Cadastrese.setStyleSheet(u"color: rgb(255, 0, 0);")

        # Conectar os botões às funções
        self.btn_Cadastrese.clicked.connect(self.cadastrese)
        self.btn_Entrar.clicked.connect(lambda: self.verificar_login(login))

        # Criar o admin padrão ao iniciar
        self.criar_admin_padrao()

        self.retranslateUi(login)

    def criar_admin_padrao(self):
        conn = None
        try:
            # Conectar ao banco de dados MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="cinefilmes_db"
            )
            cursor = conn.cursor()

            # Verificar se o admin padrão já existe
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = %s", ("adm@",))
            admin_existe = cursor.fetchone()[0]

            if admin_existe == 0:
                # Inserir o admin padrão se não existir
                cursor.execute("""
                    INSERT INTO usuarios (nome, email, senha, tipo_usuario)
                    VALUES (%s, %s, %s, %s)
                """, ("Admin", "adm@", "adm123", "admin"))
                conn.commit()
                print("Usuário admin padrão criado: adm@ / adm123")
            else:
                print("Usuário admin padrão já existe no banco de dados.")

        except mysql.connector.Error as err:
            print(f"Erro ao criar admin padrão: {err}")
        finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()

    def cadastrese(self):
        self.window_cadastro = QMainWindow()
        self.ui_cadastro = Ui_tela_Cadastro()
        self.ui_cadastro.setupUi(self.window_cadastro)
        self.window_cadastro.show()

    def verificar_login(self, janela_atual):
        # Obter os dados inseridos
        email = self.btn_Email.text().strip()
        senha = self.btn_Senha.text().strip()

        # Verificar se os campos estão preenchidos
        if not email or not senha:
            QMessageBox.warning(janela_atual, "Erro", "Por favor, preencha todos os campos!")
            return

        conn = None
        try:
            # Conectar ao banco de dados MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="cinefilmes_db"
            )
            cursor = conn.cursor()

            # Consultar o banco para verificar email, senha e tipo_usuario
            cursor.execute("SELECT tipo_usuario FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
            resultado = cursor.fetchone()

            if resultado:
                tipo_usuario = resultado[0]
                QMessageBox.information(janela_atual, "Sucesso", f"Login realizado com sucesso! Bem-vindo(a), {tipo_usuario.capitalize()}!")
                janela_atual.close()

                if tipo_usuario == "admin":
                    print("AAAAAAAA")
                    # Abrir Tela_Cadastro_Imagem.py para admin
                    self.tela_cadastro_imagem = TelaCadastroImagem()
                    self.tela_cadastro_imagem.show()
                elif tipo_usuario == "usuario":
                    # Abrir Tela_home.py para usuário comum, passando o email
                    self.tela_principal = TelaPrincipalMainWindow(email_usuario=email)
                    self.tela_principal.show()
                else:
                    QMessageBox.critical(janela_atual, "Erro", "Tipo de usuário inválido!")
            else:
                # Login falhou
                QMessageBox.critical(janela_atual, "Erro", "Email ou senha incorretos!")

        except mysql.connector.Error as err:
            QMessageBox.critical(janela_atual, "Erro", f"Erro ao conectar ao banco de dados: {err}")
        finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.img_foto_fundo.setText("")
        self.btn_Senha.setText("")
        self.btn_Entrar.setText(QCoreApplication.translate("login", u"Entrar", None))
        self.txt_login.setText(QCoreApplication.translate("login", u"Login", None))
        self.txt_Email.setText(QCoreApplication.translate("login", u"E-mail", None))
        self.txt_Senha.setText(QCoreApplication.translate("login", u"Senha", None))
        self.btn_Cadastrese.setText(QCoreApplication.translate("login", u"Cadastre-se", None))

# Para teste standalone
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login_window = QMainWindow()
    ui = Ui_login()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec())
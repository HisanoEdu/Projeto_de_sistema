# -*- coding: utf-8 -*-

import sys
import mysql.connector
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QFrame, QPushButton, QSpacerItem, QSizePolicy, QMessageBox,
                               QDialog, QFormLayout, QLineEdit)
from PySide6.QtCore import Qt, QSize, QCoreApplication, QMetaObject
from PySide6.QtGui import QPixmap, QImage, QFont

# Configuração do banco de dados MySQL
banco = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'cinefilmes_db'
}

# Classe para o diálogo de edição de usuário
class EditUserDialog(QDialog):
    def __init__(self, parent=None, email_usuario=None):
        super().__init__(parent)
        self.email_usuario = email_usuario  # Email do usuário logado
        self.setWindowTitle("Editar Dados do Usuário")
        self.setMinimumSize(QSize(400, 300))
        self.setStyleSheet("background: #221F1F; color: white;")

        # Layout principal do diálogo
        layout = QFormLayout(self)

        # Campos de entrada
        self.nome_input = QLineEdit(self)
        self.nome_input.setStyleSheet("background: white; color: black; border-radius: 5px; padding: 5px;")
        layout.addRow("Nome:", self.nome_input)

        # Email como somente leitura
        self.email_input = QLineEdit(self)
        self.email_input.setReadOnly(True)
        self.email_input.setStyleSheet("background: #d3d3d3; color: black; border-radius: 5px; padding: 5px;")
        layout.addRow("Email:", self.email_input)

        self.senha_input = QLineEdit(self)
        self.senha_input.setEchoMode(QLineEdit.Password)
        self.senha_input.setStyleSheet("background: white; color: black; border-radius: 5px; padding: 5px;")
        layout.addRow("Senha:", self.senha_input)

        # Botões
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Salvar", self)
        self.save_button.setStyleSheet("background: red; color: white; border-radius: 5px; padding: 5px;")
        self.save_button.clicked.connect(self.salvar_dados)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton("Cancelar", self)
        self.cancel_button.setStyleSheet("background: gray; color: white; border-radius: 5px; padding: 5px;")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)

        layout.addRow(button_layout)

        # Carregar dados do usuário logado
        self.carregar_dados_usuario()

    def carregar_dados_usuario(self):
        try:
            if not self.email_usuario:
                QMessageBox.warning(self, "Atenção", "Nenhum usuário logado!")
                return
            conn = mysql.connector.connect(**banco)
            cursor = conn.cursor()
            cursor.execute("SELECT nome, email, senha FROM usuarios WHERE email = %s", (self.email_usuario,))
            resultado = cursor.fetchone()
            if resultado:
                nome, email, senha = resultado
                self.nome_input.setText(nome)
                self.email_input.setText(email)
                self.senha_input.setText(senha)
            else:
                QMessageBox.warning(self, "Atenção", "Usuário não encontrado no banco de dados!")
            conn.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {str(e)}")

    def salvar_dados(self):
        nome = self.nome_input.text().strip()
        senha = self.senha_input.text().strip()
        email = self.email_input.text().strip()

        if not nome or not senha:
            QMessageBox.warning(self, "Atenção", "Nome e senha devem ser preenchidos!")
            return

        try:
            conn = mysql.connector.connect(**banco)
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE usuarios SET nome = %s, senha = %s WHERE email = %s",
                (nome, senha, email)
            )
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Sucesso", "Dados atualizados com sucesso!")
            self.accept()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar dados: {str(e)}")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Frame superior (cabeçalho)
        self.Frame_Todo = QFrame(self.centralwidget)
        self.Frame_Todo.setObjectName(u"Frame_Todo")
        self.Frame_Todo.setMaximumSize(QSize(16777215, 80))
        self.Frame_Todo.setStyleSheet(u"background: #221F1F;")
        self.Frame_Todo.setFrameShape(QFrame.StyledPanel)
        self.Frame_Todo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_Todo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 10, 20, 10)  # Adicionado padding
        self.horizontalLayout.setSpacing(10)  # Adicionado espaçamento

        self.Frame_Espaco3 = QFrame(self.Frame_Todo)
        self.Frame_Espaco3.setObjectName(u"Frame_Espaco3")
        self.Frame_Espaco3.setMaximumSize(QSize(50, 100))
        self.Frame_Espaco3.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco3)

        self.txt_Logo = QLabel(self.Frame_Todo)
        self.txt_Logo.setObjectName(u"txt_Logo")
        self.txt_Logo.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.txt_Logo.setFont(font)
        self.txt_Logo.setStyleSheet(u"color: red;")
        self.horizontalLayout.addWidget(self.txt_Logo)

        self.Btn_Inicio = QPushButton(self.Frame_Todo)
        self.Btn_Inicio.setObjectName(u"Btn_Inicio")
        self.Btn_Inicio.setMaximumSize(QSize(130, 16777215))
        self.Btn_Inicio.setStyleSheet(u"color: red; border: none; background: transparent; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_Inicio)

        self.Btn_FileseSeries = QPushButton(self.Frame_Todo)
        self.Btn_FileseSeries.setObjectName(u"Btn_FileseSeries")
        self.Btn_FileseSeries.setMaximumSize(QSize(130, 16777215))
        self.Btn_FileseSeries.setStyleSheet(u"border: none; color: red; background: transparent; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_FileseSeries)

        self.Frame_Espaco1 = QFrame(self.Frame_Todo)
        self.Frame_Espaco1.setObjectName(u"Frame_Espaco1")
        self.Frame_Espaco1.setMaximumSize(QSize(20, 16777215))
        self.Frame_Espaco1.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco1)

        self.Btn_Recomendacao = QPushButton(self.Frame_Todo)
        self.Btn_Recomendacao.setObjectName(u"Btn_Recomendacao")
        self.Btn_Recomendacao.setMaximumSize(QSize(200, 16777215))  # Aumentado para 200 para evitar corte
        self.Btn_Recomendacao.setStyleSheet(u"border: none; color: red; background: transparent; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_Recomendacao)

        self.Frame_Espaco2 = QFrame(self.Frame_Todo)
        self.Frame_Espaco2.setObjectName(u"Frame_Espaco2")
        self.Frame_Espaco2.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco2)

        # Botão "Sair"
        self.Btn_Sair = QPushButton(self.Frame_Todo)
        self.Btn_Sair.setObjectName(u"Btn_Sair")
        self.Btn_Sair.setMinimumSize(QSize(80, 30))
        self.Btn_Sair.setStyleSheet(u"color: white; background: red; border: none; border-radius: 5px; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_Sair)

        # Botão "Editar Dados"
        self.Btn_Editar_Dados = QPushButton(self.Frame_Todo)
        self.Btn_Editar_Dados.setObjectName(u"Btn_Editar_Dados")
        self.Btn_Editar_Dados.setMinimumSize(QSize(120, 30))
        self.Btn_Editar_Dados.setStyleSheet(u"color: white; background: red; border: none; border-radius: 5px; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_Editar_Dados)

        self.verticalLayout.addWidget(self.Frame_Todo)

        # Frame principal (corpo da tela)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: #000000;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Espaçador superior para dar margin-top ao título
        self.top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(self.top_spacer)

        # Título "Recomendação Aleatória"
        self.title_label = QLabel(self.frame_2)
        self.title_label.setObjectName(u"title_label")
        font_title = QFont()
        font_title.setFamilies([u"Segoe UI"])
        font_title.setPointSize(24)
        font_title.setBold(True)
        self.title_label.setFont(font_title)
        self.title_label.setStyleSheet(u"color: red;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.title_label)

        # Frame para o conteúdo do filme (card + nome)
        self.content_frame = QFrame(self.frame_2)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"background: transparent;")
        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setAlignment(Qt.AlignCenter)
        self.content_layout.setSpacing(10)

        # Placeholder para o card do filme
        self.movie_card = QLabel(self.content_frame)
        self.movie_card.setObjectName(u"movie_card")
        self.movie_card.setFixedSize(240, 320)
        self.movie_card.setAlignment(Qt.AlignCenter)
        self.movie_card.setStyleSheet(u"background: transparent;")
        self.content_layout.addWidget(self.movie_card)

        # Placeholder para o nome do filme
        self.movie_name = QLabel(self.content_frame)
        self.movie_name.setObjectName(u"movie_name")
        font_name = QFont()
        font_name.setFamilies([u"Segoe UI"])
        font_name.setPointSize(16)
        self.movie_name.setFont(font_name)
        self.movie_name.setStyleSheet(u"color: white;")
        self.movie_name.setAlignment(Qt.AlignCenter)
        self.content_layout.addWidget(self.movie_name)

        self.verticalLayout_2.addWidget(self.content_frame)

        # Botão "Recomendar"
        self.recommend_button = QPushButton(self.frame_2)
        self.recommend_button.setObjectName(u"recommend_button")
        self.recommend_button.setMaximumSize(QSize(200, 40))
        self.recommend_button.setStyleSheet(u"color: white; background: red; border: 1px solid red; border-radius: 5px; padding: 5px;")
        self.recommend_button.setFont(font_name)
        self.verticalLayout_2.addWidget(self.recommend_button, alignment=Qt.AlignCenter)

        # Espaço inferior
        self.verticalLayout_2.addStretch()

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Recomendação Aleatória", None))
        self.txt_Logo.setText(QCoreApplication.translate("MainWindow", u"CineFilmes", None))
        self.Btn_Inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.Btn_FileseSeries.setText(QCoreApplication.translate("MainWindow", u"Filmes e Series", None))
        self.Btn_Recomendacao.setText(QCoreApplication.translate("MainWindow", u"Recomenda\u00e7\u00e3o Aleatoria", None))
        self.Btn_Sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.Btn_Editar_Dados.setText(QCoreApplication.translate("MainWindow", u"Editar Dados", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Recomendação Aleatória", None))
        self.movie_name.setText("")  # Inicialmente vazio
        self.recommend_button.setText(QCoreApplication.translate("MainWindow", u"Recomendar", None))

class MainWindow(QMainWindow):
    def __init__(self, email_usuario=None):
        super().__init__()
        self.email_usuario = email_usuario  # Armazenar o email do usuário logado
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectar os botões
        self.ui.recommend_button.clicked.connect(self.recomendar_filme)
        self.ui.Btn_Inicio.clicked.connect(self.voltar_para_tela_principal)
        self.ui.Btn_FileseSeries.clicked.connect(self.abrir_tela_filmes_series)
        self.ui.Btn_Sair.clicked.connect(self.sair)
        self.ui.Btn_Editar_Dados.clicked.connect(self.editar_dados)

        # Carregar uma recomendação inicial
        self.recomendar_filme()

    def recomendar_filme(self):
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**banco)
            cursor = conn.cursor()

            # Contar o número total de filmes
            cursor.execute("SELECT COUNT(*) FROM imagens")
            total_filmes = cursor.fetchone()[0]

            if total_filmes == 0:
                print("Nenhum filme cadastrado no banco de dados.")
                self.ui.movie_card.setPixmap(QPixmap())
                self.ui.movie_name.setText("Nenhum filme disponível")
                return

            # Gerar um número aleatório para o ID
            filme_id = random.randint(1, total_filmes)
            cursor.execute("SELECT nome, imagem_card FROM imagens WHERE id = %s", (filme_id,))
            filme = cursor.fetchone()

            if filme:
                nome, imagem_card_blob = filme
                imagem = QImage.fromData(imagem_card_blob)
                pixmap = QPixmap.fromImage(imagem).scaled(240, 320, Qt.KeepAspectRatio)
                self.ui.movie_card.setPixmap(pixmap)
                self.ui.movie_name.setText(nome)
                print(f"Filme recomendado: {nome}")
            else:
                self.ui.movie_card.setPixmap(QPixmap())
                self.ui.movie_name.setText("Filme não encontrado")

        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {str(e)}")
            self.ui.movie_card.setPixmap(QPixmap())
            self.ui.movie_name.setText("Erro ao carregar recomendação")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def voltar_para_tela_principal(self):
        from Tela_home import MainWindow as TelaMainWindow
        self.tela_principal = TelaMainWindow(email_usuario=self.email_usuario)
        self.tela_principal.show()
        self.close()

    def abrir_tela_filmes_series(self):
        from Tela_FilmeeSerie import MainWindow as FilmesSeriesMainWindow
        self.tela_filmes_series = FilmesSeriesMainWindow(email_usuario=self.email_usuario)
        self.tela_filmes_series.show()
        self.close()

    def sair(self):
        QApplication.quit()

    def editar_dados(self):
        dialog = EditUserDialog(self, self.email_usuario)
        dialog.exec()  # Abre o diálogo de forma modal

def main():
    app = QApplication(sys.argv)
    window = MainWindow(email_usuario="teste@example.com")  # Simulando um email para teste
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
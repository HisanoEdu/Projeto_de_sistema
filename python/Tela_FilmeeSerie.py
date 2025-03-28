# -*- coding: utf-8 -*-

import sys
import mysql.connector
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QFrame, QPushButton, QGridLayout, QScrollArea, QSizePolicy)
from PySide6.QtCore import Qt, QSize, QCoreApplication, QMetaObject
from PySide6.QtGui import QPixmap, QImage, QFont

# Configuração do banco de dados MySQL
banco = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'cadastrar_imagem'
}

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
        self.Btn_Inicio.setStyleSheet(u"color: red; border:none;")
        self.horizontalLayout.addWidget(self.Btn_Inicio)

        self.Btn_FileseSeries = QPushButton(self.Frame_Todo)
        self.Btn_FileseSeries.setObjectName(u"Btn_FileseSeries")
        self.Btn_FileseSeries.setMaximumSize(QSize(130, 16777215))
        self.Btn_FileseSeries.setStyleSheet(u"border:none; color: red;")
        self.horizontalLayout.addWidget(self.Btn_FileseSeries)

        self.Frame_Espaco1 = QFrame(self.Frame_Todo)
        self.Frame_Espaco1.setObjectName(u"Frame_Espaco1")
        self.Frame_Espaco1.setMaximumSize(QSize(20, 16777215))
        self.Frame_Espaco1.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco1)

        self.Btn_Recomendacao = QPushButton(self.Frame_Todo)
        self.Btn_Recomendacao.setObjectName(u"Btn_Recomendacao")
        self.Btn_Recomendacao.setMaximumSize(QSize(130, 16777215))
        self.Btn_Recomendacao.setStyleSheet(u"border: none; color: red;")
        self.horizontalLayout.addWidget(self.Btn_Recomendacao)

        self.Frame_Espaco2 = QFrame(self.Frame_Todo)
        self.Frame_Espaco2.setObjectName(u"Frame_Espaco2")
        self.Frame_Espaco2.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco2)

        self.Img_usuario = QLabel(self.Frame_Todo)
        self.Img_usuario.setObjectName(u"Img_usuario")
        self.Img_usuario.setMaximumSize(QSize(60, 16777215))
        self.Img_usuario.setPixmap(QPixmap(u"icon_perfil.png"))
        self.Img_usuario.setScaledContents(True)
        self.horizontalLayout.addWidget(self.Img_usuario)

        self.verticalLayout.addWidget(self.Frame_Todo)

        # Frame principal (corpo da tela)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: #000000;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.Frame_Espaco4 = QFrame(self.frame_2)
        self.Frame_Espaco4.setObjectName(u"Frame_Espaco4")
        self.Frame_Espaco4.setMaximumSize(QSize(16777215, 30))
        self.Frame_Espaco4.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2.addWidget(self.Frame_Espaco4)

        self.Frame_topo = QFrame(self.frame_2)
        self.Frame_topo.setObjectName(u"Frame_topo")
        self.Frame_topo.setMaximumSize(QSize(16777215, 50))
        self.Frame_topo.setFrameShape(QFrame.StyledPanel)
        self.Frame_topo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Frame_topo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.Frame_Espaco5 = QFrame(self.Frame_topo)
        self.Frame_Espaco5.setObjectName(u"Frame_Espaco5")
        self.Frame_Espaco5.setMinimumSize(QSize(65, 0))
        self.Frame_Espaco5.setMaximumSize(QSize(65, 16777215))
        self.Frame_Espaco5.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2.addWidget(self.Frame_Espaco5)

        self.verticalLayout_2.addWidget(self.Frame_topo)

        self.Frame_Main = QFrame(self.frame_2)
        self.Frame_Main.setObjectName(u"Frame_Main")
        self.Frame_Main.setFrameShape(QFrame.StyledPanel)
        self.Frame_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2.addWidget(self.Frame_Main)

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Filmes e Séries", None))
        self.txt_Logo.setText(QCoreApplication.translate("MainWindow", u"CineFilmes", None))
        self.Btn_Inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.Btn_FileseSeries.setText(QCoreApplication.translate("MainWindow", u"Filmes e Séries", None))
        self.Btn_Recomendacao.setText(QCoreApplication.translate("MainWindow", u"Recomenda\u00e7\u00e3o Aleatoria", None))
        self.Img_usuario.setText("")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configurar o grid de filmes e séries
        self.cards_widget = QWidget()
        self.cards_layout = QGridLayout(self.cards_widget)
        self.cards_layout.setHorizontalSpacing(20)
        self.cards_layout.setVerticalSpacing(20)
        self.cards_layout.setContentsMargins(20, 20, 20, 20)

        # Adicionar scroll ao Frame_Main
        scroll = QScrollArea()
        scroll.setWidget(self.cards_widget)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        main_layout = QVBoxLayout(self.ui.Frame_Main)
        main_layout.addWidget(scroll)

        # Carregar e exibir filmes e séries
        self.carregar_filmes_series()

        # Conectar botões de navegação
        self.ui.Btn_Inicio.clicked.connect(self.voltar_para_tela_principal)
        self.ui.Btn_Recomendacao.clicked.connect(self.abrir_tela_aleatoria)

    def carregar_filmes_series(self):
        try:
            conn = mysql.connector.connect(**banco)
            cursor = conn.cursor()
            cursor.execute("SELECT nome, imagem_card, descricao FROM imagens")
            self.filmes_series = cursor.fetchall()
            self.exibir_filmes_series()
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def exibir_filmes_series(self):
        # Limpar o layout anterior
        for i in reversed(range(self.cards_layout.count())):
            self.cards_layout.itemAt(i).widget().setParent(None)

        # Configurar fontes
        font_nome = QFont("Segoe UI", 12, QFont.Bold)
        font_desc = QFont("Segoe UI", 10)

        # Exibir filmes e séries em um grid de 2 colunas
        for idx, (nome, imagem_card_blob, descricao) in enumerate(self.filmes_series):
            row = idx  # Cada filme/série ocupa uma linha

            # Frame do card (esquerda)
            card_frame = QFrame()
            card_frame.setStyleSheet("background: transparent;")
            card_layout = QVBoxLayout(card_frame)
            card_layout.setSpacing(5)
            card_layout.setContentsMargins(0, 0, 0, 0)

            # Imagem do card
            imagem = QImage.fromData(imagem_card_blob)
            pixmap = QPixmap.fromImage(imagem).scaled(120, 160, Qt.KeepAspectRatio)
            imagem_label = QLabel()
            imagem_label.setPixmap(pixmap)
            imagem_label.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(imagem_label)

            # Nome do filme/série
            nome_label = QLabel(nome)
            nome_label.setFont(font_nome)
            nome_label.setStyleSheet("color: white;")
            nome_label.setAlignment(Qt.AlignCenter)
            nome_label.setWordWrap(True)
            card_layout.addWidget(nome_label)

            # Descrição (direita)
            desc_label = QLabel(descricao if descricao else "Descrição não disponível")
            desc_label.setFont(font_desc)
            desc_label.setStyleSheet("color: white;")
            desc_label.setWordWrap(True)
            desc_label.setMaximumWidth(800)  # Limite de largura para a descrição
            desc_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            # Adicionar ao grid (2 colunas: card à esquerda, descrição à direita)
            self.cards_layout.addWidget(card_frame, row, 0, alignment=Qt.AlignTop | Qt.AlignLeft)
            self.cards_layout.addWidget(desc_label, row, 1, alignment=Qt.AlignTop | Qt.AlignLeft)

        self.cards_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    def voltar_para_tela_principal(self):
        from Tela_home import MainWindow as TelaMainWindow
        self.tela_principal = TelaMainWindow()
        self.tela_principal.show()
        self.close()

    def abrir_tela_aleatoria(self):
        from Tela_Aleatorio import MainWindow as AleatoriaMainWindow
        self.tela_aleatoria = AleatoriaMainWindow()
        self.tela_aleatoria.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
import sys         # Tela_Principal
import mysql.connector
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QFrame, QScrollArea, QMessageBox, QGridLayout, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem)
from PySide6.QtCore import Qt, QSize, QCoreApplication, QMetaObject
from PySide6.QtGui import QPixmap, QImage, QFont

from Tela_Banner import BannerWindow  # Importar apenas a classe BannerWindow

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
        MainWindow.resize(1100, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.Frame_Todo = QFrame(self.centralwidget)
        self.Frame_Todo.setObjectName(u"Frame_Todo")
        self.Frame_Todo.setMaximumSize(QSize(16777215, 60))
        self.Frame_Todo.setStyleSheet(u"background: #221F1F;")
        self.Frame_Todo.setFrameShape(QFrame.StyledPanel)
        self.Frame_Todo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_Todo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(5)

        self.txt_Logo = QLabel(self.Frame_Todo)
        self.txt_Logo.setObjectName(u"txt_Logo")
        self.txt_Logo.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(True)
        self.txt_Logo.setFont(font)
        self.txt_Logo.setStyleSheet(u"color: red;")
        self.horizontalLayout.addWidget(self.txt_Logo)

        self.Btn_Inicio = QPushButton(self.Frame_Todo)
        self.Btn_Inicio.setObjectName(u"Btn_Inicio")
        self.Btn_Inicio.setMinimumSize(QSize(100, 30))
        self.Btn_Inicio.setStyleSheet(u"color: red; border: none; background: transparent; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_Inicio)

        self.Btn_FileseSeries = QPushButton(self.Frame_Todo)
        self.Btn_FileseSeries.setObjectName(u"Btn_FileseSeries")
        self.Btn_FileseSeries.setMinimumSize(QSize(100, 30))
        self.Btn_FileseSeries.setStyleSheet(u"color: red; border: none; background: transparent; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_FileseSeries)

        self.Btn_Recomendacao = QPushButton(self.Frame_Todo)
        self.Btn_Recomendacao.setObjectName(u"Btn_Recomendacao")
        self.Btn_Recomendacao.setMinimumSize(QSize(100, 30))
        self.Btn_Recomendacao.setStyleSheet(u"color: red; border: none; background: transparent; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_Recomendacao)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Img_usuario = QLabel(self.Frame_Todo)
        self.Img_usuario.setObjectName(u"Img_usuario")
        self.Img_usuario.setFixedSize(QSize(40, 40))
        self.Img_usuario.setPixmap(QPixmap(u"../../Downloads/icon_perfil.png"))
        self.Img_usuario.setScaledContents(True)
        self.Img_usuario.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.Img_usuario)

        self.verticalLayout.addWidget(self.Frame_Todo)

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
        self.Frame_Espaco4.setFixedHeight(40)
        self.Frame_Espaco4.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2.addWidget(self.Frame_Espaco4)

        self.Frame_topo = QFrame(self.frame_2)
        self.Frame_topo.setObjectName(u"Frame_topo")
        self.Frame_topo.setMaximumSize(QSize(16777215, 40))
        self.Frame_topo.setFrameShape(QFrame.StyledPanel)
        self.Frame_topo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Frame_topo)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)

        self.Frame_Espaco5 = QFrame(self.Frame_topo)
        self.Frame_Espaco5.setObjectName(u"Frame_Espaco5")
        self.Frame_Espaco5.setMinimumSize(QSize(30, 0))
        self.Frame_Espaco5.setMaximumSize(QSize(30, 16777215))
        self.horizontalLayout_2.addWidget(self.Frame_Espaco5)

        self.txt_Filmes = QLabel(self.Frame_topo)
        self.txt_Filmes.setObjectName(u"txt_Filmes")
        self.txt_Filmes.setStyleSheet(u"color:red;")
        self.horizontalLayout_2.addWidget(self.txt_Filmes)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.Input_Pesquisa = QLineEdit(self.Frame_topo)
        self.Input_Pesquisa.setObjectName(u"Input_Pesquisa")
        self.Input_Pesquisa.setMaximumSize(QSize(300, 20))
        self.Input_Pesquisa.setStyleSheet(u"border: 1px solid red; background: white; border-radius: 5px")
        self.horizontalLayout_2.addWidget(self.Input_Pesquisa)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_Logo.setText(QCoreApplication.translate("MainWindow", u"CineFilmes", None))
        self.Btn_Inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.Btn_FileseSeries.setText(QCoreApplication.translate("MainWindow", u"Filmes e Series", None))
        self.Btn_Recomendacao.setText(QCoreApplication.translate("MainWindow", u"Recomenda\u00e7\u00e3o Aleatoria", None))
        self.Img_usuario.setText("")
        self.txt_Filmes.setText(QCoreApplication.translate("MainWindow", u"Filmes", None))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(QSize(1000, 500))

        self.cards_widget = QWidget()
        self.cards_layout = QGridLayout(self.cards_widget)
        self.cards_layout.setHorizontalSpacing(10)
        self.cards_layout.setVerticalSpacing(10)
        self.cards_layout.setContentsMargins(20, 20, 20, 20)

        scroll = QScrollArea()
        scroll.setWidget(self.cards_widget)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        main_layout = QVBoxLayout(self.ui.Frame_Main)
        main_layout.addWidget(scroll)

        self.imagens = []
        self.carregar_todas_imagens()

        self.ui.Input_Pesquisa.textChanged.connect(self.filtrar_imagens)
        self.showEvent = self.on_show_event
        # Conectar o botão "Recomendação Aleatória" à função de abrir Tela_Aleatoria.py
        self.ui.Btn_Recomendacao.clicked.connect(self.abrir_tela_aleatoria)
        # Conectar o botão "Filmes e Séries" à função de abrir Tela_FilmesSeries.py
        self.ui.Btn_FileseSeries.clicked.connect(self.abrir_tela_filmes_series)

    def on_show_event(self, event):
        self.exibir_imagens(self.imagens)
        super().showEvent(event)

    def carregar_todas_imagens(self):
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**banco)
            cursor = conn.cursor()
            cursor.execute("SELECT nome, imagem_card, imagem_banner, descricao, video_id FROM imagens")
            self.imagens = cursor.fetchall()
            print("Dados carregados do banco de dados:")
            for nome, _, _, descricao, video_id in self.imagens:
                print(f"Nome: {nome}, Descrição: {descricao}, Video_id: {video_id}")
            self.exibir_imagens(self.imagens)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao conectar ao banco de dados: {str(e)}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def exibir_imagens(self, imagens):
        for i in reversed(range(self.cards_layout.count())):
            self.cards_layout.itemAt(i).widget().setParent(None)

        card_width = 120
        spacing = 10
        frame_width = self.ui.Frame_Main.width() - 40
        num_cols = (frame_width + spacing) // (card_width + spacing)
        if num_cols < 3:
            num_cols = 3

        for idx, (nome, imagem_card_blob, imagem_banner_blob, descricao, video_id) in enumerate(imagens):
            row = idx // num_cols
            col = idx % num_cols

            card = QFrame()
            card.setStyleSheet("background: transparent;")
            card.setFixedSize(120, 200)
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(0, 0, 0, 0)
            card_layout.setSpacing(5)

            imagem = QImage.fromData(imagem_card_blob)
            pixmap = QPixmap.fromImage(imagem).scaled(120, 160, Qt.KeepAspectRatio)
            imagem_label = QLabel()
            imagem_label.setPixmap(pixmap)
            imagem_label.setAlignment(Qt.AlignCenter)
            imagem_label.setCursor(Qt.PointingHandCursor)
            imagem_label.mouseDoubleClickEvent = lambda event, n=nome, img=imagem_banner_blob, desc=descricao, vid=video_id: self.open_banner_dialog(n, img, desc, vid)
            card_layout.addWidget(imagem_label)

            nome_label = QLabel(nome)
            nome_label.setStyleSheet("color: white; font-size: 12px;")
            nome_label.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(nome_label)

            self.cards_layout.addWidget(card, row, col, alignment=Qt.AlignTop | Qt.AlignLeft)

        self.cards_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    def open_banner_dialog(self, nome, imagem_banner_blob, descricao, video_id):
        print(f"Abrindo banner - Nome: {nome}, Descrição: {descricao}, Video: {video_id}")
        self.banner_window = BannerWindow(nome=nome, imagem_banner_blob=imagem_banner_blob, descricao=descricao, video_id=video_id)
        self.banner_window.show()
        self.close()

    def filtrar_imagens(self):
        texto_pesquisa = self.ui.Input_Pesquisa.text().strip().lower()
        if texto_pesquisa == "":
            self.exibir_imagens(self.imagens)
        else:
            imagens_filtradas = []
            for nome, imagem_card_blob, imagem_banner_blob, descricao, video_id in self.imagens:
                if texto_pesquisa in nome.lower():
                    imagens_filtradas.append((nome, imagem_card_blob, imagem_banner_blob, descricao, video_id))
            self.exibir_imagens(imagens_filtradas)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.filtrar_imagens()

    def abrir_tela_aleatoria(self):
        from Tela_Aleatorio import MainWindow as AleatoriaMainWindow
        self.tela_aleatoria = AleatoriaMainWindow()
        self.tela_aleatoria.show()
        self.close()

    def abrir_tela_filmes_series(self):
        from Tela_FilmeeSerie import MainWindow as FilmesSeriesMainWindow
        self.tela_filmes_series = FilmesSeriesMainWindow()
        self.tela_filmes_series.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
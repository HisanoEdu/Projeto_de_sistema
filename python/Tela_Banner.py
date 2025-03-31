# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QFont, QLinearGradient, QPalette, QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget)
from Trailer import YoutubeTrailer  # Certifique-se de que o nome do import está correto

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet("background: transparent;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.Frame_Todo = QFrame(self.centralwidget)
        self.Frame_Todo.setObjectName(u"Frame_Todo")
        self.Frame_Todo.setMaximumSize(QSize(16777215, 80))
        self.Frame_Todo.setStyleSheet(u"background: rgba(0, 0, 0, 150);")
        self.Frame_Todo.setFrameShape(QFrame.StyledPanel)
        self.Frame_Todo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_Todo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.Frame_Espaco3 = QFrame(self.Frame_Todo)
        self.Frame_Espaco3.setObjectName(u"Frame_Espaco3")
        self.Frame_Espaco3.setMaximumSize(QSize(50, 100))
        self.Frame_Espaco3.setStyleSheet(u"background: transparent;")
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
        self.txt_Logo.setStyleSheet(u"color: red; background: transparent;")
        self.horizontalLayout.addWidget(self.txt_Logo)

        self.Btn_Inicio = QPushButton(self.Frame_Todo)
        self.Btn_Inicio.setObjectName(u"Btn_Inicio")
        self.Btn_Inicio.setMaximumSize(QSize(130, 16777215))
        self.Btn_Inicio.setStyleSheet(u"color: red; border: none; background: transparent;")
        self.horizontalLayout.addWidget(self.Btn_Inicio)

        self.Btn_FileseSeries = QPushButton(self.Frame_Todo)
        self.Btn_FileseSeries.setObjectName(u"Btn_FileseSeries")
        self.Btn_FileseSeries.setMaximumSize(QSize(130, 16777215))
        self.Btn_FileseSeries.setStyleSheet(u"border: none; color: red; background: transparent;")
        self.horizontalLayout.addWidget(self.Btn_FileseSeries)

        self.Frame_Espaco1 = QFrame(self.Frame_Todo)
        self.Frame_Espaco1.setObjectName(u"Frame_Espaco1")
        self.Frame_Espaco1.setMaximumSize(QSize(20, 16777215))
        self.Frame_Espaco1.setStyleSheet(u"background: transparent;")
        self.Frame_Espaco1.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco1)

        self.Btn_Recomendacao = QPushButton(self.Frame_Todo)
        self.Btn_Recomendacao.setObjectName(u"Btn_Recomendacao")
        self.Btn_Recomendacao.setMaximumSize(QSize(130, 16777215))
        self.Btn_Recomendacao.setStyleSheet(u"border: none; color: red; background: transparent;")
        self.horizontalLayout.addWidget(self.Btn_Recomendacao)

        self.Frame_Espaco2 = QFrame(self.Frame_Todo)
        self.Frame_Espaco2.setObjectName(u"Frame_Espaco2")
        self.Frame_Espaco2.setStyleSheet(u"background: transparent;")
        self.Frame_Espaco2.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco2)

        self.Img_usuario = QLabel(self.Frame_Todo)
        self.Img_usuario.setObjectName(u"Img_usuario")
        self.Img_usuario.setMaximumSize(QSize(60, 16777215))
        self.Img_usuario.setPixmap(QPixmap(u"icon_perfil.png"))
        self.Img_usuario.setScaledContents(True)
        self.Img_usuario.setStyleSheet(u"background: transparent;")
        self.horizontalLayout.addWidget(self.Img_usuario)

        self.verticalLayout.addWidget(self.Frame_Todo)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: transparent;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.Frame_Descricao = QFrame(self.frame_2)
        self.Frame_Descricao.setObjectName(u"Frame_Descricao")
        self.Frame_Descricao.setMaximumSize(QSize(300, 16777215))
        self.Frame_Descricao.setStyleSheet(u"background: rgba(0, 0, 0, 100);")
        self.Frame_Descricao.setFrameShape(QFrame.StyledPanel)
        self.Frame_Descricao.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_Descricao = QVBoxLayout(self.Frame_Descricao)
        self.verticalLayout_Descricao.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        self.txt_Descricao = QLabel(self.Frame_Descricao)
        self.txt_Descricao.setObjectName(u"txt_Descricao")
        self.txt_Descricao.setWordWrap(True)
        font_desc = QFont()
        font_desc.setFamilies([u"Segoe UI"])
        font_desc.setPointSize(12)
        self.txt_Descricao.setFont(font_desc)
        self.txt_Descricao.setStyleSheet(u"color: white; background: transparent; padding: 20px 10px 20px 20px;")
        self.txt_Descricao.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.verticalLayout_Descricao.addWidget(self.txt_Descricao)
        
        self.Btn_VerTrailer = QPushButton(self.Frame_Descricao)
        self.Btn_VerTrailer.setObjectName(u"Btn_VerTrailer")
        self.Btn_VerTrailer.setMaximumSize(QSize(130, 40))
        self.Btn_VerTrailer.setFont(font_desc)
        self.Btn_VerTrailer.setStyleSheet(u"color: white; background: red; border: 1px solid red; border-radius: 5px; padding: 5px;")
        self.verticalLayout_Descricao.addWidget(self.Btn_VerTrailer, alignment=Qt.AlignCenter)
        
        self.horizontalLayout_2.addWidget(self.Frame_Descricao)

        self.Frame_Main = QFrame(self.frame_2)
        self.Frame_Main.setObjectName(u"Frame_Main")
        self.Frame_Main.setStyleSheet(u"background: transparent;")
        self.Frame_Main.setFrameShape(QFrame.StyledPanel)
        self.Frame_Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2.addWidget(self.Frame_Main)

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
        self.txt_Descricao.setText(QCoreApplication.translate("MainWindow", u"Descrição do filme ou série será carregada aqui", None))
        self.Btn_VerTrailer.setText(QCoreApplication.translate("MainWindow", u"Ver Trailer", None))

class BannerWindow(QMainWindow):
    def __init__(self, nome=None, imagem_banner_blob=None, descricao=None, video_id=None, parent=None):
        super().__init__(parent)
        self.nome = nome
        self.imagem_banner_blob = imagem_banner_blob
        self.descricao = descricao
        self.video_id = video_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setFixedSize(1071, 648)
        self.apply_background_and_gradient()

        self.trailer_window = None
        
        # Conectar o botão "Ver Trailer" ao método abrir_trailer
        self.ui.Btn_VerTrailer.clicked.connect(self.abrir_trailer)
        # Conectar o botão "Início" ao método voltar_para_tela_filmes
        self.ui.Btn_Inicio.clicked.connect(self.voltar_para_tela_filmes)
        # Conectar o botão "Recomendação Aleatória" ao método abrir_tela_aleatoria
        self.ui.Btn_Recomendacao.clicked.connect(self.abrir_tela_aleatoria)
        # Conectar o botão "Filmes e Séries" ao método abrir_tela_filmes_series
        self.ui.Btn_FileseSeries.clicked.connect(self.abrir_tela_filmes_series)

        print(f"Configurando BannerWindow - Nome: {nome}, Descrição recebida: {descricao}, Video ID: {video_id}")
        if self.descricao and self.descricao.strip():
            self.ui.txt_Descricao.setText(self.descricao)
        else:
            self.ui.txt_Descricao.setText("Descrição não disponível")

    def abrir_trailer(self):
        try:
            if not self.video_id:
                print("Nenhum video_id fornecido para este banner.")
                return
            if self.trailer_window is None or not self.trailer_window.isVisible():
                self.trailer_window = YoutubeTrailer(self.video_id)
                self.trailer_window.show()
            else:
                self.trailer_window.raise_()
        except Exception as e:
            print(f"Erro ao abrir o trailer: {e}")

    def voltar_para_tela_filmes(self):
        # Importar MainWindow aqui para evitar importação circular
        from Tela_home import MainWindow as FilmesMainWindow
        # Criar uma nova instância da tela dos filmes
        self.filmes_window = FilmesMainWindow()
        self.filmes_window.show()
        # Fechar a janela atual do banner
        self.close()

    def abrir_tela_aleatoria(self):
        # Importar MainWindow de Tela_Aleatoria.py dinamicamente
        from Tela_Aleatorio import MainWindow as AleatoriaMainWindow
        # Criar uma nova instância da tela de recomendação aleatória
        self.tela_aleatoria = AleatoriaMainWindow()
        self.tela_aleatoria.show()
        # Fechar a tela atual
        self.close()

    def abrir_tela_filmes_series(self):
        # Importar MainWindow de Tela_FilmesSeries.py dinamicamente
        from Tela_FilmeeSerie import MainWindow as FilmesSeriesMainWindow
        # Criar uma nova instância da tela de filmes e séries
        self.tela_filmes_series = FilmesSeriesMainWindow()
        self.tela_filmes_series.show()
        # Fechar a tela atual
        self.close()

    def apply_background_and_gradient(self):
        if self.imagem_banner_blob:
            try:
                pixmap = QPixmap()
                if not pixmap.loadFromData(self.imagem_banner_blob):
                    print("Erro: Não foi possível carregar a imagem do blob.")
                    self.setStyleSheet("background: darkgray;")
                    return
                
                scaled_pixmap = pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                palette = QPalette()
                palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
                self.setPalette(palette)
                self.setAutoFillBackground(True)
            except Exception as e:
                print(f"Erro ao aplicar o banner como fundo: {e}")
                self.setStyleSheet("background: darkgray;")
        else:
            print("Nenhum banner fornecido, usando fundo padrão.")
            self.setStyleSheet("background: darkgray;")

        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0.0, QColor(20, 20, 20, 255))
        gradient.setColorAt(1.0, QColor(100, 100, 100, 0))

        self.gradient_widget = QWidget(self)
        self.gradient_widget.setGeometry(0, 0, self.width(), self.height())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.gradient_widget.setPalette(palette)
        self.gradient_widget.setAutoFillBackground(True)
        self.gradient_widget.lower()

        self.ui.centralwidget.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.Frame_Todo.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.frame_2.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.Frame_Main.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.Frame_Descricao.setAttribute(Qt.WA_TranslucentBackground)

    def resizeEvent(self, event):
        self.apply_background_and_gradient()
        super().resizeEvent(event)
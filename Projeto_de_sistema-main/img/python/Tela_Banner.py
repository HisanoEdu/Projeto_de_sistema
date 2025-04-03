from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QFont, QLinearGradient, QPalette, QPixmap)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget, QMessageBox, QDialog, QFormLayout, QLineEdit)
import mysql.connector

from Trailer import YoutubeTrailer  # Certifique-se de que o nome do import está correto

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
            conn = mysql.connector.connect(**banco)
            cursor = conn.cursor()
            cursor.execute("SELECT nome, email, senha FROM usuarios WHERE email = %s", (self.email_usuario,))
            resultado = cursor.fetchone()
            if resultado:
                nome, email, senha = resultado
                self.nome_input.setText(nome)
                self.email_input.setText(email)
                self.senha_input.setText(senha)
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
        self.horizontalLayout.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout.setSpacing(10)
        
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
        self.Frame_Espaco1.setStyleSheet(u"background: transparent;")
        self.Frame_Espaco1.setFrameShape(QFrame.StyledPanel)
        self.Frame_Espaco1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.Frame_Espaco1)

        self.Btn_Recomendacao = QPushButton(self.Frame_Todo)
        self.Btn_Recomendacao.setObjectName(u"Btn_Recomendacao")
        self.Btn_Recomendacao.setMaximumSize(QSize(200, 16777215))
        self.Btn_Recomendacao.setStyleSheet(u"border: none; color: red; background: transparent; padding: 5px;")
        self.horizontalLayout.addWidget(self.Btn_Recomendacao)

        self.Frame_Espaco2 = QFrame(self.Frame_Todo)
        self.Frame_Espaco2.setObjectName(u"Frame_Espaco2")
        self.Frame_Espaco2.setStyleSheet(u"background: transparent;")
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
        self.Btn_Sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.Btn_Editar_Dados.setText(QCoreApplication.translate("MainWindow", u"Editar Dados", None))
        self.txt_Descricao.setText(QCoreApplication.translate("MainWindow", u"Descrição do filme ou série será carregada aqui", None))
        self.Btn_VerTrailer.setText(QCoreApplication.translate("MainWindow", u"Ver Trailer", None))

class BannerWindow(QMainWindow):
    def __init__(self, nome=None, imagem_banner_blob=None, descricao=None, video_id=None, email_usuario=None, parent=None):
        super().__init__(parent)
        self.nome = nome
        self.imagem_banner_blob = imagem_banner_blob
        self.descricao = descricao
        self.video_id = video_id
        self.email_usuario = email_usuario  # Armazenar o email do usuário logado
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setFixedSize(1071, 648)
        self.apply_background_and_gradient()

        self.trailer_window = None
        
        # Conectar os botões
        self.ui.Btn_VerTrailer.clicked.connect(self.abrir_trailer)
        self.ui.Btn_Inicio.clicked.connect(self.voltar_para_tela_filmes)
        self.ui.Btn_Recomendacao.clicked.connect(self.abrir_tela_aleatoria)
        self.ui.Btn_FileseSeries.clicked.connect(self.abrir_tela_filmes_series)
        self.ui.Btn_Sair.clicked.connect(self.sair)
        self.ui.Btn_Editar_Dados.clicked.connect(self.editar_dados)

        print(f"Configurando BannerWindow - Nome: {nome}, Descrição recebida: {descricao}, Video ID: {video_id}, Email: {email_usuario}")
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
        try:
            from Tela_home import MainWindow as FilmesMainWindow
            self.filmes_window = FilmesMainWindow(email_usuario=self.email_usuario)
            self.filmes_window.show()
            self.close()
        except ImportError as e:
            print(f"Erro ao importar Tela_home: {e}")
            QMessageBox.critical(self, "Erro", "Não foi possível abrir a tela inicial. Verifique o arquivo Tela_home.py.")

    def abrir_tela_aleatoria(self):
        try:
            from Tela_Aleatorio import MainWindow as AleatoriaMainWindow
            self.tela_aleatoria = AleatoriaMainWindow()
            self.tela_aleatoria.show()
            self.close()
        except ImportError as e:
            print(f"Erro ao importar Tela_Aleatorio: {e}")
            QMessageBox.critical(self, "Erro", "Não foi possível abrir a tela de recomendação aleatória.")

    def abrir_tela_filmes_series(self):
        try:
            from Tela_FilmeeSerie import MainWindow as FilmesSeriesMainWindow
            self.tela_filmes_series = FilmesSeriesMainWindow(email_usuario=self.email_usuario)
            self.tela_filmes_series.show()
            self.close()
        except ImportError as e:
            print(f"Erro ao importar Tela_FilmeeSerie: {e}")
            QMessageBox.critical(self, "Erro", "Não foi possível abrir a tela de filmes e séries.")

    def sair(self):
        QApplication.quit()

    def editar_dados(self):
        dialog = EditUserDialog(self, self.email_usuario)
        dialog.exec()  # Abre o diálogo de forma modal

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

def main():
    import sys
    app = QApplication(sys.argv)
    window = BannerWindow(nome="Teste", descricao="Descrição de teste", video_id="dQw4w9WgXcQ", email_usuario="teste@example.com")
    window.show()
    sys.exit(app.exec())
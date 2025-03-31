import sys
import mysql.connector
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt, QCoreApplication, QMetaObject
from PySide6.QtGui import QFont

# Configuração do banco de dados MySQL
banco = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',  # Ajuste conforme necessário
    'database': 'cinefilmes_db'
}

# Função para conectar ao MySQL
def conectar():
    try:
        conexao = mysql.connector.connect(**banco)
        print("Conexão bem-sucedida!")
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        return None

# Função para criar o banco de dados
def criar_banco():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=""
        )
        cursor = conexao.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS cinefilmes_db")
        print("Banco de dados 'cinefilmes_db' criado com sucesso ou já existe.")
        conexao.close()
    except mysql.connector.Error as err:
        print(f"Erro ao criar o banco de dados: {err}")

# Função para criar as tabelas
def criar_tabelas():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            # Tabela de usuários com tipo_usuario
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    senha VARCHAR(255),
                    tipo_usuario ENUM('usuario', 'admin') DEFAULT 'usuario'
                )
            """)
            # Tabela de imagens
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS imagens (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    descricao TEXT,
                    video_id VARCHAR(255),
                    imagem_card LONGBLOB NOT NULL,
                    imagem_banner LONGBLOB NOT NULL
                )
            """)
            conexao.commit()
            print("Tabelas criadas com sucesso ou já existem.")
        except mysql.connector.Error as err:
            print(f"Erro ao criar tabelas: {err}")
        finally:
            conexao.close()

# Função para converter imagem em blob
def converter_imagem_para_blob(caminho_imagem):
    with open(caminho_imagem, 'rb') as arquivo:
        blob = arquivo.read()
    return blob

# Classe da janela de cadastro de imagens
class Ui_CadastroImagem(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 500)
        MainWindow.setStyleSheet("background: #1E1E1E;")  # Fundo escuro

        # Widget central e layout
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layout = QVBoxLayout(self.centralwidget)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)

        # Título
        self.titulo = QLabel("Cadastro de Filmes", self.centralwidget)
        font_titulo = QFont("Segoe UI", 20, QFont.Bold)
        self.titulo.setFont(font_titulo)
        self.titulo.setStyleSheet("color: #FF0000;")  # Vermelho
        self.titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.titulo)

        # Campo Nome
        self.label_nome = QLabel("Nome:", self.centralwidget)
        self.label_nome.setStyleSheet("color: #FFFFFF; font: 12pt 'Segoe UI';")
        self.nome_input = QLineEdit(self.centralwidget)
        self.nome_input.setPlaceholderText("Nome do filme")
        self.nome_input.setStyleSheet("""
            QLineEdit {
                background: #2A2A2A;
                color: #FFFFFF;
                border: 1px solid #FF0000;
                border-radius: 5px;
                padding: 8px;
                font: 12pt 'Segoe UI';
            }
            QLineEdit:focus {
                border: 2px solid #FF5555;
            }
        """)
        self.layout.addWidget(self.label_nome)
        self.layout.addWidget(self.nome_input)

        # Campo Descrição
        self.label_descricao = QLabel("Descrição:", self.centralwidget)
        self.label_descricao.setStyleSheet("color: #FFFFFF; font: 12pt 'Segoe UI';")
        self.descricao_input = QLineEdit(self.centralwidget)
        self.descricao_input.setPlaceholderText("Descrição")
        self.descricao_input.setStyleSheet("""
            QLineEdit {
                background: #2A2A2A;
                color: #FFFFFF;
                border: 1px solid #FF0000;
                border-radius: 5px;
                padding: 8px;
                font: 12pt 'Segoe UI';
            }
            QLineEdit:focus {
                border: 2px solid #FF5555;
            }
        """)
        self.layout.addWidget(self.label_descricao)
        self.layout.addWidget(self.descricao_input)

        # Campo Video ID
        self.label_video = QLabel("ID do Vídeo (YouTube):", self.centralwidget)
        self.label_video.setStyleSheet("color: #FFFFFF; font: 12pt 'Segoe UI';")
        self.tela_input = QLineEdit(self.centralwidget)
        self.tela_input.setPlaceholderText("ID do vídeo do YouTube")
        self.tela_input.setStyleSheet("""
            QLineEdit {
                background: #2A2A2A;
                color: #FFFFFF;
                border: 1px solid #FF0000;
                border-radius: 5px;
                padding: 8px;
                font: 12pt 'Segoe UI';
            }
            QLineEdit:focus {
                border: 2px solid #FF5555;
            }
        """)
        self.layout.addWidget(self.label_video)
        self.layout.addWidget(self.tela_input)

        # Botão Selecionar Imagem Card
        self.btn_selecionar_card = QPushButton("Selecionar Imagem do Card", self.centralwidget)
        self.btn_selecionar_card.setStyleSheet("""
            QPushButton {
                background: #FF0000;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font: 12pt 'Segoe UI';
            }
            QPushButton:hover {
                background: #FF5555;
            }
        """)
        self.btn_selecionar_card.clicked.connect(self.selecionar_imagem_card)
        self.layout.addWidget(self.btn_selecionar_card)

        # Label para imagem do card
        self.imagem_card_label = QLabel("Nenhuma imagem de card selecionada", self.centralwidget)
        self.imagem_card_label.setStyleSheet("color: #AAAAAA; font: 10pt 'Segoe UI';")
        self.layout.addWidget(self.imagem_card_label)

        # Botão Selecionar Imagem Banner
        self.btn_selecionar_banner = QPushButton("Selecionar Imagem do Banner", self.centralwidget)
        self.btn_selecionar_banner.setStyleSheet("""
            QPushButton {
                background: #FF0000;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font: 12pt 'Segoe UI';
            }
            QPushButton:hover {
                background: #FF5555;
            }
        """)
        self.btn_selecionar_banner.clicked.connect(self.selecionar_imagem_banner)
        self.layout.addWidget(self.btn_selecionar_banner)

        # Label para imagem do banner
        self.imagem_banner_label = QLabel("Nenhuma imagem de banner selecionada", self.centralwidget)
        self.imagem_banner_label.setStyleSheet("color: #AAAAAA; font: 10pt 'Segoe UI';")
        self.layout.addWidget(self.imagem_banner_label)

        # Botão Cadastrar
        self.btn_cadastrar = QPushButton("Cadastrar", self.centralwidget)
        self.btn_cadastrar.setStyleSheet("""
            QPushButton {
                background: #FF0000;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font: 12pt 'Segoe UI';
            }
            QPushButton:hover {
                background: #FF5555;
            }
        """)
        self.btn_cadastrar.clicked.connect(self.cadastrar_imagem)
        self.layout.addWidget(self.btn_cadastrar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Variáveis para armazenar os caminhos das imagens
        self.caminho_imagem_card = None
        self.caminho_imagem_banner = None

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Cadastro de Imagens", None))

    def selecionar_imagem_card(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self.centralwidget, "Selecionar Imagem do Card", "",
            "Imagens (*.png *.jpg *.jpeg *.bmp)"
        )
        if caminho:
            self.caminho_imagem_card = caminho
            self.imagem_card_label.setText(f"Card: {caminho.split('/')[-1]}")

    def selecionar_imagem_banner(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self.centralwidget, "Selecionar Imagem do Banner", "",
            "Imagens (*.png *.jpg *.jpeg *.bmp)"
        )
        if caminho:
            self.caminho_imagem_banner = caminho
            self.imagem_banner_label.setText(f"Banner: {caminho.split('/')[-1]}")

    def cadastrar_imagem(self):
        nome = self.nome_input.text()
        descricao = self.descricao_input.text()
        video_id = self.tela_input.text()

        if not nome or not self.caminho_imagem_card or not self.caminho_imagem_banner:
            QMessageBox.warning(self.centralwidget, "Erro", "Nome, imagem do card e imagem do banner são obrigatórios!")
            return

        try:
            imagem_card_blob = converter_imagem_para_blob(self.caminho_imagem_card)
            imagem_banner_blob = converter_imagem_para_blob(self.caminho_imagem_banner)
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO imagens (nome, descricao, video_id, imagem_card, imagem_banner)
                VALUES (%s, %s, %s, %s, %s)
            """, (nome, descricao, video_id, imagem_card_blob, imagem_banner_blob))
            conn.commit()
            QMessageBox.information(self.centralwidget, "Sucesso", "Imagens cadastradas com sucesso!")
            self.limpar_campos()
        except mysql.connector.Error as e:
            QMessageBox.critical(self.centralwidget, "Erro", f"Erro ao cadastrar: {e}")
        finally:
            cursor.close()
            conn.close()

    def limpar_campos(self):
        self.nome_input.clear()
        self.descricao_input.clear()
        self.tela_input.clear()
        self.imagem_card_label.setText("Nenhuma imagem de card selecionada")
        self.imagem_banner_label.setText("Nenhuma imagem de banner selecionada")
        self.caminho_imagem_card = None
        self.caminho_imagem_banner = None

class CadastroImagem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastroImagem()
        self.ui.setupUi(self)

# Função principal
def main():
    criar_banco()
    criar_tabelas()
    app = QApplication(sys.argv)
    janela = CadastroImagem()
    janela.show()
    sys.exit(app.exec())
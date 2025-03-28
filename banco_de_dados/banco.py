import sys
import mysql.connector
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt

# Configuração do banco de dados MySQL
banco = {
    'host': '127.0.0.1',
    'user': 'root',  # Substitua pelo seu usuário do MySQL
    'password': '',  # Substitua pela sua senha do MySQL
    'database': 'cadastrar_imagem'  # Nome do banco de dados
}

# Função para criar a tabela no banco de dados MySQL
def criar_tabela():
    try:
        conn = mysql.connector.connect(**banco)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS imagens (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                descricao TEXT,
                video_id VARCHAR(255),
                imagem_card LONGBLOB NOT NULL,
                imagem_banner LONGBLOB NOT NULL
            )
        ''')
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()
        conn.close()

# Função para converter imagem em blob
def converter_imagem_para_blob(caminho_imagem):
    with open(caminho_imagem, 'rb') as arquivo:
        blob = arquivo.read()
    return blob

# Classe da janela principal
class CadastroImagem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Imagens")
        self.setGeometry(100, 100, 400, 400)

        # Widget central e layout
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Campos de entrada
        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Nome do filme")
        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.nome_input)

        self.descricao_input = QLineEdit(self)
        self.descricao_input.setPlaceholderText("Descrição")
        layout.addWidget(QLabel("Descrição:"))
        layout.addWidget(self.descricao_input)

        self.tela_input = QLineEdit(self)
        self.tela_input.setPlaceholderText("ID video do Youtube")
        layout.addWidget(QLabel("ID video do Youtube"))
        layout.addWidget(self.tela_input)

        # Botão para selecionar imagem do card
        self.btn_selecionar_card = QPushButton("Selecionar Imagem do Card", self)
        self.btn_selecionar_card.clicked.connect(self.selecionar_imagem_card)
        layout.addWidget(self.btn_selecionar_card)

        # Label para mostrar o caminho da imagem do card
        self.imagem_card_label = QLabel("Nenhuma imagem de card selecionada")
        layout.addWidget(self.imagem_card_label)

        # Botão para selecionar imagem do banner
        self.btn_selecionar_banner = QPushButton("Selecionar Imagem do Banner", self)
        self.btn_selecionar_banner.clicked.connect(self.selecionar_imagem_banner)
        layout.addWidget(self.btn_selecionar_banner)

        # Label para mostrar o caminho da imagem do banner
        self.imagem_banner_label = QLabel("Nenhuma imagem de banner selecionada")
        layout.addWidget(self.imagem_banner_label)

        # Botão para cadastrar
        self.btn_cadastrar = QPushButton("Cadastrar", self)
        self.btn_cadastrar.clicked.connect(self.cadastrar_imagem)
        layout.addWidget(self.btn_cadastrar)

        # Variáveis para armazenar os caminhos das imagens
        self.caminho_imagem_card = None
        self.caminho_imagem_banner = None

    def selecionar_imagem_card(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self, "Selecionar Imagem do Card", "", 
            "Imagens (*.png *.jpg *.jpeg *.bmp)"
        )
        if caminho:
            self.caminho_imagem_card = caminho
            self.imagem_card_label.setText(f"Card: {caminho.split('/')[-1]}")

    def selecionar_imagem_banner(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self, "Selecionar Imagem do Banner", "", 
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
            QMessageBox.warning(self, "Erro", "Nome, imagem do card e imagem do banner são obrigatórios!")
            return

        try:
            imagem_card_blob = converter_imagem_para_blob(self.caminho_imagem_card)
            imagem_banner_blob = converter_imagem_para_blob(self.caminho_imagem_banner)
            conn = mysql.connector.connect(**banco)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO imagens (nome, descricao, video_id, imagem_card, imagem_banner)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nome, descricao, video_id, imagem_card_blob, imagem_banner_blob))
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Imagens cadastradas com sucesso!")
            self.limpar_campos()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar: {e}")
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

# Função principal
def main():
    # Criar o banco de dados e a tabela se não existirem
    criar_tabela()

    # Iniciar a aplicação
    app = QApplication(sys.argv)
    janela = CadastroImagem()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
import mysql.connector
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import Qt

# Função para conectar ao MySQL
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",  # Coloque a senha se necessário
            database="cinefilmes_db",  # Nome do banco de dados
        )
        print("Conexão bem-sucedida!")
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        return None

# Função para criar o banco de dados
def criar_banco():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            # Cria o banco de dados se ele não existir
            cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_cadastro")
            print("Banco de dados criado com sucesso ou já existe.")
        except mysql.connector.Error as err:
            print(f"Erro ao criar o banco de dados: {err}")
        finally:
            conexao.close()
    else:
        print("Não foi possível conectar ao MySQL.")

# Função para criar a tabela
def criar_tabela():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            # Cria a tabela 'usuarios' se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    senha VARCHAR(255)
                )
            """)
            print("Tabela 'usuarios' criada com sucesso ou já existe.")
        except mysql.connector.Error as err:
            print(f"Erro ao criar a tabela: {err}")
        finally:
            conexao.close()
    else:
        print("Não foi possível conectar ao MySQL.")

# Chama as funções para criar o banco de dados e a tabela
criar_banco()
criar_tabela()

import mysql.connector
from mysql.connector import Error

def conectar_banco():
    try:
        # Conecta ao banco de dados MySQL
        conn = mysql.connector.connect(
            host='localhost',  # ou o endereço do seu servidor MySQL
            user='root',       # seu usuário do MySQL
            password='',       # sua senha (deixe em branco se não houver senha)
            database='cinefilmes_db'  # banco de dados que você quer usar
        )
        if conn.is_connected():
            print("Conexão com o MySQL estabelecida com sucesso.")
            return conn
        else:
            print("Não foi possível conectar ao MySQL.")
            return None
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def criar_banco():
    try:
        # Conecta ao MySQL sem banco de dados (apenas para criar o banco)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        cursor = conn.cursor()
        
        # Cria o banco de dados 'sistema_cadastro' se não existir
        cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_cadastro")
        print("Banco de dados 'sistema_cadastro' criado ou já existe.")
        
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"Erro ao criar banco de dados: {e}")

def criar_tabela():
    conn = conectar_banco()  # Conecta ao banco de dados 'sistema_cadastro'
    if conn is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = conn.cursor()
        
        # Cria a tabela de usuários se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único do usuário
                email VARCHAR(100) NOT NULL UNIQUE, -- E-mail do usuário
                senha VARCHAR(255) NOT NULL,        -- Senha do usuário
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP -- Data de criação do registro
            );
        """)
        
        conn.commit()  # Confirma as alterações no banco de dados
        print("Tabela 'usuarios' criada com sucesso ou já existe.")
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        conn.close()  # Garante que a conexão será fechada

# Chama a função para criar o banco de dados (caso não exista)
criar_banco()

# Chama a função para criar a tabela de usuários
criar_tabela()

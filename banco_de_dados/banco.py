import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",    
        user="root",   # Altere para seu usuário do MySQL
        password="", # Altere para sua senha do MySQL
        database="sistema_cadastro"
    )

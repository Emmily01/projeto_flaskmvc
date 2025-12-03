import mysql.connector

print("Conectando ao MySQL...")

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="" 
    )

    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS central_achados")
    print("✅ Sucesso! O banco de dados 'central_achados' foi criado/verificado.")

except mysql.connector.Error as err:
    print(f"❌ Erro ao conectar no MySQL: {err}")
    print("Verifique se o XAMPP/MySQL está rodando (Luz verde no painel).")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()

        conexao.close()

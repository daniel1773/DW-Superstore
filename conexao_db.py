import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_db():

    try:
        conexao = oracledb.connect(
            user = os.getenv("user_db"),
            password = os.getenv("password_db"),
            dsn = os.getenv("dsn_db"),
            mode = oracledb.SYSDBA
        )
        print("Conexão com Oracle deu certo!")
        return conexao

    except oracledb.Error as e:
        erro_obj, = e.args
        print(erro_obj.message)
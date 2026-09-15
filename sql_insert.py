import pandas as pd
from conexao_db import conectar_db

def formatar_lista(lista):
    lista2 = []
    for e in lista:
        palavra = ''
        for c in e.lower():
            if c == " " or c == "-":
                palavra += "_"
            else:
                palavra += c
        lista2.append(palavra)
    return lista2
    

#DATA FRAME
dados = pd.read_csv(r"dados_brutos\Superstore.csv", encoding='latin1')
dados_filtrado = dados.drop(columns=["Row ID"])


##Permite o Oracle reconhecer datas no formato 02/31/2005 como 31/02/2005
dados_filtrado["Order Date"] = pd.to_datetime(
    dados_filtrado["Order Date"],
    format="%m/%d/%Y"
)
dados_filtrado["Ship Date"] = pd.to_datetime(
    dados_filtrado["Ship Date"],
    format="%m/%d/%Y"
)

#nome de todas as colunas do arquivo CSV
nome_colunas_csv = list(dados_filtrado.columns)
nome_colunas_csv_formatado = formatar_lista(nome_colunas_csv)
nome_colunas_csv_string = ', '.join(nome_colunas_csv_formatado)

#quantidade de colunas do csv com formato em ":numero1, :numero2 ..."
segunda_parte_sql = ", ".join(f":{i+1}" for i in range(len(dados_filtrado.columns)))

#montando a consulta SQL com as duas variaveis anteriores
sql_insert = f"""
    INSERT INTO stg_superstore ({nome_colunas_csv_string})
    VALUES ({segunda_parte_sql})
"""

#--------------------------

sql_valores = dados_filtrado.values.tolist()

conexao = conectar_db()

with conexao.cursor() as cursor:
    cursor.executemany(sql_insert, sql_valores)
conexao.commit()
conexao.close()
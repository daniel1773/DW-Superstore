from conexao_db import conectar_db

#--- STAGING TABLE ---#
sql_stg_table = """
    CREATE TABLE stg_superstore(
        row_id NUMBER(10) GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        order_id VARCHAR2(14),
        order_date VARCHAR2(10),
        ship_date VARCHAR(10),
        ship_mode VARCHAR2(40),
        customer_id VARCHAR2(8),
        customer_name VARCHAR2(25),
        segment VARCHAR2(25),
        country VARCHAR2(25),
        city VARCHAR2(25),
        state VARCHAR(25),
        postal_code NUMBER(5),
        region VARCHAR2(10),
        product_id VARCHAR2(15),
        category VARCHAR2(25),
        sub_category VARCHAR2(25),
        product_name VARCHAR2(150),
        sales NUMBER(10,2),
        quantity NUMBER(10),
        discount NUMBER(3,2),
        profit NUMBER(10,3)
    )
"""

conexao = conectar_db()
try:
    with conexao.cursor() as cursor:
        cursor.execute(sql_stg_table)
    conexao.commit()
    print("tabela criada com sucesso!")
except:
    print("ERRO ao criar tabela!")
conexao.close()
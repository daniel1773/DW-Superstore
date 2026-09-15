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

#--- DIMENSIONS TABLES ---#
sql_dim_customer_table = """
    CREATE TABLE dim_customer (
        customer_key NUMBER,
        customer_id VARCHAR2(8) NOT NULL,
        name VARCHAR2(50),
        segment VARCHAR2(25)
    )
"""

sql_dim_product_table = """
    CREATE TABLE dim_product (
        product_key NUMBER,
        product_id VARCHAR2(25),
        name VARCHAR2(200),
        category VARCHAR2(25),
        sub_category VARCHAR2(25)
    )
"""

sql_dim_location_table = """
    CREATE TABLE dim_location (
        location_key NUMBER,
        country VARCHAR2(25),
        city VARCHAR2(25),
        state VARCHAR2(40),
        region VARCHAR2(25),
        postal_code NUMBER(15)
    )
"""

sql_dim_ship_table = """
    CREATE TABLE dim_ship (
        ship_mode_key NUMBER,
        ship_mode VARCHAR2(25) NOT NULL
    )
"""

sql_dim_data_table = """
    CREATE TABLE dim_data (
        data_key NUMBER,
        order_date,
        year NUMBER,
        month NUMBER,
        day NUMBER,
        ship_date
    )
"""

#--- FACT TABLE ---#
sql_fact_sale_table = """
    CREATE TABLE fact_sale (
        order_id
        sales
        quantity
        discount
        profit,
        keykeykey
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
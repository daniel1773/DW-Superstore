from conexao_db import conectar_db

#--- STAGING TABLE ---#
sql_stg_table = """
    CREATE TABLE stg_superstore(
        row_id NUMBER(10) GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        order_id VARCHAR2(14),
        order_date DATE,
        ship_date DATE,
        ship_mode VARCHAR2(40),
        customer_id VARCHAR2(8),
        customer_name VARCHAR2(50),
        segment VARCHAR2(25),
        country VARCHAR2(25),
        city VARCHAR2(40),
        state VARCHAR2(40),
        postal_code NUMBER(15),
        region VARCHAR2(25),
        product_id VARCHAR2(25),
        category VARCHAR2(25),
        sub_category VARCHAR2(25),
        product_name VARCHAR2(200),
        sales NUMBER(10, 2),
        quantity NUMBER(10),
        discount NUMBER(3, 2),
        profit NUMBER(10, 3)
    )
"""

#--- DIMENSIONS TABLES ---#
sql_dim_customer_table = """
    CREATE TABLE dim_customer (
        sk_customer NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        customer_id VARCHAR2(8) NOT NULL,
        name VARCHAR2(50),
        segment VARCHAR2(25)
    )
"""

sql_dim_product_table = """
    CREATE TABLE dim_product (
        sk_product NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        product_id VARCHAR2(25) NOT NULL,
        name VARCHAR2(200),
        category VARCHAR2(25),
        sub_category VARCHAR2(25)
    )
"""

sql_dim_location_table = """
    CREATE TABLE dim_location (
        sk_location NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        postal_code NUMBER(15),
        country VARCHAR2(25),
        region VARCHAR2(25),
        state VARCHAR2(40),
        city VARCHAR2(40)
    )
"""

sql_dim_ship_table = """
    CREATE TABLE dim_ship (
        sk_ship_mode NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        ship_mode VARCHAR2(40) NOT NULL
    )
"""

sql_dim_data_table = """
    CREATE TABLE dim_date (
        sk_data NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        full_date DATE NOT NULL,
        year NUMBER(4),
        month NUMBER(2),
        day NUMBER(2),
        day_name VARCHAR2(15),
        month_name VARCHAR2(15)
    )
"""

#--- FACT TABLE ---#
sql_fact_sale_table = """
    CREATE TABLE fact_sale (
        sk_customer NUMBER,
        sk_product NUMBER,
        sk_location NUMBER,
        sk_ship_mode NUMBER,
        sk_order_date NUMBER,
        sk_ship_date NUMBER,
        order_id VARCHAR2(14),
        sales NUMBER(10, 2),
        quantity NUMBER(10),
        discount NUMBER(3, 2),
        profit NUMBER(10, 3),
        
        CONSTRAINT fk_fact_customer FOREIGN KEY (sk_customer) REFERENCES dim_customer(sk_customer),
        CONSTRAINT fk_fact_product  FOREIGN KEY (sk_product) REFERENCES dim_product(sk_product),
        CONSTRAINT fk_fact_location FOREIGN KEY (sk_location) REFERENCES dim_location(sk_location),
        CONSTRAINT fk_fact_ship     FOREIGN KEY (sk_ship_mode) REFERENCES dim_ship(sk_ship_mode),
        CONSTRAINT fk_fact_ord_date FOREIGN KEY (sk_order_date) REFERENCES dim_data(sk_data),
        CONSTRAINT fk_fact_shp_date FOREIGN KEY (sk_ship_date) REFERENCES dim_data(sk_data)
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
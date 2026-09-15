## Sobre
Projeto de estudo sobre Data Warehouse em Star Schema utilizando python, pandas, sql, oracle e o dataset Superstore da Kaggle.

## Estrutura do modelo dimensional

### Tabela Staging
* `stg_superstore` (dados brutos do dataset Superstore)

### Tabela Fato
* `fact_sale` (sk_customer, sk_product, sk_location, sk_ship_mode, sk_order_date, sk_ship_date, order_id, sales, quantity, discount, profit)

### Tabelas Dimensão:
* `dim_customer` (sk_customer, customer_id, name, segment)
* `dim_product` (sk_product, product_id, name, category, sub_category)
* `dim_location` (sk_location, postal_code, country, region, state, city)
* `dim_ship` (sk_ship_mode, ship_mode)
* `dim_date` (sk_date, full_date, year, month, day)

## Tecnologias Utilizadas
* **Linguagens**: Python 3.14 e SQL
* **Bibliotecas Python**: `pandas`, `os`, `python-dotenv`, `oracledb`
* **Banco de dados**: Oracle (local)
* **Dataset**: Superstore (Kaggle)
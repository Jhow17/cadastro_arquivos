import sqlite3
import conection


def cria_banco():
    
    conn = conection.conectar_banco()
    try:
        with conn:
            create_table_query = '''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL,
                    description TEXT
                );
                '''
            cursor=conn.cursor()
            cursor.execute(create_table_query)
    except sqlite3.Error as e:
        print(f"Erro {e}")
    conn.close()
  


def cadastrar_banco(dados):
    
    conn = conection.conectar_banco()
    try:
        cria_banco()
        with conn:
            cursor = conn.cursor()

            # avoid Injection? placeholders in parameterized queries ensure that input values are treated as data
            query = "INSERT INTO products (name, price, description) VALUES (?, ?, ?)"
            cursor.executemany(query, dados)
            
            print(f"{cursor.rowcount} produtos adicionados no banco")
            
    except sqlite3.Error as e:
        print(f"Erro a cadastrar no banco de dados {e}")
    
        
    conn.close()


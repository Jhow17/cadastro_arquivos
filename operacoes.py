import sqlite3
import conection
import gerir_arquivos


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


def get_all():
    conn = conection.conectar_banco()
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM products WHERE products.price <= 10"
        cursor.execute(query) 
        lista_tuplas = cursor.fetchmany(size=cursor.arraysize // 2)
        
        resul_json = gerir_arquivos.to_JSON(lista_tuplas)
        return resul_json

    except sqlite3.Error as e :
        print(f"Erro ao pegar produtos no banco {e}")
        
    conn.close()
        


def cadastrar_banco(dados):
    
    conn = conection.conectar_banco()
    try:
        cria_banco()
        with conn:
            cursor = conn.cursor()

            # avoid Injection? sqlite placeholders in parameterized queries ensure that input values are treated as data
            query = "INSERT INTO products (name, price, description) VALUES (?, ?, ?)"
            cursor.executemany(query, dados)
            
            print(f"{cursor.rowcount} produtos adicionados no banco")
            
    except sqlite3.Error as e:
        print(f"Erro a cadastrar no banco de dados {e}")
    
        
    conn.close()


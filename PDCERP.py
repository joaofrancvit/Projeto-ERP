import sqlite3

conn = sqlite3.connect("dados_galpao.db")
cursor = conn.cursor()

#criação da tabela de produtos abaixo

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    sku_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT UNIQUE NOT NULL,
    descricao TEXT NOT NULL
)
""")

#criação da tabela de endereços abaixo

cursor.execute("""
CREATE TABLE IF NOT EXISTS enderecos(
    sku_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT UNIQUE NOT NULL,
    enderecamento TEXT,
    FOREIGN KEY (sku_id) REFERENCES produtos(sku_id)
)
""")

#criação da tabela de kardex/movimentações

cursor.execute("""
CREATE TABLE IF NOT EXISTS movimentacao_estoque(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku_id INTEGER NOT NULL,
    tipo TEXT CHECK(tipo IN ('ENTRADA', 'SAIDA', 'AJUSTE')),
    quantidade INTEGER NOT NULL,
    documento TEXT,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_usuario INTEGER,
    FOREIGN KEY (sku_id) REFERENCES produtos(sku_id)
)
""")

#criação tabela de saldos em estoque
cursor.execute("""
CREATE TABLE IF NOT EXISTS estoque(
    sku_id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
    qtd_disp INTEGER NOT NULL DEFAULT 0,
    qtd_resv INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (sku_id) REFERENCES produtos(sku_id)
)
""")
conn.commit()

def cadastrar_sku(sku, descricao):
    try:
        cursor.execute("INSERT INTO produtos(sku, descricao) VALUES (?, ?)", (sku, descricao))
        sku_id = cursor.lastrowid
        cursor.execute("INSERT INTO enderecos(sku) VALUES (?)", (sku,))
        cursor.execute("INSERT INTO estoque(qtd_disp) VALUES (?)", ('0'))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        print(f"Erro: O SKU {sku} já está cadastrado.")

def buscar_sku(sku):
    cursor.execute("SELECT sku, descricao FROM produtos WHERE sku = ?",(sku,))
    resultado = cursor.fetchone()
    if resultado:
        print(f'SKU: {resultado[0]} Descrição: {resultado[1]}')
    else:
        print('SKU não cadastrado.')

def enderecar(sku, endereco):
    try:
        cursor.execute("""UPDATE enderecos
        WHERE sku = ?
        SET enderecamento = ?
        """,(sku, endereco))
        print(f'SKU {sku} endereçado no endereço {endereco}')
    except:
        print('Erro!')

def buscar_endereco(sku):
    cursor.execute("SELECT sku, enderecamento FROM enderecos WHERE sku = (?)", (sku,))
    resultado = cursor.fetchone()
    if resultado:
        print(f'O endereço de {resultado[0]} é {resultado[1]}')

def movimentar_saldo(sku_id, quantidade, documento, id_usuario):
    try:
        cursor.execute("INSERT INTO movimentacao_estoque(sku_id, quantidade, documento, id_usuario) VALUES(?,?,?,?)",(sku_id, quantidade, documento, id_usuario))

        cursor.execute("""
        UPDATE estoque
        SET qtd_disp = qtd_disp + ?
        WHERE sku_id = ?
        """,(sku_id, quantidade))
        conn.commit()
        print(f'Movimentação concluída de {quantidade} do id{sku_id}.')
    except:
        print("Movimentação não concluída.")
        conn.rollback()


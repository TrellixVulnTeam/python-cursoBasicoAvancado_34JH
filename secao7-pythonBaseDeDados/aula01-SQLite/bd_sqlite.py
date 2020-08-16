import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

#cursor.execute ('CREATE TABLE IF NOT EXISTS clientes ('
#               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#               'nome TEXT,'
#               'peso REAL'
#               ')')
'''
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
                {'nome': 'Joãozinho', 'peso': 25})

cursor.execute('INSERT INTO clientes VALUES (:nome, :peso)',
                {'id':None, 'nome': 'Daniel', 'peso': 25})

conexao.commit()
'''

cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Karla', 'id': 2}
)

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)


cursor.close()
conexao.close()
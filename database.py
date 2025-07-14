import sqlite3

def conexao():
    conect = sqlite3.connect('crud.db')
    cursor = conect.cursor()
    return cursor

##### CREATE ######
def CREATE_TABLE():
    cursor.execute('''CREATE TABLE IF NOT EXISTS funcionario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        funcao TEXT,
        salario FLOAT,
        setor TEXT);
    ''')

def INSERT(dados):
    conect = sqlite3.connect('crud.db')
    cursor = conect.cursor()
    cursor.execute('''INSERT INTO funcionario (nome,funcao,salario,setor) VALUES(?,?,?,?)''',
                   [dados[1],dados[2],dados[3],dados[4]])
    conect.commit()
    

##### README #####
def README():
    cursor = conexao()
    cursor.execute('SELECT * FROM funcionario')
    lista = cursor.fetchall()
    return lista

##### UPDATE #####
def UPDATE(dados):
    cursor = conexao()
    cursor.execute(f'''UPDATE funcionario SET 
            nome = {dados[1]},
            funcao = {dados[2]},
            salario = {dados[3]},
            setor = {dados[4]},
            WHERE id = {dados[0]}
    ''')
    

##### DELETE #####
def DELET(id):
    cursor = conexao()
    cursor.execute(f'DELET FROM funcionario WHERE id = {id}')
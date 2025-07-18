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
                   [dados[0],dados[1],dados[2],dados[3]])
    conect.commit()
    

##### README #####
def README():
    cursor = conexao()
    cursor.execute('SELECT * FROM funcionario')
    return cursor.fetchall()


##### UPDATE #####
def UPDATE(dados):
    conect = sqlite3.connect('crud.db')
    cursor = conect.cursor()
    cursor.execute(f'''UPDATE funcionario SET 
            nome = '{dados[0]}',
            funcao = '{dados[1]}',
            salario = '{dados[2]}',
            setor = '{dados[3]}'
            WHERE id = {dados[4]}
    ''')
    conect.commit()

##### DELETE #####
def DELET(id):
    conect = sqlite3.connect('crud.db')
    cursor = conect.cursor()
    cursor.execute(f"DELETE FROM funcionario WHERE id = {id} ")
    conect.commit()


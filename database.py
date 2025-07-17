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
    
#INSERT(dados=['MARCELO','analista de Ti','2000','Ti'])

##### README #####
def README():
    cursor = conexao()
    cursor.execute('SELECT * FROM funcionario')
    return cursor.fetchall()


##### README COM CONDIÇÃO LÓGICA######
def UPDATE_LOGICA(id):
    cursor = conexao()
    cursor.execute(f'SELECT * FROM funcionario WHERE id = {id}')
    return cursor.fetchall()


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
    conect = sqlite3.connect('crud.db')
    cursor = conect.cursor()
    cursor.execute(f"DELETE FROM funcionario WHERE id = {id} ")
    conect.commit()

#DELET(7)
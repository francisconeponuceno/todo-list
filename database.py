import sqlite3

conect = sqlite3.connect('crud.db')
cursor = conect.cursor()

##### CREATE ######
def CREATE_TABLE():
    cursor.execute('''CREATE TABLE IF NOT EXISTS funcionario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        funcao TEXT,
        salario FLOAT,
        setor TEXT);
    ''')

def INSERT():
    cursor.execute('''INSERT INTO funcionario (nome,funcao,salario,setor) VALUES(?,?,?,?)''',
                   ['João','Axiliar de Ti','1900','Ti'])
    
    conect.commit()
    print('dados salvos com sucesso')

##### README #####
def README():
    cursor.execute('SELECT * FROM funcionario')
    lista = cursor.fetchall()
    return lista

##### UPDATE #####
def UPDATE(dados):
    cursor.execute(f'''UPDATE funcionario SET 
                   nome = {dados[1]},
                   funcao = {dados[2]},
                   salario = {dados[3]},
                   setor = {dados[4]},
                   WHERE id = {dados[0]}
                   ''')
    print(README())


##### DELETE #####

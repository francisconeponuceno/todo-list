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

def README ():
    conect = sqlite3.connect('crud.db')

    cursor = conect.cursor()
    cursor.execute('''INSERT INTO funcionarios (nome,funcao,salario,setor) VALUES(?,?,?,?)''',
                   ['Francisco','Analista de Sistema','2000','Ti'])
    
    conect.commit()
README()
##### README #####

##### UPDATE #####

##### DELETE #####

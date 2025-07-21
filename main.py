import database
from flask import Flask, render_template, request, redirect



app = Flask(__name__)

@app.route('/')
def index():
    lista = database.README()
    dados_formulario = request.form.to_dict()
    return render_template('index.html',lista=lista,dados=dados_formulario)

@app.route('/principal', methods=['POST','GET'])
def principal():
    return redirect('/')

## ADICIONAR OS DADOS
@app.route('/adicionar', methods=['POST'])
def adicionar():
    form_dados = request.form.to_dict() # captura todos os campos do formulário
    database.INSERT(dados=list(form_dados.values()))
    return redirect('/')


## SELECIONAR OS DADOS
@app.route('/select/<int:id>', methods=['POST','GET'])
def select(id):
    select_dados = database.select(id)
    return render_template('update.html',select_dados=select_dados)

    
## FASER A ALTERAÇÃO DOS DADOS
@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    lista = request.form.to_dict()
    lista = list(lista.values())
    lista.append(id)
    database.UPDATE(dados=lista)
    return redirect('/')
    
    
## FASER A EXCLUSÃO DOS DADOS
@app.route('/delete',methods=['POST', 'GET'])
def delete():
    id = request.form['pont']
    database.DELET(id)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)

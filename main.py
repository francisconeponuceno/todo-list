import database
from flask import Flask, render_template, request, redirect



app = Flask(__name__)

@app.route('/')
def index():
    lista = database.README()
    dados_formulario = request.form.to_dict()
    return render_template('index.html',lista=lista,dados=dados_formulario)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    form_dados = request.form.to_dict() # captura todos os campos do formulário
    database.INSERT(dados=list(form_dados.values()))
    return redirect('/')

    
@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    lista = request.form.to_dict()
    lista = list(lista.values())
    lista.append(id)
    database.UPDATE(dados=lista)
    return redirect('/')
    
    
@app.route('/delete/<int:id_task>',methods=['POST', 'GET'])
def delete(id_task):
    id = id_task
    database.DELET(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

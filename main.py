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

    
@app.route('/update', methods=['POST','GET'])
def update():
    pass


@app.route('/delete',methods=['POST', 'GET'])
def delete():
    id = request.form.to_dict()
    id = list(id.values())
    database.DELET(id[0])
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

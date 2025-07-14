import database
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():

    lista = database.README()
    dados_formulario = request.form.to_dict()
    return render_template('index.html',lista=lista,dados=dados_formulario)


@app.route('/adicionar')
def adicionar():
    
    
    return render_template('index.html')
    



if __name__ == '__main__':
    app.run(debug=True)

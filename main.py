from flask import Flask, render_template, request, redirect
import database
app = Flask(__name__)

@app.route('/')
def index():

    lista = database.README()
    print(lista)
    return render_template('index.html',lista=lista)

if __name__ == '__main__':
    app.run(debug=True)
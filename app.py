from flask import Flask, render_template

app = Flask('meu app')

posts = [
    {
        "titulo": "Minha primeira postagem",
        "texto": "Testando",
    },
    {
        "titulo": "Segunda postagem",
        "texto": "Testando navamente",
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)
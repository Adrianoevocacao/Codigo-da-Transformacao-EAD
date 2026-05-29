from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
 
ARQUIVO_JSON = 'produtos.json'


# ler produtos do json
def ler_produtos():

    if not os.path.exists(ARQUIVO_JSON):
        return []

    with open(ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo:
        produtos = json.load(arquivo)

    return produtos


# salvar produtos no json
def salvar_produtos(produtos):

    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)


# página inicial
@app.route('/')
def index():

    produtos = ler_produtos()

    return render_template('index.html', produtos=produtos)


# adicionar produto
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():

    if request.method == 'POST':

        nome = request.form['nome']
        preco = request.form['preco']
        descricao = request.form['descricao']

        produtos = ler_produtos()

        novo_produto = {
            'id': len(produtos) + 1,
            'nome': nome,
            'preco': preco,
            'descricao': descricao
        }

        produtos.append(novo_produto)

        salvar_produtos(produtos)

        return redirect('/')

    return render_template('adicionar.html')


# detalhes do produto
@app.route('/produto/<int:id>')
def detalhes(id):

    produtos = ler_produtos()

    produto_encontrado = None

    for produto in produtos:

        if produto['id'] == id:
            produto_encontrado = produto
            break

    return render_template('detalhes.html', produto=produto_encontrado)


if __name__ == '__main__':
    app.run(debug=True)
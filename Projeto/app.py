# Exercício 6 - 

# 1. Cria um novo projeto Flask com uma estrutura de diretórios adequada.
# 2. O teu website deve ter pelo menos três páginas: uma página inicial, uma página de
# desafios e uma página final.
# 3. Na página inicial, dá as boas-vindas aos visitantes e apresenta o propósito do teu
# website.
# 4. Na página de desafios, cria pelo menos três desafios interactivos que os visitantes
# devem completar para avançar para a página final. Utiliza formulários para capturar as
# respostas dos visitantes e exibe mensagens personalizadas baseadas nas suas
# respostas (por exemplo, se acertaram ou não).
# 5. Na página final, agradece aos visitantes pela participação e convida-os a deixar um
# comentário ou mensagem utilizando um formulário.
# 6. Personaliza o design do teu website utilizando CSS. Podes adicionar imagens e outros
# elementos visuais para torná-lo mais atractivo.
# 7. Certifica-te de que o teu código está bem organizado e comentado.
# 8. Faz uso da tua criatividade para tornar o teu website único e interessante.

# Exemplo de adicionar uma imagem num template HTML:
# html
# <img src="{{ url_for('static', filename='image.jpg') }}" alt="Descrição da Imagem">

# Para adicionar estilos CSS, pode-se criar um arquivo `.css` na pasta `static`.
# Exemplo de linkar o arquivo CSS num template HTML:
# html
# <link rel="stylesheet" href="{{ url_for('static', filename='estilos.css') }}">

# Exemplo de adicionar estilos CSS inline diretamente nos elementos HTML:
# html
# <h1 style="color: blue; text-align: center;">Título Centralizado em Azul</h1>

# Adicionando Hyperlinks
# Use hyperlinks para guiar o utilizador através das pistas. Certifique-se de que cada pista conduz de forma
# lógica à próxima.
# Exemplo de adicionar um hyperlink num template HTML:
# html
# <a href="{{ url_for('proxima_pista') }}">Clique aqui para a próxima pista</a>

from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RespostaForm, MensagemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo'
respostas = ['branca', 'esquerda', 'botão','flask']
mensagens = []

# Estrutura de Pastas do Projeto

# # seu_projeto/
# │ app.py
# | forms.py
# │
# ├───static/
# │ │ nome-da-imagem.jpg
# │ │ estilos.css
# │
# ├───templates/
# │ │ home.html
# │ │ Desafio1.html
# │ │ Desafio2.html
# │ │ Desafio3.html
# │ │ sucesso.html
# │ │ mensagens.html

@app.route("/", methods=['GET', 'POST'])
def home():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[0].lower():
            return redirect(url_for('Desafio1'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('home.html', form=form)

@app.route("/Desafio1", methods=['GET', 'POST'])

def Desafio1():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[1].lower():
            return redirect(url_for('Desafio2'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('Desafio1.html', form=form)

@app.route("/Desafio2", methods=['GET', 'POST'])

def Desafio2():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[2].lower():
            return redirect(url_for('Desafio3'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('Desafio2.html', form=form)

@app.route("/Desafio3", methods=['GET', 'POST'])

def Desafio3():
    form = RespostaForm()
    if form.validate_on_submit():
        if form.resposta.data.lower() == respostas[3].lower():
            return redirect(url_for('sucesso'))
        else:
            flash('Resposta incorreta. Tenta novamente.', 'error')
    return render_template('Desafio3.html', form=form)

@app.route("/sucesso", methods=['GET', 'POST'])

def sucesso():
    form = MensagemForm()
    if form.validate_on_submit():
        mensagem = form.mensagem.data
        mensagens.append(mensagem)
        print(f'Mensagem recebida: {mensagem}') # Print da mensagem no terminal
        flash(f'Mensagem enviada com sucesso! Já existem {len(mensagens)} mensagem(s).', 'success')
    return render_template('sucesso.html', form=form)

@app.route("/mensagens")

def ver_mensagens():
    return render_template('mensagens.html', mensagens=mensagens)

if __name__ == "__main__":
    app.run()
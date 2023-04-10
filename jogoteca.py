from flask import Flask, render_template


class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

# Iniciar o variavel do projeto
app = Flask(__name__)

# Criar um nova rota
@app.route('/inicio')
def ola():

    jogo1 = Jogo('Tetris', 'Puzzle', 'Ataria')
    jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista = [jogo1, jogo2, jogo3]

    return render_template('lista.html', titulo='Jogos', jogos=lista)


# Rodar o projeto
app.run()

# trecho da app
#app.run(host='0.0.0.0', port=8080)

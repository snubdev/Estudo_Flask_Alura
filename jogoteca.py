from flask import Flask, render_template

# Iniciar o variavel do projeto
app = Flask(__name__)

# Criar um nova rota
@app.route('/inicio')
def ola():
    return render_template('lista.html')


# Rodar o projeto
app.run()

# trecho da app
#app.run(host='0.0.0.0', port=8080)

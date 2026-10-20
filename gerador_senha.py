from flask import Flask, render_template_string
import string
import random

app = Flask(__name__)

@app.route("/")
def home():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    comprimento = 12
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    
    # HTML simples retornado pelo Python
    return render_template_string(f"""
        <h2>Gerador de Senha em Python</h2>
        <p>Senha gerada: <strong>{{ senha }}</strong></p>
        <a href="/">Gerar nova senha</a>
    """, senha=senha)

if __name__ == "__main__":
    app.run(debug=True)
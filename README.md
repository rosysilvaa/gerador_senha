##🔐 Gerador de Senhas (Password Generator)

Este projeto é uma aplicação web simples e eficiente para geração de senhas seguras e aleatórias. O repositório contém duas implementações distintas:

Versão Web (Frontend): Construída com HTML5, CSS3 e JavaScript, funcionando diretamente no navegador sem necessidade de backend.

Versão Server-Side (Backend): Construída com Python e Flask, processando a lógica no servidor e renderizando a resposta na página web.

##🛠️ Tecnologias Utilizadas

HTML5: Estruturação da interface web.

CSS3: Estilização e layout responsivo.

JavaScript (ES6+): Lógica do gerador de senhas no lado do cliente (Client-side).

Python 3: Linguagem de programação para a lógica de backend.

##Flask: Microframework web em Python para criação das rotas e servidor web.

1. Pré-requisitos

Certifique-se de ter o Python 3.x instalado.

2. Instalação de Dependências

Crie e ative um ambiente virtual (opcional, mas recomendado) e instale o Flask:

# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual (Windows)
.venv\Scripts\activate

# Ativar ambiente virtual (Linux/Mac)
source .venv/bin/activate

# Instalar o Flask
pip install flask


3. Executando o Servidor

Execute o arquivo principal (app.py):

python app.py


4. Acessando no Navegador

Abra o navegador e acesse o endereço fornecido no terminal:
http://127.0.0.1:5000

💡 Como Funciona a Geração de Senhas?

O gerador sorteia caracteres aleatórios com base em um conjunto completo que inclui:

Letras minúsculas: a-z

Letras maiúsculas: A-Z

Números: 0-9

Símbolos/Caracteres especiais: !@#$%^&*()_+-=[]{}|;:,.<>?

Por padrão, a senha gerada possui o comprimento de 12 caracteres, garantindo um alto nível de segurança contra ataques de força bruta.

📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.<img width="1366" height="768" alt="Captura de tela 2026-10-19 220657" src="https://github.com/user-attachments/assets/32a5c703-5f86-4b00-b37f-ce9a5c1a8f02" />

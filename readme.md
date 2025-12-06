# Central de Achados e Perdidos - IFRN

Este projeto é uma aplicação web desenvolvida em Python com Flask, seguindo o **MVC (Model-View-Controller)** e organizada através de **Blueprints**. O sistema foi criado para modernizar, centralizar e agilizar o processo de registro, consulta e devolução de objetos perdidos no campus.

## Integrantes do Grupo
Carla Gabriele da Silva Santos

Ingrid Monteiro de Melo 

Emmily Kettily Bezerra da Silva

## Tecnologias Utilizadas
* O projeto segue a arquitetura **MVC (Model-View-Controller)**:

* **Linguagem:** Python 3
* **Framework:** Flask
* **Banco de Dados:** SQLite (via SQLAlchemy)
* **Autenticação:** Flask-Login
* **Frontend:** HTML5, CSS3, Jinja2
* **Organização:** Uso de *Blueprints* para modularização do código.


##  Como Rodar o Projeto

### 1. Pré-requisitos
* Ter o **Python** instalado.

### 2. Instalação das Dependências
Abra o terminal na pasta do projeto e execute:
1**(Opicional) Crie um ambiente virtual:**

Bash

python -m venv env
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

Bash

pip install flask flask-sqlalchemy flask-login mysql-connector-python werkzeug


### 3. Executando o Sistema
Inicie o servidor Flask com o comando:

Bash

python app.py
### 4. Acessando
Abra o navegador e digite:

https://www.google.com/search?q=http://127.0.0.1:5000

🚀 Funcionalidades do Sistema
👤 Área Pública (Alunos e Comunidade)
* Consultar Itens: Visualização pública de todos os objetos encontrados.

* Status: Identificação visual se o item está "Ativo" (na secretaria) ou "Devolvido".
  
* Detalhes: Informações sobre onde e quando o objeto foi encontrado.
  
🔐 Área Administrativa (Secretaria/Bolsistas)
* Login Seguro: Acesso restrito via usuário e senha.
  
* Cadastro de Itens: Registro de novos achados (descrição, categoria, local).
  
* Gestão Total: Edição e remoção de registros incorretos.
  
* Devolução (Baixa): Registro de quem retirou o objeto e a data da saída, mudando o status automaticamente para "Devolvido".



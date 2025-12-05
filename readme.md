# Central de Achados e Perdidos - IFRN

Este projeto é uma aplicação web desenvolvida em Python com Flask, seguindo o **MVC (Model-View-Controller)** e organizada através de **Blueprints**. O sistema foi criado para modernizar, centralizar e agilizar o processo de registro, consulta e devolução de objetos perdidos no campus.

## Integrantes do Grupo
Carla Gabriele da Silva Santos
Ingrid Monteiro de Melo 
Emmily Kettily Bezerra da Silva

## Tecnologias Utilizadas
* **Backend:** Python 3, Flask
* **Estrutura:** MVC com Blueprints
* **Banco de Dados:** MySQL (via conector `mysql-connector-python`)
* **ORM:** SQLAlchemy
* **Autenticação:** Flask-Login
* **Frontend:** HTML5, CSS3, Jinja2

##  Como Rodar o Projeto

### 1. Pré-requisitos
* Ter o **Python** instalado.
* Ter o **XAMPP** (ou outro servidor MySQL) instalado e rodando.

### 2. Instalação das Dependências
Abra o terminal na pasta do projeto e execute:
Bash
pip install flask flask-sqlalchemy flask-login mysql-connector-python werkzeug

### Configuração do Banco de Dados
Abra o painel do XAMPP e inicie o módulo MySQL (botão Start).

No terminal, execute o script de criação automática do banco:

Bash

python criar_banco.py
(Se aparecer "✅ Sucesso!", o banco central_achados foi criado corretamente).

Depois abre o MySql Workbench e roda esse código:
CREATE DATABASE achados_perdidos;

4. Executando o Sistema
Inicie o servidor Flask com o comando:

Bash

python app.py
5. Acessando
Abra o navegador e digite:

https://www.google.com/search?q=http://127.0.0.1:5000

🚀 Funcionalidades do Sistema
👤 Área Pública (Alunos e Visitantes)
Consultar Itens: Visualização de todos os objetos encontrados.

Status em Tempo Real: Identificação se o item está "Disponível", "Emprestado" ou "Devolvido".

Detalhes: Informações sobre onde e quando o objeto foi encontrado.

🔐 Área Administrativa (Funcionários/Bolsistas)
Login Seguro: Acesso restrito a usuários cadastrados.

Cadastro de Itens: Registro de novos achados com descrição, categoria e local.

Gerenciamento: Edição e remoção de registros.

Registro de Devolução/Saída: Controle de quem retirou o objeto, alterando o status automaticamente para "Emprestado" ou "Devolvido" e salvando o nome do responsável.

📝 Reflexão Crítica (Avaliação do Projeto)
Esta seção aborda os pontos críticos e sociais da solução, conforme solicitado na proposta do trabalho.

1. O Problema
A gestão de achados e perdidos em instituições de ensino frequentemente sofre com a desorganização. O uso de cadernos físicos ou planilhas locais dificulta a divulgação. Como resultado, muitos alunos não sabem onde procurar seus pertences, e a secretaria acumula objetos indefinidamente.

2. A Solução Web
A implementação de um sistema web centralizado resolve o problema da visibilidade.

Acessibilidade: O aluno pode verificar de qualquer lugar se seu objeto foi encontrado, sem precisar se deslocar fisicamente até a coordenação várias vezes.

Transparência: O sistema mostra claramente o status do item, evitando falsas esperanças se o objeto já tiver sido retirado.

3. Limites da Solução
Apesar dos benefícios, a tecnologia não resolve tudo:

Fator Humano: O sistema depende inteiramente que alguém encontre o objeto e tenha a boa vontade de levá-lo até a secretaria para registro.

Verificação de Identidade: O software registra quem retirou o item, mas a validação se aquela pessoa é realmente a proprietária do objeto continua sendo uma tarefa manual e presencial do funcionário.

Exclusão Digital: Pessoas sem acesso fácil à internet ou smartphones podem ter dificuldade em consultar a lista online.

4. Aprendizado Técnico
O desenvolvimento deste projeto consolidou o entendimento sobre a arquitetura MVC:

A separação de responsabilidades (models para dados, templates para interface, routes para lógica) tornou o código mais limpo.

O uso de Blueprints foi fundamental para organizar a aplicação em módulos ("Auth" e "Itens"), simulando um ambiente de desenvolvimento profissional.

A integração com banco de dados SQL permitiu entender na prática como persistir dados de forma segura e eficiente.
# projeto-login-com-mysql

🛡️ Sistema de Autenticação Full Stack - Flask & MySQL
Este projeto é um sistema de login e cadastro robusto, desenvolvido com foco em segurança da informação, UX (User Experience) e arquitetura limpa. A aplicação utiliza criptografia de ponta e gerenciamento seguro de credenciais.

## 📺 Demonstração em Vídeo
![Demonstração do Projeto](gravação_de_tela_do_codigo_rodando.mp4)

🚀 Tecnologias Utilizadas
Back-end: Python 3 com Framework Flask.

Banco de Dados: MySQL (Relacional).

Segurança: * Werkzeug: Para Hashing de senhas (PBKDF2 com SHA256).

Python-Dotenv: Gerenciamento de variáveis de ambiente para proteger credenciais.

Front-end: HTML5 e CSS3 com design moderno (Glassmorphism).

🛠️ Funcionalidades Principais
Cadastro de Usuários: Validação de dados e armazenamento seguro.

Criptografia de Senhas: Nenhuma senha é salva em texto puro no banco de dados. Utilizamos salting e hashing para garantir que, mesmo em caso de vazamento, os dados fiquem ilegíveis.

Sistema de Login: Verificação dinâmica de credenciais com comparação de Hash.

Feedback ao Usuário: Mensagens de alerta customizadas (Flask Flash) para erros de login ou sucesso no cadastro.

Proteção de Ambiente: Uso de arquivo .env para que chaves secretas e senhas do banco não fiquem expostas no código-fonte.

📂 Estrutura do Projeto
Plaintext

projeto-login/
├── static/              # Arquivos CSS e Imagens
├── templates/           # Páginas HTML (Jinja2)
├── .env                 # Variáveis sensíveis (não enviado ao GitHub)
├── .gitignore           # Proteção de arquivos
├── app.py               # Servidor e Rotas Flask
└── requirements.txt     # Dependências do sistema
🔧 Como Rodar o Projeto
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:

Bash

pip install -r requirements.txt
Configure o Banco de Dados:

Crie um banco chamado projeto_login.

Crie uma tabela usuarios com as colunas: id (INT AI), nome (VARCHAR), email (VARCHAR), senha (VARCHAR 255).

Configure o seu .env: Crie um arquivo .env na raiz e adicione suas credenciais:

Plaintext

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=projeto_login
SECRET_KEY=sua_chave_secreta
Inicie o servidor:

Bash

python app.py
👨‍💻 Desenvolvido por
Wendel -[Meu LinkedIn](https://www.linkedin.com/in/wendel-soares-b02528204/) | [Meu Portfolio](https://wsoaresdev.github.io/Meu-Portifolio/)
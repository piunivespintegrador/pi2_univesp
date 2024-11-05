# Univesp PI 2

Projeto Integrador II

Participantes:

```
Angra Dias de Olivera
Bruno Rosendo Alves
Felipe de Oliveira
Gabriel Antonio Ribeiro da Silva
Lucas Campos Achcar
Lucas Edson Santos Silva
Raquel Alves Nogueira Santos
Silvio Soares Pereira
```

Código do projeto integrador 2 usando Django 5.1.2 e Python 3.12.3

Crie um ambiente virtual (venv) do python3 

```
python3 -m venv /path/to/new/virtual/environment
```

Faça o acesso do seu venv do python3

```
source /path/to/new/virtual/environment/bin/activate
```

Para mais detalhes acesse [venv](https://docs.python.org/pt-br/3/library/venv.html)

Instalação das Dependências do Projeto

```
pip install -r requirements.txt
```

Faça a instalação do MySQL (Docker)

Crie o banco de dados do projeto

```
CREATE DATABASE lava_jato CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'seu_usuario'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON meu_banco_django.* TO 'seu_usuario'@'localhost';
FLUSH PRIVILEGES;
```

Isso criará um banco de dados chamado ```lava_jato``` com o usuário ```seu_usuario``` com a senha ```sua_senha```

Entre na pasta do projeto 

```
cd lava jato
```

No arquivo python ```settings.py```, configure o DATABASES adicionado a senha e o usuário criado por você na criação do banco de dados.

```
'mysql_db': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'lava_jato',     # Nome do banco de dados
    'USER': 'seu_usuario',   # Usuário do banco de dados
    'PASSWORD': 'sua_senha', # Senha do banco de dados
    'HOST': '127.0.0.1',     # Endereço do servidor (pode ser 'localhost' para local)
    'PORT': '3306',          # Porta do MySQL, geralmente 3306
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        'charset': 'utf8mb4',
    },
}
```

Verifique a conexão com o banco de dados

```
python manage.py check
```

Crie os arquivos das migrations

```
python manage.py makemigrations
```

Execute as migrations no bancos

```
python manage.py migrate admin --database=default
python manage.py migrate auth --database=default
python manage.py migrate sessions --database=default

python manage.py migrate private_site --database=mysql_db
python manage.py migrate public_site --database=mysql_db

python manage.py migrate private_site --database=mongo_db
python manage.py migrate public_site --database=mongo_db
```

Rode o Faker Data para popular o banco com dados para testes (Use apenas para testes)

```
python manage.py populate_data
```

Rode o projeto

```
python manage.py runserver
```

O DJango irá dar acesso a página pelo ip ```http://127.0.0.1:8000/```

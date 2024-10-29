# Univesp PI 2
Código do projeto integrador 2 usando Django 5.1.2

Crie um ambiente virtual (venv) do python3 

```
python3 -m venv /path/to/new/virtual/environment
```

Faça o acesso do seu venv do python3

```
source /path/to/new/virtual/environment/bin/activate
```

Para mais detalhes acesse [venv](https://docs.python.org/pt-br/3/library/venv.html)

Instalação do DJango Versão 5.1.2

```
python3 -m pip install django==5.1.2
```

Instalação do Faker

```
pip install Faker
```

Instalação do driver mysqlclient

```
pip install mysqlclient
```


* OBS: Caso você receba algum erro na instalação do mysqlclient, instale os pacotes essenciais

```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

Instalação do django-mysql

```
pip install django-mysql
```

* OBS: Se existir algum problema com o uso do mysqlclient, utilize o django-mysql

Faça a instalação do MySQL (Docker)
Faça a instalação do MongoDB (Docker)

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
    'USER': 'root',          # Usuário do banco de dados
    'PASSWORD': 'root',      # Senha do banco de dados
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

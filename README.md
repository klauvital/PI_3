Este projeto foi feito com:

Python 3.10.0
Django 4.0b1


Como rodar o projeto?

1)Clone esse repositório.
  git clone https://github.com/klauvital/PI_3.git
2) Crie um virtualenv com Python 3
  pip install virtualenv
3) Ative o virtualenv  pelo windows
  venv/scripts/activate
4) Instale as dependências
  python manage.py .\requirements.txt
5) Rode as migrações
  python manage.py makemigrations
  --aguarde instalar a pasta migrations e depois
  python manage.py migrate
6)Execute python manage.py cria_grupos



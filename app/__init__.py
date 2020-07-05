from flask import Flask
from flask_sqlalchemy import SQLAlchemy # É um modulo ORM. ORM é uma ferramenta que facilita a criação e comunicação com o banco de dados
from flask_script import Manager # Modulo que muda a forma de execução da ferramenta e adiciona comandos a ela
from flask_migrate import Migrate, MigrateCommand # Modulo que auxilia a migração do banco de dados

app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db)


manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
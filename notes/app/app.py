from flask import Flask
from micawber import bootstrap_basic
from peewee import SqliteDatabase

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SqliteDatabase(app.config['DATABASE'], threadlocals=True)
oembed = bootstrap_basic()





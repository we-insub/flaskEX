import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
print(__name__)
#os.path.abspath 절대경로 명령어

dbfile = os.path.join(basedir, "db.sqlite")
#basedir 폴더에 os.path.join 명령어를 이용해서 db.sqlite 파일로 만들어라,

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+dbfile
app.config['SQLALCHEMY_COMMIT_IN_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    __tablename__ = 'test_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
#id sms 인티저로만들어졌으며,
#이름은 스트링 32최대로 작성이 가능하다.

db.create_all()

@app.route('/')
def hello():
    return 'Hello World!!'
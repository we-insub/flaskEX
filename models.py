from flask_sqlalchemy import SQLAlchemy
#orm형식으로 접근하는법,
db = SQLAlchemy()
#테이블 클래스 마이유저 선언

class MyUser(db.Model):
    __tablename__ = 'myuser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))
    #옆으로 칼럼 만들어서 1은 integer
    #두번쨰는 64개 길이의 의 비번
    #세번째는 아이디 32 길이의 아이디
    #8개의 유저이름
    #테이블 만드는 과
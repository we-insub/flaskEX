import os
from flask import Flask
from flask import render_template
from models import db

app=Flask(__name__)

#슬래쉬 레지스터.html파일을 불러올것이다.
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    print('Hello')
    basedir = os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))
    dbfile = os.path.join(basedir, 'db.sqlite')
    print('file:{}'. format(dbfile))

    app.config['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///' + dbfile
    #데이터베이스를 dbfile 을 쓸거고 sqlite에 있다.
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    #티어 다운은 / 루트에 대한 엑세스를 하게되면 데이터베이스를 중간중간 업데이트가 되어야 한다.
    #웹페이지 , 웹서비스 같은경우는 이벤트에 대해서 업데이트가 되기떄문에
    #특정 페이지에 접근했을때 티어다운이 발생이 됨 그래서 COMMIT 를 이용해서
    #데이터 베이스를 업데이트를 한다 라는 조
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #객체 추정에대한부

    db.init_app(app)
    #초기화를 하
    db.app=app
    #앱하고 연결을 하
    db.create_all()
    app.run(host='127.0.0.1', port = 5000, debug = True)
    #실행을 하는데 아이피는 127.0.0.1 을 사용하고
    #포트번호는 5000번을 하고

    #어떤 요청을 서버에서 클라이언트가 요청을 해서 받는것을 애크라 한다.
    #애크가 오지않았는데, 서버가 종료되었을때, 타임아웃이 걸린다,
    #address 가 사용중입니다 라고 뜨는것,
    #즉 TimeOut 그럴땐 기다리지말고 포트번호 바꿔서 테스트 하면된다.


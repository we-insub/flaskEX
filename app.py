import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db
from models import MyUser
app = Flask(__name__)

@app.route('/register', methods=['GET','POST'])
def hello():
return render_template('hello.html')
if __name__ == "__main__":
    print('hello')
    basedir = os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))
    dbfile = os.path.join(basedir, 'db.sqlite')
    print('file:{}'.format(dbfile))
    # SQLITE Database uri address
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    # True로 설정하면 각 리퀘스트의 끝에 데이터베이스 변동사항을 자동 커밋한다.
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # 개체 수정을 추적하고 신호를 방출한다. 일반적으로 잘 사용하지 않고 추가 메모리가 필요하여 False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='127.0.0.1', port = 5000, debug= True)
def register():
    if request.method == 'POST':
        print(request.method)
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re‐password')

        if (userid and username and password and re_password) and (password == re_password):
            myuser = Myuser()
            myuser.userid = userid
            myuser.username = username
            myuser.password = password
            db.session.add(myuser)
            db.session.commit()

            return redirect('/')
    return render_template('register.html')
@app.route("/", methods=['GET','POST']) # 어떤 주소로 함수를 시작할것이냐.
def hello(): # /에 접근했을때 hello함수 실행
    return "Hello world!"



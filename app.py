import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db
from models import MyUser
app = Flask(__name__)

@app.route('/register', methods=['GET','POST'])
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



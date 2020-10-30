from flask import Flask
app = Flask(__name__)

@app.route("/") # 어떤 주소로 함수를 시작할것이냐.
def hello(): # /에 접근했을때 hello함수 실행
    return "Hello world!"

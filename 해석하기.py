# import 해당 모듈을 모두 가지고온다.
# from module import 해당 모듈내의 해당변수를 가져온다.
from flask import Flask, render_template # flask내에 있는 render_template 가져오기
# render_template 의 키 값을 쌍으로 추가하여 경로 동적내용 템플릿 전달
from gpiozero import LEDBoard # gpio 에서 LED 의 변수를 가져오기
from flask_sqlalchemy import SQLAlchemy # flask_sqlalchemy 에서 SQLAchemy 변수가져오기
import Adafruit_DHT # 온습계인데, 센서이용
import datetime # 기본 날짜와 시간형을 가지고 오기.
now = datetime.datetime.now() # ORM 으로 데이터가 찍히고 소멸되게 ?
# orm형식으로 접근하는법,
db = SQLAlchemy() # ORM 으로 데이터가 찍히고 소멸되게?
# 테이블 클래스 마이유저 선언

app = Flask(__name__) # ?

# leds의 핀번호 정의(BCM 핀번호)
leds = LEDBoard(14, 15, 18) #라즈베리파이의 전원핀번호

# leds의 상태 정보 저장을 위한 데이터 # 빵판에 꽂은 전구의 기본값 0 전원off
led_states = {
    'red': 0,
    'green': 0,
    'yellow': 0
}

@app.route('/') # ip:port에 접속하면 메인으로 보이는 화면, hello world!를 출력하고끝!
def hello():
    return 'Hello World!'

@app.route('/temp')
def temp_hum():
    sensor = Adafruit_DHT.DHT11
    pin = 17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    DHT = {'temp': temperature, 'humi': humidity}
    return render_template('index2.html', **DHT)

# ex) 192.168.1.57:5000/red/0
@app.route('/<color>/<int:state>')
def led_switch(color, state):
    led_states[color] = state
    leds.value = tuple(led_states.values())
    return render_template('index.html', led_states=led_states)

@app.route('/all/<int:state>') #전원은 정수형 1,0이기때문에 INT선언
def all_on_off(state):
    if state is 0: #0 이면 전원 off
        led_states = {
            'red': 0,
            'green': 0,
            'yellow': 0
        }
    elif state is 1: #1 이면 전원 on
        led_states = {
            'red': 1,
            'green': 1,
            'yellow': 1
        }

    leds.value = tuple(led_states.values()) # 튜플값으로 전원 온오프 묶기,
    return render_template('index.html', led_states=led_states)
# 랜더 탬플리트 인덱스.html, led states 로 실행 종료

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

class MyUser(db.Model): # Date Base Table 만드는 것,
    __tablename__ = 'myuser'
    id = db.Column(db.Integer, primary_key=True)
    red = db.Column(db.String(64))
    yellow = db.Column(db.String(32))
    green = db.Column(db.String(8))
    time = db.Column(db.string(30))

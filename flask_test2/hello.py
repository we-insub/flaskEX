from flask import Flask, send_file, render_template, make_response

from io import BytesIO
import numpy as np 
import time
import threading 

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
#################

## remove cache 
from functools import wraps, update_wrapper
from datetime import datetime

def nocache(view):
  @wraps(view)
  def no_cache(*args, **kwargs):
    response = make_response(view(*args, **kwargs))
    response.headers['Last-Modified'] = datetime.now()
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response      
  return update_wrapper(no_cache, view)
###############

app = Flask(__name__, static_url_path='/static', )



def func1():
  while(True):
    time.sleep(5)
    print("hello")
    

def timer_run():
  print('Timer thread running')
  threading.Timer(5.0, timer_run).start()



@app.route('/single')
@nocache
def single():
  return render_template("single_image.html", width=400, height=300)



@app.route('/multi')
@nocache
def multi():
  now = time.localtime()
  strTime = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+str(now.tm_hour)+str(now.tm_min)+str(now.tm_sec)
  print(strTime)
  fig1(4,3)
  fig2(4,3)
  fig3(4,3)

  return render_template("multi_image.html", width=400, height=300)


@app.route('/fig/<int:xsize>_<int:ysize>')
@nocache
def fig(xsize, ysize):
  plt.figure(figsize=(xsize, ysize))
  xs = [0,1,2,3,4]
  ys = [0,1,4,9,16]
  plt.plot(xs,ys)
  """
  file로 저장하는 것이 아니라 binary object에 저장해서 그대로 file을 넘겨준다고 생각하면 됨
  """
  img1 = BytesIO()
  plt.savefig(img1, format='png', dpi=300)
  img1.seek(0)## object를 읽었기 때문에 처음으로 돌아가줌
  return send_file(img1, mimetype='image/png')


#@app.route('/fig1/<int:xsize>_<int:ysize>')
#@nocache
def fig1(xsize, ysize):
  plt.figure(figsize=(xsize, ysize))
  xs = [0,1,2,3,4]
  ys = [0,1,4,9,16]
  plt.plot(xs,ys)
  """
  file로 저장하는 것이 아니라 binary object에 저장해서 그대로 file을 넘겨준다고 생각하면 됨
  """
  #img1 = BytesIO()
  plt.savefig('static/img1.png', format='png', dpi=300)
  #img1.seek(0)## object를 읽었기 때문에 처음으로 돌아가줌
  #return send_file('img1.png', mimetype='image/png')

#@app.route('/fig2/<int:xsize>_<int:ysize>')
#@nocache
def fig2(xsize, ysize):
  plt.figure(figsize=(xsize, ysize))
  y = [5,3,7,10,9,5,3.5,8]
  x = range(len(y))
  plt.bar(x,y, width=0.7, color="blue")
  """
  file로 저장하는 것이 아니라 binary object에 저장해서 그대로 file을 넘겨준다고 생각하면 됨
  """
  #img2 = BytesIO()
  plt.savefig('static/img2.png', format='png', dpi=300)
  #img2.seek(0)## object를 읽었기 때문에 처음으로 돌아가줌
  #return send_file('img2, mimetype='image/png')

#@app.route('/fig3/<int:xsize>_<int:ysize>')
#@nocache
def fig3(xsize, ysize):
  plt.figure(figsize=(xsize, ysize))

  # 폰트 설정
  mpl.rc('font', family='NanumGothic')
  # 유니코드에서  음수 부호설정
  mpl.rc('axes', unicode_minus=False)
  xs = [0,1,2,3,4]
  ys = [0,1,4,9,16]
  plt.title("'rs--' 스타일의 plot ")
  plt.plot(xs,ys,'rs--')
  """
  file로 저장하는 것이 아니라 binary object에 저장해서 그대로 file을 넘겨준다고 생각하면 됨
  """


  img3 = BytesIO()
  plt.savefig('static/img3.png', format='png', dpi=300)
  #img3.seek(0)## object를 읽었기 때문에 처음으로 돌아가줌
  #return send_file(img3, mimetype='image/png')

#################
if __name__ == '__main__':
  threading.Thread(target=func1).start()
  
  # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)

from flask import Flask, url_for, render_template
app = Flask(__name__)

# 라우팅(route) URL을 특정 함수에 연결하는 작업
# URL/ 로 접속했을 때 hello_world() 함수를 실행한다. (http://127.0.0.1:5000/)
@app.route('/')
def hello_world():
    return 'Hello, World'

# 터미널에 flask --app 파일이름 run을 하면 플라스크 개발 서버를 시작한다.

# URL 변수 <변수명> 형태로 사용가능. 
# 해당 변수는 라우팅으로 연결될 함수의 인자로 선언하여 값을 받을 수 있다.
# http://127.0.0.1:5000/user/mir 주소로 접속하면 "User : mir" 문자열이 표시된다.
@app.route('/user/<username>')
def user(username):
    return f'User : {username}'

# url_for() 함수는 특정 함수에 매핑된 URL을 반환한다.
# 함수 파라미터 전달은 '변수=변수값' 형태로 전달한다.
# _scheme는 URL에 사용될 프로토콜을 지정한다.
# _external을 True로 설정하면 전체 URL을 생성한다.
@app.route('/userURL/<name>')
def userURL(name):
    user_url = url_for('user', username=f'{name}', _scheme='http', _external=True)
    return f'User URL : {user_url}'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/brandList')
def brand():
    brandList = ['Nike', 'Adidas', 'HOKA', 'Lulu Lemon', 'Asics', 'New Balance']
    return render_template('brandList.html', brandList=brandList)

@app.route('/message')
def message():
    return render_template('message.html')

if __name__ == '__main__':
    app.run(debug=True)
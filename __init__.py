from flask import Flask, render_template, request, make_response
import urllib.request, urllib.parse, urllib.error, json

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello World - Subhasis Martha"

@app.route('/authors')
def authors():
    url1 = 'https://jsonplaceholder.typicode.com/users'
    uh1 = urllib.request.urlopen(url1)
    data1 = json.loads(uh1.read().decode('utf-8'))
    url2 = 'https://jsonplaceholder.typicode.com/posts'
    uh2 = urllib.request.urlopen(url2)
    data2 = json.loads(uh2.read().decode('utf-8'))
    for users in data1:
        c = 0
        for posts in data2:
            if users['id'] == posts['userId']:
                c = c + 1;
        users['count'] = c
    return render_template('authors.html', data1 = data1)

@app.route('/setcookie')
def setcookie():
    resp = make_response(render_template('setcookie.html'))
    if 'username' not in request.cookies:
        resp.set_cookie('username', 'Subhasis Martha')
    if 'age' not in request.cookies:
        resp.set_cookie('age', '19')
    return resp

@app.route('/getcookies')
def getcookies():
    username = request.cookies.get('username')
    age = request.cookies.get('age')
    return render_template('getcookies.html', username = username, age = age)

@app.route('/robots.txt')
def robots():
    return render_template('error.html')

@app.route('/html')
def html():
    return render_template('random.html')

@app.route('/input', methods=['GET','POST'])
def input():
    if request.method == 'POST':
        data = request.form['log']
        print('Entered text: ' + data)
        return render_template('input.html', data=data)
    return render_template('input.html')

if __name__ == "__main__":
    app.run()

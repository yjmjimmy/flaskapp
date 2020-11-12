from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def firstRequest():
    return(render_template('home.html'))

@app.route('/info', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('info.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    API_KEY = 'b9e65cc056232a28aea67900bf212713'
    city = request.args.get('q')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    temperature = response.json()
    weather = temperature["weather"][0]['description']

    return weather

@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    myobj = {'1': 'Hello world'}
    x = request.post('http://127.0.0.1:5000/thirdrequest' , data = myobj)
    return x
    #reqData = request.form
    #return('You just posted.... ' + str(reqData))

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language is {}</h1>
                    <h1>The framework is {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                Languange: <input type="text" name="language"><br>
                Framework: <input type="text" name="framework"><br>
                <input type="submit" value="Submit"><br>
            </form>'''

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import requests
import json


def read_data():
    url = 'https://api.ibb.gov.tr/ispark/Park'
    response = requests.get(url)
    park_data = json.loads(response.text)
    return park_data


app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():

    park_data = read_data()
    a = list({v['Ilce']: v for v in park_data}.values())
    ilceler = {}
    for data_ in a:
        if data_['Ilce'] not in ilceler:
            ilceler[data_['Ilce']] = data_['Ilce']

    a = list({v['ParkID']: v for v in park_data}.values())

    park_yerleri = {}
    for data_ in a:
        if data_['ParkID'] not in park_yerleri:
            park_yerleri[data_['ParkID']] = data_['ParkID']
            park_yerleri[data_['ParkAdi']] = data_['ParkAdi']

    return render_template('index.html', title='Home', park_data=park_data, ilceler=ilceler, park_yerleri=park_yerleri)

if __name__ == '__main__':
    app.run(debug=True)

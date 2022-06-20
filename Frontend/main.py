from distutils.log import debug
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('models/random_forest_model.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['post'])
def data():
    dept_city = int(request.form.get('departure city'))
    dept_date = int(request.form.get('departure date'))
    duration = int(request.form.get('duration'))
    weekday = int(request.form.get('weekday'))
    dept_hours = int(request.form.get('departure hours'))
    dept_airline = int(request.form.get('departure airline'))
    arrival_airline = int(request.form.get('arrival airline'))
    flight_time = int(request.form.get('flight time'))
    dept_minutes = int(request.form.get('departure minutes'))
    arrival_hours = int(request.form.get('arrival hours'))
    price = int(request.form.get('price'))
    result = model.predict([[dept_city, dept_date, duration, weekday, dept_hours, dept_airline, arrival_airline, 
                                flight_time==1, flight_time==2, flight_time==0, flight_time==3, dept_minutes, arrival_hours, price]])
    print(result)

    return render_template('predict.html', data=int(result[0]))


app.run(debug=True)
from flask import Blueprint, render_template

from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')


def get_data():
    db = get_db()

    current_data = db.execute('SELECT a.humidity AS sensor_0_hum, b.humidity AS sensor_1_hum, a.temp AS sensor_0_temp, b.temp AS sensor_1_temp, a.sensor AS sensor_0, b.sensor AS sensor_1, a.date FROM environment a inner join environment b ON a.date = b.date WHERE a.sensor = 0 AND b.sensor = 1').fetchone()
    time = current_data['date']
    temp = int(current_data['sensor_0_temp']) + int(current_data['sensor_1_temp']) / 2
    hum = int(current_data['sensor_0_hum']) + int(current_data['sensor_1_hum']) / 2

    return time, temp, hum


@bp.route('/', methods=['GET'])
def home():
    time, temp, hum = get_data()
    templateData = {
        'time': time,
        'temp': temp,
        'hum': hum
    }

    return render_template('index.html', **templateData)
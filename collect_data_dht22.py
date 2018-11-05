import datetime
import os
import time
import sqlite3
import Adafruit_DHT

db_path = os.path.join(os.getcwd(), 'instance/pi_kiln.sqlite')
sampleFreq = 60  # time in seconds


# get data from DHT sensor
def getDHTdata():
    DHT22Sensor = Adafruit_DHT.DHT22
    DHTpin = 16
    hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)

    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp, 1)
    return temp, hum


# log sensor data on database
def logData(temp, hum):
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()

    cur_time = datetime.datetime.now()
    sensor = "1"
    print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temp * 1.8 + 32, hum))
    curs.execute("INSERT INTO environment (humidity, temp, sensor, date) VALUES (?,?,?,?)", (temp * 1.8 + 32, hum, sensor, cur_time))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    while True:
        temp, hum = getDHTdata()
        logData(temp, hum)
        time.sleep(sampleFreq)
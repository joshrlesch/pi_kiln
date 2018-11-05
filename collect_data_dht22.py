import datetime
import time
import sqlite3
import Adafruit_DHT

dbname = 'sensorsData.db'
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
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()

    cur_time = datetime.datetime.now()
    sensor = "1"
    curs.execute("INSERT INTO environment (humidity, temp, sensor, date) VALUES (?,?,?,?)", (temp, hum, sensor, cur_time))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    while True:
        temp, hum = getDHTdata()
        logData(temp, hum)
        time.sleep(sampleFreq)
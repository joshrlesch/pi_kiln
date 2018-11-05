import datetime
import sqlite3
from random import randint
from time import sleep

db = sqlite3.connect("/Users/josh.lesch/github/open_source_projects/pi_kiln/instance/pi_kiln.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.row_factory = sqlite3.Row

for _ in range(100):
    time = datetime.datetime.now()
    for i in range(2):
        hum = randint(0, 100)
        temp = randint(0, 200)
        db.execute("INSERT INTO environment (humidity, temp, sensor, date) VALUES (?,?,?,?)",
                   (hum, temp, i, time))
        db.commit()
        print("Saving temp:{}; hum:{}; sensor:{}; date:{}".format(temp,hum,i,time))

    sleep(10)

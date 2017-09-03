import os
from datetime import datetime
from flask import Flask, jsonify
from pytz import timezone
from tzlocal import get_localzone

app = Flask(__name__)

fmt = '%Y-%m-%dT%H:%M:%S%z'

@app.route('/api/v1.0/time', methods=['GET'])
def get_time():
    my_zone = get_localzone()
    zones = [my_zone,
             timezone('Australia/Sydney'),
             timezone('Singapore'),
             timezone('Europe/Zurich'),
             timezone('Europe/London'),
             timezone('US/Eastern'),
             timezone('US/Pacific')]
    now = my_zone.localize(datetime.now())
    results = {zone.zone: now.astimezone(zone).strftime(fmt) for zone in zones}
    return jsonify(results)

@app.route('/api/v1.0/info', methods=['GET'])
def get_info():
    uname_data = list(os.uname())
    tz = str(get_localzone().zone)
    uname_data.append(tz)
    uname_fields = ['sysname', 'nodename', 'release', 'version', 'machine', 'timezone']
    results = dict(zip(unname_fields, uname_data))
    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

import flask
import subprocess
from pip import main
HOST=""
USERNAME=""
PASSWORD=""
app = flask.Flask(__name__)

def get_creds():
    """Parses server host, username and password from a conf file in current directory"""
    with open("creds.txt", "r") as cred_file:
        global HOST, USERNAME, PASSWORD
        all_creds = cred_file.read().split("\n")
        HOST = all_creds[0]
        USERNAME = all_creds[1]
        PASSWORD = all_creds[2]


def get_temperature():
    """Gets the current temperature of the system and returns it to the caller of the function"""
    out = subprocess.Popen(f"ipmitool -I lanplus -H {HOST} -U {USERNAME} -P {PASSWORD} sdr type temperature | grep degrees | cut -d ' ' -f 16", shell=True, stdout=subprocess.PIPE).stdout.read()
    return out.decode('utf-8').split("\n")[0]

def set_fan_speed(speed):
    """Sets the parsed speed as the server''s fan speed"""
    badChars = ["&", "&&", "`", "``", "|", "||", ";", "os.", "\n", "0x0a", " "]
    for element in speed:
        if element in badChars:
            return "ERROR!"
    if int(speed) <= 60 and int(speed) >=0:
        out = subprocess.Popen(f"ipmitool -I lanplus -H {HOST} -U {USERNAME} -P {PASSWORD} raw 0x30 0x30 0x02 0xff 0x{speed}", shell=True, stdout=subprocess.PIPE).stdout.read()
        return speed
    else:
        return "ERROR!"


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Dell powerEdge R710 Fan Controller API by Nee</h1>'''


@app.route('/get-temperature', methods=['GET'])
def get_server_temperature():
    return '''<h1>Current Server Temperature -> {}</h1>'''.format(get_temperature())


@app.route('/set-fan-speed/<speed>', methods=['GET'])
def set_server_fan_speed(speed):
    result = set_fan_speed(speed)
    if result == "ERROR!":
        return '''<h1>Error! Please enter a speed inbetween 0 and 60'''
    else:    
        return '''<h1>Fan speed has been set to {}</h1>'''.format(set_fan_speed(speed))


def main():
    get_creds()
    app.run(host='0.0.0.0', port=10001)

if __name__ == "__main__":
    main()
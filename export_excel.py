
import requests
import configparser
import sys, os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    configfilename = os.path.abspath(os.path.dirname(sys.argv[0])) + '\export_excel.ini'
    config = configparser.ConfigParser()

    config.read(configfilename)
    hostname = config['DEFAULT']['hostname']
    login = config['DEFAULT']['login']
    password = config['DEFAULT']['password']
    filename = config['DEFAULT']['filename']

    # auth_data = "{\"action\":\"login\",\"data\":{\"login\":\"" + login + "\",\"password\":\"" + password + "\"}}"
    # print(auth_data)
    auth_data = '{"action":"login","data":{"login":"' + login + '","password":"' + password + '"}}'
    print(auth_data)

    req = requests.Session()
    responce = req.post(hostname + '/action/login', data=auth_data)
    c = req.cookies
    h = req.headers
    excel_filename = '{"data":{"filename":"%s"}}' % (filename)

    responce = req.post(hostname + '/action/export/production_state', cookies=c, headers = h)
    print(responce.text)

    responce = req.get(hostname + '/action/logout', cookies=c, headers=h)
    print('Done.')
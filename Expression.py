import configparser
import requests

def GetFace(img_url, key, api_url):
    try:
        with open(img_url, 'rb') as f:
            img = f.read()
    except:
        print("ファイルが存在しません")
        return False
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key
    }
    res = requests.post(url = api_url, headers=headers, data=img)
    return res.json()

def GetDegreeOfSurprise(img):
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')
    KEY = config_ini['FaceAPI']['KEY']
    URL = config_ini['FaceAPI']['URL']
    res = GetFace(img_url=img, key=KEY, api_url=URL)
    if not res:
        json = {"result": False}
    else:
        json = {"result": True}
    return json
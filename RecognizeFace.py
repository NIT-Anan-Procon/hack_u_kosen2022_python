import configparser

import requests


def GetFace(key, api_url):
    try:
        with open("images/img1.jpg", "rb") as f:
            img = f.read()
    except:
        print("ファイルが存在しません")
        return False
    headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": key
    }
    res = requests.post(url=api_url, headers=headers, data=img)
    return res.json()


def RecognizeFace():
    config_ini = configparser.ConfigParser()
    config_ini.read("config.ini", encoding="utf-8")
    KEY = config_ini["FaceAPI"]["KEY"]
    URL = config_ini["FaceAPI"]["URL"]
    res = GetFace(key=KEY, api_url=URL)
    if res:
        json = {"result": True}
    else:
        json = {"result": False}
    return json

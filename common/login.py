# coding=utf-8
import json
import unittest

import requests
from framework import readConfigFile
from framework.logger import Logger


config = readConfigFile.ReadConfig()
mylog = Logger(logger="test_login").getlog()
def test_Login_token():
    """
    登录
    :return:
    """
    host = config.get_http("browserName")
    url = host + "/api/v1/user/account/login"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",

    }

    payload = "username=15074709134&password=123456&captcha=&systemCode=kuaishou&loginType=1&networkType=2G&udid=867194040464771&deviceId=973526c9b75c1323&deviceName=MI%206X&deviceModel=MI%206X&vendor=xiaomi&operatingSystem=8.1.0&appVersion=2.0.4&deviceResolution=1080*2030&imei=867194040464771&pushId=1104a89792ed4f4b20e&undefined="

    response = requests.post(url, data=payload, headers=headers, verify=False)
    print(response.text)
    assert response.json()['message'], "成功"
    assert response.json()['success'], True
    assert response.json()['code'], 1



    # print(token)
    # print(response.json()['response'])
    return response.json()['response']

def test_Login_mobile_erro():
    """
    用户名错误
    :return:
    """
    host = config.get_http("browserName")
    url = host + "/api/v1/user/account/login"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",

    }

    payload = "username=1507470913&password=123456&captcha=&systemCode=kuaishou&loginType=1&networkType=2G&udid=867194040464771&deviceId=973526c9b75c1323&deviceName=MI%206X&deviceModel=MI%206X&vendor=xiaomi&operatingSystem=8.1.0&appVersion=2.0.4&deviceResolution=1080*2030&imei=867194040464771&pushId=1104a89792ed4f4b20e&undefined="

    response = requests.post(url, data=payload, headers=headers, verify=False)
    print(response.text)
    assert response.json()['message'], "用户名或密码错误"

    assert response.json()['code'], 2104


def test_Login_password_erro():
    """
    密码错误
    :return:
    """
    host = config.get_http("browserName")
    url = host + "/api/v1/user/account/login"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",

    }

    payload = "username=1507470913&password=123456&captcha=&systemCode=kuaishou&loginType=1&networkType=2G&udid=867194040464771&deviceId=973526c9b75c1323&deviceName=MI%206X&deviceModel=MI%206X&vendor=xiaomi&operatingSystem=8.1.0&appVersion=2.0.4&deviceResolution=1080*2030&imei=867194040464771&pushId=1104a89792ed4f4b20e&undefined="

    response = requests.post(url, data=payload, headers=headers, verify=False)
    assert response.json()['message'], "用户名或密码错误"

    assert response.json()['code'], 2104


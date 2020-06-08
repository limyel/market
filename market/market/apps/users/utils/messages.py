import requests
import json


class Message:

    def __init__(self, api_key='6fb38cc317395a45b438fd1c53e72b93'):
        self.api_key = api_key
        self.url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def sendMessage(self, code, mobile):
        data = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': F'【林新煌】您的验证码是{code}。如非本人操作，请忽略本短信'
        }
        response = requests.post(self.url, data=data)
        res_dict = json.loads(response.text)
        print(res_dict)
        return res_dict
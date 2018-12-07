import random
import hashlib
import urllib
from urllib import parse, request
import json
from langdetect import detect


appid = '20181206000244574'
secretKey = 'PiCc_tvV1Dm0KBWD4keX'
url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

class Translator():
    def __init__(self):
        self.appid = '20181206000244574'
        self.secretKey = 'PiCc_tvV1Dm0KBWD4keX'
        self.url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        self.tolang=''
        self.from_lang=''


    def detect_language(self,text):
        from_lang = detect(text)
        self.from_lang=from_lang
        return self.from_lang

    def set_tolang(self,des_lan):
        self.tolang=des_lan
        return self.tolang

    def translateBaidu(self,text,f,t):
        salt = random.randint(32768, 65536)
        sign = self.appid + text + str(salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        url = self.url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + f + '&to=' + t + \
        '&salt=' + str(salt) + '&sign=' + sign
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        data = json.loads(content)
        result = str(data['trans_result'][0]['dst'])
        return result


if __name__ == '__main__':
    a=Translator()
    word = input()
    tolan = input()
    b=a.translateBaidu(word,'auto', tolan)
    print(b)


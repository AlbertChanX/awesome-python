import requests
from time import sleep
url = 'http://api.lianqu.top/api/v1/verifycodes/register'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'}
def send(phone):
    data = {'mobile': phone}
    res = requests.post(url, data=data, headers=headers)
    print(res.text)

if __name__ == '__main__':
    for i in range(10):
        send('13588888888')
        sleep(30) 

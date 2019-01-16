import time

import requests


class SMSSend_seven(object):
    """易法通短信接口"""

    def __init__(self, mobile):
        self.url = "http://www.yifatong.com/Customers/gettcode?rnd="
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Referer': 'http://www.yifatong.com/Customers/registration?url=',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep - alive'
        }
        self.mobile = mobile

    def get_response(self, ip):
        time_now = time.time()
        time_new = ("%0.3f" % time_now)

        # print(time_new)

        url = self.url + time_new + "&mobile=" + self.mobile

        proxies = {
            'http': 'http://{}'.format(ip),
            'https': 'http://{}'.format(ip),
        }

        try:
            print(proxies)
            response = requests.get(url=url, headers=self.header, proxies=proxies)
            print(response.content)
            print("{}:{}>>>易法通短信接口 发送成功".format(url, self.mobile))
        except Exception:
            print("{}:{}>>>易法通短信接口 发送失败".format(url, self.mobile))

    # 验证ip
    def find_ip(self, proxies=None):
        # print(proxies)
        url = "http://pv.sohu.com/cityjson?ie=utf-8"
        # print("原有IP:   " + requests.get(url).text)
        fileHandle = open('test.txt', 'w')

        for i in range(0, len(proxies)):
            ip_info = proxies[i]
            try:
                print(ip_info)
                print("原有IP:   " + requests.get(url, proxies=proxies).text)
                fileHandle.write(ip_info)
            except Exception:
                print("ss")

    def run(self):
        self.get_response()

    def setMb(self, mobile):
        self.mobile = mobile;


if __name__ == "__main__":
    s = SMSSend_seven("1222");
    proxies = [{"http": "1.198.73.11:9999"}]
    s.find_ip(proxies);

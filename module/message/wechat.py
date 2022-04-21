import json
import datetime
import requests

CORP_ID = "wwdace9a993cbd606d"
SECRET = "LJy24acAwDSwRiFqCutk0wBlr9Nxb_HgfocdWJoSswg"


class WeChatPub:
    s = requests.session()

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={SECRET}"
        rep = self.s.get(url)
        if rep.status_code != 200:
            print("request failed.")
            return
        return json.loads(rep.content)['access_token']

    def send_msg(self, content):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
        header = {
            "Content-Type": "application/json"
        }
        form_data = {
            "touser": "@all",
            "toparty": " PartyID1 | PartyID2 ",
            "totag": " TagID1 | TagID2 ",
            "msgtype": "textcard",
            "agentid": 1000002,
            "textcard": {
                "title": "服务异常告警",
                "description": content,
                "url": "URL",
                "btntxt": "更多"
            },
            "safe": 0
        }
        rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
        if rep.status_code != 200:
            print("request failed.")
            return
        return json.loads(rep.content)


if __name__ == '__main__':
    wechat = WeChatPub()
    now = datetime.datetime.now()
    timenow = now.strftime('%Y年%m月%d日 %H:%M:%S')
    wechat.send_msg(
        f"<div class=\"gray\">{timenow}</div> <div class=\"normal\">阿里云 cookie 已失效</div><div class=\"highlight\">请尽快更换新的 cookie</div>")

import requests
import time
from scapy.all import *
from scapy.layers.inet import IP, UDP


def packet_callback(packet):
    try:
        raw = packet[Raw]
        # print(hexdump(raw))
        aa = hexdump(raw,dump=True)
        # print(str(aa))
        if '02 00 48' in str(aa):
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("+++++++++++++++++++++++++++++++++++++++")
            print("[*] your_ip:%s"%packet[IP].src)
            print("[*] your_port:%s"%packet[UDP].sport)

            print("--------------------------------")
            print("[*] woof_ip:%s"%packet[IP].dst)

            print("[*] woof_port:%s"%packet[UDP].dport)
            print("+++++++++++++++++++++++++++++++++++++++")

    # print(packet.show())
        # return
    except Exception as e :
        pass
        # print(e)
    # print(packet.show())


if __name__ == '__main__':
    qq_number = input('请输入QQ号：')
    api_url = f'https://zy.xywlapi.cc/qqcx?qq={qq_number}'
    infos = requests.get(api_url).json()
    print(f'''通过{qq_number}查询到的个人信息如下：
    密保手机号：{infos.get("phone")},
    号码归属地：{infos.get("phonediqu")},
    lol信息：{infos.get("lol")},
    微博UID：{infos.get("wb")}
    ''')
    # #开启嗅探
    # sniff(prn=packet_callback, store=0)
    sniff(filter='src host 192.168.128.5 && dst port 80', prn=lambda x: x.summary())
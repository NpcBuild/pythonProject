# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import time
import execjs
def getUrl(fscode):
    head = 'http://fund.eastmoney.com/pingzhongdata/'
    tail = '.js?v='+ time.strftime("%Y%m%d%H%M%S",time.localtime())
    return head+fscode+tail
#根据基金代码获取净值
def getWorth(fscode):
    content = requests.get(getUrl(fscode))
    jsContent = execjs.compile(content.text)
    name = jsContent.eval('fs_name')
    code = jsContent.eval('fs_code')
    #单位净值走势
    netWorthTrend = jsContent.eval('Data_netWorthTrend')
    #累计净值走势
    ACWorthTrend = jsContent.eval('Data_ACWorthTrend')
    netWorth = []
    ACWorth = []
    for dayWorth in ACWorthTrend[::-1]:
        netWorth.append(dayWorth['y'])
    for dayACWorth in ACWorthTrend[::-1]:
        ACWorth.append(dayACWorth[1])
    print(name,code)
    return netWorth,ACWorth
def getAllCode():
    url = 'http://fund.eastmoney.com/js/fundcode_search.js'
    content = requests.get(url)
    jsContent = execjs.compile(content.text)
    rawData = execjs.eval('r')
    allCode = []
    for code in rawData:
        allCode.append(code[0])
    return allCode


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    allCode = getAllCode()
    print(allCode)
    # netWorthFile = open('./netWorth.csv', 'w')
    # ACWorthFile = open('./ACWorth.csv', 'w')
    # for code in allCode:
    #     try:
    #         netWorth,ACWorth = getWorth(code)
    #     except:
    #         continue
        # if len(netWorth<=0 or len(ACWorth)<0):
            
        # print(code +"'s' data is empty.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

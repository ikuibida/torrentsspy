import requests, bs4, re

def undotIPv4 (dotted):
    return sum (int (octet) << ( (3 - i) << 3) for i, octet in enumerate (dotted.split ('.') ) )

def dotIPv4 (addr):
    return '.'.join (str (addr >> off & 0xff) for off in (24, 16, 8, 0) )

def rangeIPv4 (start, stop):
    for addr in range (undotIPv4 (start), undotIPv4 (stop) ):
        yield dotIPv4 (addr)



def getinfo(ip):
    s=requests.get('https://iknowwhatyoudownload.com/ru/peer/?ip='+ip)
    s.encoding = s.apparent_encoding
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.torrent_files')
    for x in p:
        z=x.getText()
        print(u''+z.strip())

for x in rangeIPv4 ('92.55.160.50', '92.55.160.60'):
    print('IP: '+x+'\n'+'--------------')
    getinfo(x)
    print('-------------------')



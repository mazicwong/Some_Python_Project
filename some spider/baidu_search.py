import requests

try:
    kv = {'wd': 'Python'}
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.encoding)
    r.raise_for_status()
    r.enconding = r.apparent_encoding
    print(r.enconding)
    print("length of the whole source code : %s " %len(r.text))
except:
    print( "there must be a wrong")

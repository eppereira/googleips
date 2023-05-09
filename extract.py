import json, urllib3



urls = ["https://www.gstatic.com/ipranges/goog.json"]
arquivo = open('enderecos', 'a')
for u in urls:
    print(u)
    response = urllib3.request("GET", u)
    dados = json.loads(response.data.decode('utf-8'))
    prefixos = dados["prefixes"]

    for p in prefixos:
        arquivo.write(p["ipv4Prefix"]+'\n')
        # print(p["ipv4Prefix"])

arquivo.close
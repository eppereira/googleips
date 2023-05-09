import json, urllib3
 
urls = ["https://www.gstatic.com/ipranges/goog.json","https://www.gstatic.com/ipranges/cloud.json"]
arquivo = open('enderecos', 'a')
for u in urls:
    response = urllib3.request("GET", u)
    dados = json.loads(response.data.decode('utf-8'))
    prefixos = dados["prefixes"]

    for p in prefixos:
        if "ipv4Prefix" in p:
            arquivo.write(p["ipv4Prefix"]+'\n')

arquivo.close
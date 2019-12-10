temp = {}
with open('arabic small talk responses.csv') as raw:
    for x in raw:
        item = x.split(';')
        if item[0] in temp.keys():
            temp[item[0]].append(item[1])
        else:
            temp[item[0]] = [item[1]]

    import json
    with open('response.json') as response:
        res = json.load(response)
        for t in temp:
            try:
                res[t]['ar']['content']['elements'] = temp[t]
            except:
                pass
        
        with open('response_new.json', 'wb') as wjson:
            txt = json.dumps(res, indent=3, ensure_ascii = False)
            wjson.write(txt.encode())

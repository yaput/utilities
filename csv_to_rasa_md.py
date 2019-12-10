res = {}
with open('alain_nlu_arabic_latest.csv') as raw:
    for x in raw:
        item = x.split(';')
        if item[0] in res.keys():
            res[item[0]].append(item[1])
        else:
            res[item[0]] = [item[1]]

with open('main_ar.md', 'w+') as final:
    for key in res:
        final.write("## intent:{}".format(key))
        final.write('\n')
        for val in res[key]:
            final.write('- {}'.format(val))



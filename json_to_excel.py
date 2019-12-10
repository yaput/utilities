import json
from xlwt import Workbook
wb = Workbook()
s1 = wb.add_sheet('Sheet 1')
with open('response.json') as r:
    r_json = json.load(r)
    row = 0
    for i in r_json:
        lang = ''
        if 'en' in r_json[i].keys():
            lang = 'en'
        else:
            lang = 'ar'
        if r_json[i][lang]['content']['type'] == "text":
            ar = ""
            if 'ar' in r_json[i].keys():
                ar = r_json[i]['ar']['content']['elements'][0] if len(r_json[i]['ar']['content']['elements']) > 0 else ""
            try:
                s1.write(row, 0, i)
                s1.write(row, 1, r_json[i][lang]['content']['elements'][0] if len(r_json[i]['en']['content']['elements']) > 0 else "")
                s1.write(row, 2, ar)
            except Exception as e:
                pass
        elif r_json[i][lang]['content']['type'] == "quickreplies":
            ar = ""
            if 'ar' in r_json[i].keys():
                ar = r_json[i]['ar']['content']['elements'][0] if len(r_json[i]['ar']['content']['elements']) > 0 else ""
            try:
                s1.write(row, 0, i)
                s1.write(row, 1, json.dumps(r_json[i][lang]['content']['elements'][0]) if len(r_json[i]['en']['content']['elements']) > 0 else "")
                s1.write(row, 2, json.dumps(ar, ensure_ascii=False))
            except Exception as e:
                pass
        row+=1

    wb.save('response.xls')
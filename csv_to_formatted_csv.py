import csv
check = []
new_list = []
temp_list = []
# with open('a.csv') as a:
#     lines = csv.reader(a)
#     for l in lines:
#         if l[0] not in check:
#             check.append(l[0])
#             new_list.append(l)

# with open('b.csv', 'w') as b:
#     c = csv.writer(b, dialect='excel')
#     c.writerows(new_list)

# for x in [1,2,3,4,5]:
#     with open('%s_AR.csv' % str(x)) as c:
#         lines = csv.reader(c)
#         for l in lines:
#             if l[0] not in check:
#                 check.append(l[0])
#                 new_list.append(l)

# with open('AR.csv', 'w') as ar:
#     r = csv.writer(ar, dialect='excel')
#     r.writerows(new_list) 

with open('b.csv') as en, open('products.csv', 'w') as products:
    for enl in csv.reader(en):
        with open('AR.csv') as ar:
            for arl in  csv.reader(ar):
                temp_list = []
                if (enl[0].upper().strip() == arl[0].upper().strip()) and (arl[0] not in check):
                    check.append(arl[0])
                    temp_list = enl[0:16]
                    temp_list.append(arl[3])
                    temp_list.append(arl[7])
                    temp_list.append(arl[8])
                    try:
                        temp_list.append(enl[16])
                    except:
                        temp_list.append("")
                    try:
                        temp_list.append(arl[16])
                    except:
                        temp_list.append("")
                    new_list.append(temp_list)

    pwrite = csv.writer(products, dialect='excel')
    pwrite.writerows(new_list)

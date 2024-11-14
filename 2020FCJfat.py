import csv
import json
import html
filename = './csv/FCJ2020fat.csv'
outputname = './output/2020FCJfat.json'


def isfloat(_s):
    try:
        _f = round(float(_s), 4)
    except ValueError:
        return 0
    else:
        return _f


with open(filename, encoding='utf8', newline='') as f:
    with open(outputname, "w", encoding='utf8', newline='') as p:
        csvreader = csv.reader(f)
        _dicts = []
        for row in csvreader:
            _dict = {
                "name": row[3],
                "description": "日本食品標準成分表2020年版(八訂)" +
                "_FCJ="+row[1]+"_ "+row[62],
                "unit": 100,
                "saturated_fat": isfloat(row[8]),
                "n3": isfloat(row[11]),
                "DHA_EPA": isfloat(row[60]),
                "n6": isfloat(row[12]),
            }
            _dicts.append(_dict)
        p.write(json.dumps(_dicts, ensure_ascii=False,))

"(id,name,tag,description,userid,user,passhash,timestamp,"
"unit,cost,carbo,fiber,protein,fat,saturated_fat,n3,DHA_EPA,n6,"
"ca,cl,cr,cu,i,fe,mg,mn,mo,p,k,se,na,zn,va,vb1,vb2,vb3,vb5,vb6,vb7,"
"vb9,vb12,vc,vd,ve,vk,colin,kcal)"

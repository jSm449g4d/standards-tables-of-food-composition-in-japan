import csv
import json
import html
filename = './csv/FCJ2020fat.csv'
outputname = './output/FCJ2020fat.json'


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
            _tag = ""
            match int(row[0]):
                case 1:
                    _tag = "穀類"
                case 2:
                    _tag = "いも及びでん粉類"
                case 3:
                    _tag = "砂糖及び甘味類"
                case 4:
                    _tag = "豆類"
                case 5:
                    _tag = "種実類"
                case 6:
                    _tag = "野菜類"
                case 7:
                    _tag = "果実類"
                case 8:
                    _tag = "きのこ類"
                case 9:
                    _tag = "藻類"
                case 10:
                    _tag = "魚介類"
                case 11:
                    _tag = "肉類"
                case 12:
                    _tag = "卵類"
                case 13:
                    _tag = "乳類"
                case 14:
                    _tag = "油脂類"
                case 15:
                    _tag = "菓子類"
                case 16:
                    _tag = "し好飲料類"
                case 17:
                    _tag = "調味料及び香辛料類"
                case 18:
                    _tag = "調味済み流通食品類"
                    
            _dict = {
                "name": row[3],
                "tag": _tag,
                "description": "日本食品標準成分表2020年版(八訂)" +
                " _FCJ="+row[1]+"_ "+row[62],
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

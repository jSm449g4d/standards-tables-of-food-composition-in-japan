import csv
import json
import html
filename = './csv/FCJ2025human.csv'
outputname = './output/FCJ2025human.json'


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
            if (row[0]=="name"): continue
            _dict = {
                "name": row[0],
                "tag": row[1],
                "description": row[2],
                "unit": isfloat(row[3]),
                "carbo": isfloat(row[4]),
                "fiber": isfloat(row[5]),
                "protein": isfloat(row[6]),
                "fat": isfloat(row[7]),
                "saturated_fat": isfloat(row[8]),
                "n3": isfloat(row[9]),
                "DHA_EPA": isfloat(row[10]),
                "n6": isfloat(row[11]),
                "ca": isfloat(row[12]),
                "cl": isfloat(row[13]),
                "cr": isfloat(row[14]),
                "cu": isfloat(row[15]),
                "i": isfloat(row[16]),
                "fe": isfloat(row[17]),
                "mg": isfloat(row[18]),
                "mn": isfloat(row[19]),
                "mo": isfloat(row[20]),
                "p": isfloat(row[21]),
                "k": isfloat(row[22]),
                "se": isfloat(row[23]),
                "na": isfloat(row[24]),
                "zn": isfloat(row[25]),
                "va": isfloat(row[26]),
                "vb1": isfloat(row[27]),
                "vb2": isfloat(row[28]),
                "vb3": isfloat(row[29]),
                "vb5": isfloat(row[30]),
                "vb6": isfloat(row[31]),
                "vb7": isfloat(row[32]),
                "vb9": isfloat(row[33]),
                "vb12": isfloat(row[34]),
                "vc": isfloat(row[35]),
                "vd": isfloat(row[36]),
                "ve": isfloat(row[37]),
                "vk": isfloat(row[38]),
                "colin": isfloat(row[39]),
                "kcal": isfloat(row[40]),
            }
            _dicts.append(_dict)
        p.write(json.dumps(_dicts, ensure_ascii=False,))

"(id,name,tag,description,userid,user,passhash,timestamp,"
"unit,cost,carbo,fiber,protein,fat,saturated_fat,n3,DHA_EPA,n6,"
"ca,cl,cr,cu,i,fe,mg,mn,mo,p,k,se,na,zn,va,vb1,vb2,vb3,vb5,vb6,vb7,"
"vb9,vb12,vc,vd,ve,vk,colin,kcal)"

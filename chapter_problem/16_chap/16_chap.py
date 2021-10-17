import csv
from os import pipe
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld']
]
with open('villains', 'w') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains', 'r') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]

print(villains)

with open('villains', 'r') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

with open('villains.csv', 'w') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

with open('villains.csv', 'r') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)

# 16.3.2 XML
import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attrbutes:', grandchild.attrib)

print(len(root))
print(len(root[0]))

# 16.3.3 XMLのセキュリティに関するコメント
# from xml.etree.ElementTree import parse
# et = parse(xmlfile)
# from defusedxml.ElementTree import parse
# et = parse(xmlfile)

# 16.3.5 JSON
menu = \
{
    "breakfast": {
        "hours": "7-11",
        "items": {
            "breakfast burritos": "$6.00",
            "pancakes": "$4.00"
        }
    },
    "lunch": {
        "hours": "11-3",
        "items": {
            "hamburger": "$5.00"
        }
    },
    "dinner": {
        "hours": "3-10",
        "items": {
            "spaghetti": "$8.00"
        }
    }
}

import json
menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

import datetime
now = datetime.datetime.utcnow()
now_str = str(now)
print(now_str)

from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

import datetime
now = datetime.datetime.utcnow()
class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))

import datetime
import json
now = datetime.datetime.utcnow()
print(json.dumps(now, default=str))

# 16.3.6 YAML
import yaml
with open('mcintyre.yaml', 'r') as fin:
    text = fin.read()

data = yaml.safe_load(text)
print(data['details'])
print(len(data['poems']))
print(data['poems'][1]['title'])

# 16.3.8 Pandas
import pandas as pd
data = pd.read_csv('villains.csv')
print(data)

dates = pd.date_range('2019-01-01', periods=3, freq='MS')
print(dates)

# 16.3.9
import configparser
cfg = configparser.ConfigParser()
print(cfg)


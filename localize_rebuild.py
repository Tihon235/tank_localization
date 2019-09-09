#!/usr/bin python3
# encoding: utf-8
import json

with open("csDic.json",'r') as load_f:
    load_dict = json.load(load_f)

with open("csDic.json.bak",'w') as dump_f:
    json.dump(load_dict,dump_f)

with open("record.en.txt",'r') as load_en:
    lang_en = load_en.readlines();

with open("record.ar.txt",'r') as load_ar:
    lang_ar = load_ar.readlines();

with open("record.ja.txt",'r') as load_ja:
    lang_ja = load_ja.readlines();

with open("record.ko.txt",'r') as load_ko:
    lang_ko = load_ko.readlines();

with open("record.ru.txt",'r') as load_ru:
    lang_ru = load_ru.readlines();

with open("record.tw.txt",'r') as load_tw:
    lang_tw = load_tw.readlines();
zh = 6
en = 10
ja = 22
ko = 23
ru = 30
ar = 1
tw = 41

def check_language(jsondata,language_type,lang):
    exsit = False;
    for value in jsondata:
        if int(value['regionID']) == language_type:
            value['text'] = lang.strip()
            exsit = True;
            break;
    clone = jsondata[0];
    if not exsit:
        clone['regionID'] = language_type
        clone['text'] = lang.strip()
        jsondata.append(clone)

length = len(load_dict['language'])
i = 0
content = ''
for language in load_dict['language']:
    print(i /length)
    items = language['datas']
    check_language(items,en,lang_en[i]);
    check_language(items,ja,lang_ja[i]);
    check_language(items,ko,lang_ko[i]);
    check_language(items,ru,lang_ru[i]);
    check_language(items,ar,lang_ar[i]);
    check_language(items,tw,lang_tw[i]);
    i = i + 1    

with open("csDic.json","w") as dump_f:
    json.dump(load_dict,dump_f)

import hashlib
def get_token(md5str):
    m1 = hashlib.md5()
    m1.update(md5str.encode("utf-8"))
    token = m1.hexdigest()
    return token

with open('csDic.json.md5','w') as md5:
    md5.write(get_token(json.dumps(load_dict)))
    
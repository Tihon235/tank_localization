#!/usr/bin python3
# encoding: utf-8
import json

with open("csDic.json",'r') as load_f:
    load_dict = json.load(load_f)

with open("csDic.json.bak",'w') as dump_f:
    json.dump(load_dict,dump_f)

with open("record.cn.txt",'r') as load_cn:
    lang_cn = load_cn.readlines();

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

def check_language(template,language_type,lang):
    clone = template.copy();
    clone['regionID'] = language_type
    clone['text'] = lang.strip()
    return clone

length = len(load_dict['language'])
i = 0
content = ''
for language in load_dict['language']:
    print(i /length)
    item = language['datas'][0]
    newjson = []
    newjson.append(check_language(item,zh,lang_cn[i]));
    newjson.append(check_language(item,en,lang_en[i]));
    newjson.append(check_language(item,ja,lang_ja[i]));
    newjson.append(check_language(item,ko,lang_ko[i]));
    newjson.append(check_language(item,ru,lang_ru[i]));
    newjson.append(check_language(item,ar,lang_ar[i]));
    newjson.append(check_language(item,tw,lang_tw[i]));
    language['datas'] = newjson;
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
    
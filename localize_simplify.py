#!/usr/bin python3
# encoding: utf-8
from translate import Translator
translator = Translator(to_lang="en",from_lang='zh')
import json

en = 10
zh = 6
with open("csDic.json",'r') as load_f:
    load_dict = json.load(load_f)

length = len(load_dict['language'])
i = 0
content = ''
for language in load_dict['language']:
    print(i /length)
    i = i + 1
    items = language['datas']
    key = language['key'].strip();
    content += key;
    content += '\r\n' 
    print(key)
    language['key'] = key;
       
        
with open("csDic.json","w") as dump_f:
    json.dump(load_dict,dump_f)


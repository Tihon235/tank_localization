#!/usr/bin python3
# encoding: utf-8

import json

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
       
        
with open("record.cn.txt","w") as file_cn:
    file_cn.write(content);

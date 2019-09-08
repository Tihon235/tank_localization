#!/usr/bin python3
# encoding: utf-8
# from translate import Translator
# translator_zh= Translator(to_lang="zh")
# translator_en = Translator(to_lang="en",from_lang='zh')
# translator_ja= Translator(to_lang="ja",from_lang='zh')
# translator_ko= Translator(to_lang="ko",from_lang='zh')
# translator_ar= Translator(to_lang="ar",from_lang='zh')
# translator_ru= Translator(to_lang="ru",from_lang='zh')
# translator_tw= Translator(to_lang="zh-tw",from_lang='zh')
# temp ="来我家玩吧"
# translation = translator_en.translate(temp)
# print(translation)
# translation = translator_ja.translate(temp)
# print(translation)
# translation = translator_ko.translate(temp)
# print(translation)
# translation = translator_ar.translate(temp)
# print(translation)
# translation = translator_ru.translate(temp)
# print(translation)
# translation = translator_tw.translate(temp)
# print(translation)

from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
      'translate.google.com.hk',
    ])
print(translator.translate('veritas lux mea', src='la',dest='ja'))
import json

zh = 6
en = 10
ja = 22
ko = 23
ru = 30
ar = 1
tw = 41

with open("csDic.json",'r') as load_f:
    load_dict = json.load(load_f)

length = len(load_dict['language'])
i = 0
for language in load_dict['language']:
    print(i /length)
    i = i + 1
    items = language['datas']
    key = language['key']
    print(key)
    for value in items:
        if value['text'].strip()!="":
            continue
        if int(value['regionID']) == zh:
            continue
        # if int(value['regionID']) == en:
        #     value['text'] = translator_en.translate(key)
        # if int(value['regionID']) == ja:
        #     value['text'] = translator_ja.translate(key)
        # if int(value['regionID']) == ko:
        #     value['text'] = translator_ko.translate(key)
        # if int(value['regionID']) == ru:
        #     value['text'] = translator_ru.translate(key)
        # if int(value['regionID']) == tw:
        #     value['text'] = translator_tw.translate(key)
        # if int(value['regionID']) == ar:
        #     value['text'] = translator_ar.translate(key)
        # if int(value['regionID']) == en:
        #     value['text'] = translator.translate(key, src='zh',dest='en')
        # if int(value['regionID']) == ja:
        #     value['text'] = translator.translate(key, src='zh',dest='ja')
        # if int(value['regionID']) == ko:
        #     value['text'] = translator.translate(key, src='zh',dest='ko')
        # if int(value['regionID']) == ru:
        #     value['text'] = translator.translate(key, src='zh',dest='ru')
        # if int(value['regionID']) == tw:
        #     value['text'] = translator.translate(key, src='zh',dest='zh-tw')
        # if int(value['regionID']) == ar:
        #     value['text'] = translator.translate(key, src='zh',dest='ar')

with open("record.json","w") as dump_f:
    json.dump(load_dict,dump_f)
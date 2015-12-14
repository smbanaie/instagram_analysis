# -*- coding: utf-8 -*-
import requests
import codecs
from utility import MakeUniqueValues
from langdetect import detect

client_id = 'baad7b9aa14041c5bb2dc1f9b477447c'
parameters = dict(
    client_id=client_id
)


tags_file = codecs.open(r'tags.txt', 'rU', 'utf-8')
tags = []
for tag in tags_file :
    tags.append(tag)
tags_file.close()

output = codecs.open(r'tags.txt', 'aU', 'utf-8')

tags_collection = {}

# tags =["زمستان","مشهد" ,"ایران" ,"گل","تهران","اصفهان","شیراز","اهواز","بوشهر","پسرونه","دخترونه","طنز","تلگرام"]
for tag in tags :
    tag_endpoint = "https://api.instagram.com/v1/tags/%s/media/recent" % (tag.strip())
    print tag_endpoint
    try :
        r = requests.get(tag_endpoint,params=parameters)
        if r.status_code == 200 :
            medias =  r.json()["data"]
            for media in medias:
                for tag in media["tags"] :
                        if detect(tag)=='fa' and len(tag)>1:
                            print(tag)
                            if tag in tags_collection.keys() :
                                tags_collection[tag] += 1
                            else :
                                tags_collection[tag] = 1

    except :
        pass
for k,v in tags_collection.items() :
    output.write("%s - %s\n" %(k,v) )
output.close()
# remove redundancies
MakeUniqueValues('tags.txt')

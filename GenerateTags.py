#-*- coding: utf-8 -*-
import requests
import codecs
import time
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

output = codecs.open(r'tags_all.txt', 'w', 'utf-8')

# tags =["زمستان","مشهد" ,"ایران" ,"گل","تهران","اصفهان","شیراز","اهواز","بوشهر","پسرونه","دخترونه","طنز","تلگرام"]
cnt =1
length = len(tags)
for tag in tags :
    print ("%d of %d" %(cnt,length))
    cnt+=1
    tag_endpoint = u"https://api.instagram.com/v1/tags/%s/media/recent" % (tag.strip())
    try :
        time.sleep(1)
        r = requests.get(tag_endpoint,params=parameters)
        if r.status_code == 200 :
            medias =  r.json()["data"]
            for media in medias:
                for tag in media["tags"] :
                        if detect(tag)=='fa' :
                            if len(tag)>1:
                                print(tag)
                                output.write(tag+"\n")
            output.flush()
    except Exception as e :
        print(str(e))
output.close()
# remove redundancies
MakeUniqueValues('tags_all.txt','tags.txt')

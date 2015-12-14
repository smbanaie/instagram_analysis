#-*- coding: utf-8 -*-

import requests
import codecs
from utility import MakeUniqueValues

from langdetect import detect

client_id = 'baad7b9aa14041c5bb2dc1f9b477447c'

output = codecs.open(r'tags.txt', 'aU', 'utf-8')

parameters = dict(
    client_id=client_id
)

tags =["پسرونه" ,"ایران" ,"دخترونه" ,"تهران" ,"کتاب" , "مهتاب","سفر"]

for tag in tags :
    tag_endpoint = "https://api.instagram.com/v1/tags/%s/media/recent" % (tag)
    try :
        r = requests.get(tag_endpoint,params=parameters)

        if r.status_code == 200 :

            medias =  r.json()["data"]
            for media in medias:
                for tag in media["tags"] :
                        if detect(tag)=='fa' and len(tag)>1:
                            output.write(tag + "\n")
                            print (tag)
    except :
        pass
output.close()

# remove redundancies
MakeUniqueValues('tags.txt')
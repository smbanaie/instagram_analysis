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
media_ids = codecs.open(r"medias.txt", 'aU', 'utf-8')




line  =1
mcnt  = 1
for tag in tags_file :
            # output.write(media["caption"]["text"]+"\n")
    tag_endpoint = "https://api.instagram.com/v1/tags/"+tag.strip()+"/media/recent"
    print (str(line))
    line +=1
    try :
            r = requests.get(tag_endpoint,params=parameters)
            if r.status_code == 200 :

                medias =  r.json()["data"]
                for media in medias:
                    if detect(media["caption"]["text"])=="fa" :
                        print ("   media #: "+ str(mcnt))
                        mcnt +=1
                        media_ids.write(media["id"]+"\n")

                media_ids.flush()
    except Exception,e:
        print e.message

tags_file.close()
media_ids.close()

MakeUniqueValues("medias.txt")
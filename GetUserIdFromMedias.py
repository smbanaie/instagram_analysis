# -*- coding: utf-8 -*-


import requests
import codecs

from utility import MakeUniqueValues

client_id = 'baad7b9aa14041c5bb2dc1f9b477447c'

parameters = dict(
    client_id=client_id
)

media_ids = codecs.open(r"D:\MyProjects\Instagram\medias.txt", 'rU', 'utf-8')
user_ids = codecs.open(r"D:\MyProjects\Instagram\user_ids.txt", 'wU', 'utf-8')


line = 1
for id in media_ids :
    print("Processing Line # "+str(line))
    like_endpoint = "https://api.instagram.com/v1/media/"+id.strip()+"/likes"
    print (str(line))
    line +=1
    try :
        r = requests.get(like_endpoint,params=parameters)
        if r.status_code == 200 :
            likes = r.json()["data"]
            for like in likes :
                user_ids.write(like["id"]+"\n")
    except :
        pass

    comments_endpoint = "https://api.instagram.com/v1/media/"+id.strip()+"/comments"
    try :
        r = requests.get(comments_endpoint,params=parameters)
        if r.status_code == 200 :
            comments = r.json()["data"]
            for comment in comments :
                user_ids.write(comment["from"]["id"]+"\n")
    except :
        pass
    media_ids.flush()




media_ids.close()
user_ids.close()


MakeUniqueValues("D:\MyProjects\Instagram\user_ids.txt")

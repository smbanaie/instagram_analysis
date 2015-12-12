# -*- coding: utf-8 -*-

from datetime import datetime
import requests
import codecs
from utility import MakeUniqueValues

from langdetect import detect

client_id = 'baad7b9aa14041c5bb2dc1f9b477447c'

info_output = codecs.open(r"D:\MyProjects\Instagram\info.csv", 'aU', 'utf-8')
user_id_input = codecs.open(r"D:\MyProjects\Instagram\user_ids.txt", 'rU', 'utf-8')
csv_info = u"user_id,post_id,utc_time,tags_count,likes_count,comments_count,text_length\n"
info_output.write(csv_info)
parameters = dict(
    client_id=client_id
)

cnt = 1
for uid in user_id_input :
    user_endpoint = "https://api.instagram.com/v1/users/%s/media/recent/" % (uid.strip())
    try :
        print  ("Processing # " + str(cnt))
        cnt +=1
        r = requests.get(user_endpoint,params=parameters)
        if r.status_code == 200 :
            user_data =  r.json()["data"]
            for post in user_data:
                post_info={}
                post_info["user_id"] = uid.strip()
                post_info["post_id"] = post["id"]
                post_info["time"] = datetime.utcfromtimestamp(float(post["caption"]["created_time"])).isoformat()
                post_info["text"] = post["caption"]["text"]
                post_info["tags"] = post["tags"]
                post_info["tags_count"] = len(post["tags"])
                post_info["likes_count"] = post["likes"]["count"]
                post_info["comments_count"] = post["comments"]["count"]

                print post_info

                csv_info = (u"%(user_id)s,%(post_id)s,%(time)s,%(tags_count)s,%(likes_count)s,%(comments_count)s," % post_info) + str(len(post_info["text"]))
                info_output.write(csv_info)
                info_output.write("\n")
        info_output.flush()



    except Exception,e:
        print(e.message)

info_output.close()
user_id_input.close()
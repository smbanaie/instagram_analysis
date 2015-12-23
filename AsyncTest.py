#-*- coding: utf-8 -*-
import requests
import codecs
from utility import MakeUniqueValues
from langdetect import detect
import grequests


client_id = 'baad7b9aa14041c5bb2dc1f9b477447c'
parameters = dict(
    client_id=client_id
)

tags_file = codecs.open(r'tags.txt', 'rU', 'utf-8')
tags = []
for tag in tags_file :
    tags.append(tag)
tags_file.close()


def print_url(r,**kwargs):
    if r.status_code == 200 :
            output = codecs.open(r'tags_all.txt', 'aU', 'utf-8')
            medias =  r.json()["data"]
            for media in medias:
                for tag in media["tags"] :
                        if detect(tag)=='fa' and len(tag)>1:
                            print(tag)
                            output.write(tag+"\n")
            output.close()

def async(url_list):
    sites = []
    for u in url_list:
        rs = grequests.get(u, hooks=dict(response=print_url))
        sites.append(rs)
    return grequests.map(sites)

urls = [u"https://api.instagram.com/v1/tags/%s/media/recent?client_id=%s" % (tag.strip(),client_id) for tag in tags]
print (async(urls))




#
# output = codecs.open(r'tags_all.txt', 'wU', 'utf-8')
#
# # tags =["زمستان","مشهد" ,"ایران" ,"گل","تهران","اصفهان","شیراز","اهواز","بوشهر","پسرونه","دخترونه","طنز","تلگرام"]
# cnt =1
# length = len(tags)
# for tag in tags :
#     print ("%d of %d" %(cnt,length))
#     cnt+=1
#     tag_endpoint = u"https://api.instagram.com/v1/tags/%s/media/recent" % (tag.strip())
#     try :
#         r = requests.get(tag_endpoint,params=parameters)

#     except Exception,e:
#         print(e.message)
# output.close()
# remove redundancies
MakeUniqueValues('tags_all.txt','tags.txt')
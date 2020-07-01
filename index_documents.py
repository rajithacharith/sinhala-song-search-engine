import json
import os
from elasticsearch import Elasticsearch

es=Elasticsearch([{'host':'localhost','port':9200}])
file_list = os.listdir('./processed_corpus')
count = 0
for file in file_list:
    count+=1
    f = open('./processed_corpus/'+file, encoding="utf8")
    s = f.read()
    data = json.loads(s.replace('\r\n', ''), strict=False)
    res=es.index(index='song_new',doc_type='songs',id=count,body=data)


#-*- coding: UTF-8 -*-
import json

data = []
with open('./cnblogs.json') as f:
    for line in f:
        data.append(json.loads(line))

#print json.dumps(data, ensure_ascii=False)

import codecs
file_object = codecs.open('cnblogs.txt', 'w' ,"utf-8")
for item in data:
    #print json.dumps(item)
    str = "%s#_#%s#_#%s#_#%s\r\n" % (item['title'],item['link'],item['desc'],item['listUrl'])
    file_object.write(str)

file_object.close()
print "success"

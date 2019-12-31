from videoDemo import videoDemo 
from Dbobj import Dbobj 
import json
if __name__=='__main__':
	#g = {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":1,"translateResult":[[{"src":"english","tgt":"英语"}]]};
    l = range(5);
    for i in l:
    	print(i)
    exit('8')
    url="https://www.xvideos.com";
    getObj = videoDemo();
    dbObj = Dbobj('redio','re_')
    curName=getObj.doTrans('Big ass asian girlfriend moaning for creampie');
    print(curName);exit('9')
    # arr = []
    # for i in getObj.getCategory('https://www.xvideos.com/'):
    #    if i != '':
    #    	arr.append({'_id':dbObj.getNextValue('category'),'name':i.strip(),'cname':''})
    # re = dbObj.getTbname('category').insert_many(arr)
    tmpData = dbObj.getTbname('tags').find({"cname": ""})
    for v in tmpData:
    	if v['name'].strip() != '':
    		curName=getObj.doTrans(v['name']);
    		dbObj.getTbname('tags').update({"_id":v['_id']},{"$set":{"cname":curName}})
 #    doTrans(self,keywords)
 #    ;print('5');
 #    print('55')
 #   		print(i);exit('3')
 #       arr.append({'_id':dbObj.getNextValue('category'),'name':i.strip(),'cname':''})
	# re = dbObj.getTbname('category').insert_many(arr){'id': '52398905', 'rel': '/video52398905/big_ass_asian_girlfriend_moaning_for_creampie', 'title': 'Big ass asian girlfriend moaning for creampie', 'ctitle': '', 'show_time': '21 min', 'real_time': 21}
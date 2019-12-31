from videoDemo import videoDemo 
from Dbobj import Dbobj 
import pymongo
import json
if __name__=='__main__':
    url="https://www.xvideos.com";
    # pageList = range(1,5)
    # print(pageList);exit('3')
    # getObj = videoDemo();
    dbObj = Dbobj('redio','re_')
    curTableObj = dbObj.getTbname('redios')#.limit(10).skip(5)
    #data = curTableObj.find({"tags":{"$reg":"%hot%"}}).limit(1)
    data = curTableObj.find({'tags': {'$regex':'mo.*'}}).limit(1)
 db.inventory.find( {
    $and : [
        { $or : [ { price : 0.99 }, { price : 1.99 } ] },
        { $or : [ { sale : true }, { qty : { $lt : 20 } } ] }
    ]
} ) 
   
    #results_count = data.count()
    for v in data:
         print(v['tags'])

    print(data.count());exit('3')
    # for v in data:
    #     print(v['rel'])
    # for v in tmpData:
    # 	if v['name'].strip() != '':
    # 		curName=getObj.doTrans(v['name']);
    # 		dbObj.getTbname('tags').update({"_id":v['_id']},{"$set":{"cname":curName}})
 #    doTrans(self,keywords)
 #    ;print('5');
 #    print('55')
 #   		print(i);exit('3')
 #       arr.append({'_id':dbObj.getNextValue('category'),'name':i.strip(),'cname':''})
	# re = dbObj.getTbname('category').insert_many(arr){'id': '52398905', 'rel': '/video52398905/big_ass_asian_girlfriend_moaning_for_creampie', 'title': 'Big ass asian girlfriend moaning for creampie', 'ctitle': '', 'show_time': '21 min', 'real_time': 21}
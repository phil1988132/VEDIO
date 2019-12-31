#分页抓取视频url
from videoDemo import videoDemo 
from Dbobj import Dbobj 
import json
from multiprocessing import Pool,Process
import time


if __name__=='__main__':    
    getObj = videoDemo();
    dbObj = Dbobj('redio','re_')
    arr = [];
    curTableObj = dbObj.getTbname('redios')
    data = curTableObj.find({"status":0}).sort('_id', pymongo.ASCENDING).limit(10)
    base = 'https://www.xvideos.com/'
    _count = len(data)
    pool = Pool(_count)
    for v in data:
       curUrl = base+i['rel'].strip('/')   
       #curTableObj.run(curUrl,i['id'])
       p.apply_async(curTableObj.run, args=(curUrl,v['id']))
    p.close()
    p.join()
    print('All subprocesses done.')
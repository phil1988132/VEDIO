#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#分页抓取视频url
import json
from multiprocessing import Pool,Process
import time
import pymongo
import sys
sys.path.append('..')
from commone.GoogleTranslator import GoogleTranslator
from commone.videoDemo import videoDemo 
from commone.Dbobj import Dbobj 

def deRange(num):
    getObj = videoDemo();
    dbObj = Dbobj('redio','re_')
    arr = [];
    curTableObj = dbObj.getTbname('redios')
    url="https://www.xvideos.com/new/"+str(num);

    for v in getObj.getVedioUrl(url):
        print(v);exit('4');
        if v['id']!='':
           v['_id'] = dbObj.getNextValue('redios')
           v['tags']=v['cates']=''
           v['status']=0
           curTableObj.update({"id":v['id'].strip()},{"$setOnInsert":v}, upsert=True);
    i -=1;
    if i%10 == 0:
       time.sleep(0.5)     
if __name__=='__main__':
    pageList = [1]
    pageCount = len(pageList)
    p = Pool(pageCount)
    for i in pageList:
        p.apply_async(deRange, args=(i,))
    p.close()
    p.join()
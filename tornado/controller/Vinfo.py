#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tornado.ioloop
import tornado.web
# import sys
# sys.path.append('D:\\wwwroot\\py\\tornado')
#from videoDemo import videoDemo 
#from Dbobj import Dbobj 
import math
import pymongo
import re
import hashlib
from urllib.parse import urlparse
#import sys
#sys.path.append('....commone')
import os
os.sys.path.append(os.path.join( os.path.dirname(__file__), '../..'))
from commone.Credis import Credis
from commone.Dbobj import Dbobj
from commone.videoDemo import videoDemo

class Vinfo(tornado.web.RequestHandler):
    base = 'https://www.xvideos.com/'
    pageNum = 36
    _k = '12345,.Abc33678'
    def post(self):
      #try:
        head = self.request.headers
        nonce = head.get('nonce',None)
        token = head.get('token',None)
        if(nonce == None or token == None):
           self.finish({'message':1})
           return
        isValid = self.checkPost(nonce,token)
        if isValid == False:
           self.finish({'message':1})
           return
        _stype =  self.get_argument('stype',0)
        if _stype !=0:
           _stype = int(_stype)         
        word = self.get_argument('word',None)
        if word != None:
           word = word.strip().replace("'",'').replace('"','') 
        no = self.get_argument('no',None)
        if no != None:
           no = no.strip().replace("'",'').replace('"','')
           no = int(no)         
        type = self.get_argument('t',1)
        deinfo = ''
        _type = int(type)
        if _type == 1:
            deinfo = self.detail(no)
        elif _type == 2:
            pageSize = self.get_argument('pageNum',0)
            pageSize = int(pageSize)
            ltype = self.get_argument('ltype',0)
            ltype = int(ltype)
            deinfo = self.list(self.get_argument('stype',1),word,self.get_argument('page',1),pageSize,ltype)
        elif _type == 3:
            deinfo = self.tags()
        elif _type == 4:
            deinfo = self.related(no,self.get_argument('page',1))
        elif _type == 5:
            deinfo = self.likes(no)
        elif _type == 6:
            deinfo = self.views(no)
        elif _type == 7:
            deinfo = self.tops()
        elif _type == 8:
            deinfo = self.tags(1)
        elif _type == 9:
            deinfo = self.tags(2)
        self.finish(deinfo)
      #except:
      #  self.finish({'message':1})
    # def get(self):
    #     type = self.get_argument('t',1)
    #     deinfo = ''
    #     if int(type) == 1:
    #         deinfo = self.detail(self.get_argument('no'))
    #     elif int(type) == 2:
    #         deinfo = self.list(self.get_argument('stype',1),self.get_argument('word',None),self.get_argument('page',1))
    #     self.finish(deinfo)
        # # elif type == 2:
        # # elif type == 3:
        # self.finish(deinfo)
        # username = self.get_argument('username',None)   # 获取用户名
        # password = self.get_argument('password',None)   # 获取密码        print(self.request)
        # #self.write(username+'555'+password)
        # self.finish({'message': 'ok','url':'12313'})

    def checkPost(self,nonce,token):
        #return True
        nonce = str(nonce).strip()
        _str = str(nonce)+"..,"+self._k
        m = hashlib.md5()
        b = _str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        re = False
        if str_md5 == token:
           re = True
        else:
           re = False   
        
        return re    

    def views(self, videoNo):
        arr = [];
        curTableObj = self.__dbInfo('redios')
        videoNo = int(videoNo)
        if videoNo > 0:
          curTableObj.update_one({"id":str(videoNo)},{"$inc":{"view_times":1}})
        return {'message':0}

    def likes(self, videoNo):
        arr = [];
        curTableObj = self.__dbInfo('redios')
        videoNo = int(videoNo)
        if videoNo > 0:
          curTableObj.update_one({"id":str(videoNo)},{"$inc":{"like_times":1}})
        return {'message':0}
    def getMp4Url(self,url):

        res=urlparse(url)
        return res.netloc

    def detail(self,videoNo):
        arr = [];
        curTableObj = self.__dbInfo('redios')
        data = curTableObj.find_one({"id":str(videoNo)})
        if data is None:
            return {'message':1}  
        sourceInfo = ''
        message = 1
        scheme = self.request.protocol
        curReqHost = self.request.host
        if len(data)>0:
           data['vimg'] = scheme+'://'+curReqHost+'/pimg/'+str(data['id'] )+'/setThumbUrl.jpg'
           message = 0
           getObj = videoDemo();
           url = self.base.rstrip('/')+'/'+data['rel'].lstrip('/')
           sourceInfo = getObj.getMp4(url)
           if 'setVideoUrlLow' in sourceInfo:
              curHost = self.getMp4Url(sourceInfo['setVideoUrlLow'])
              data['lowUrl'] = sourceInfo['setVideoUrlLow'].replace(curHost,curReqHost).replace('https','http')+"&orig="+self.getMp4Url(sourceInfo['setVideoUrlLow'])
           if 'setVideoUrlHigh' in sourceInfo:
              data['highUrl'] = sourceInfo['setVideoUrlHigh'] .replace(curHost,curReqHost).replace('https','http')+"&orig="+self.getMp4Url(sourceInfo['setVideoUrlLow'])
        return {'message':message,'data':data}
    def __dbInfo(self, tableName):
        getObj = videoDemo();
        dbObj = Dbobj('redio','re_')
        return dbObj.getTbname(tableName)

    def list(self,stype,word,page=1,pageSize=0,ltype=0):
        scheme = self.request.protocol
        curReqHost = self.request.host
        _sort = '_id'
        if ltype == 1:#热
           _sort = 'view_times' 
        elif ltype == 2:#高
           _sort = 'like_times' 
          
        page = int(page)
        arr = [];
        curTableObj = self.__dbInfo('redios')
        if pageSize > 0:
           curSize = pageSize
        else:
           curSize = self.pageNum 
        curBegin = (page - 1)*curSize
        #无搜索分页
        newData = []
        data = ''
        count = 0
        if word != None:
           word = word.strip()
           if len(word) < 1:
              word = None
        orig_word = word      

        if stype == '1' or word == None:
           data = curTableObj.find({"status":1}).sort(_sort, pymongo.DESCENDING).limit(curSize).skip(curBegin)
           count = data.count()
        else:           
           word = word+'.*'  
        if stype == '2':
           #data = curTableObj.find({'tags': {'$regex':'mp.*'}}).limit(1)	
           data = curTableObj.find({"status":1,"tags": {'$regex': word}}).sort('_id', pymongo.DESCENDING).limit(curSize).skip(curBegin)
           #data = curTableObj.find({'tags': {'$regex':'mo.*'}}).limit(1)
           count = data.count()
           #return {'page':count}
        if stype == '3':
            #tagsArr = self.getTagsFromK(orig_word)
            #return {'d':tagsArr}
            # if tagsArr != '':           
            #   data = curTableObj.find({"$and":[{"status":1},{"$or":[{"tags":{'$in':tagsArr}},{"title":{'$regex': word}}]}]}).sort('_id', pymongo.ASCENDING).limit(curSize).skip(curBegin)
            # else:
            #    data = curTableObj.find({"status":1,"title":{'$regex': word}}).sort('_id', pymongo.ASCENDING).limit(curSize).skip(curBegin) 
            data = curTableObj.find({"status":1,"title":{'$regex': word}}).sort('_id', pymongo.DESCENDING).limit(curSize).skip(curBegin) 
            count = data.count() 
        if stype == '4':

           data = curTableObj.find({"category": word}).sort('_id', pymongo.DESCENDING).limit(curSize).skip(curBegin)

           count = data.count()
        if stype == '5':

           data = curTableObj.find({"trends": word}).sort('_id', pymongo.DESCENDING).limit(curSize).skip(curBegin)

           count = data.count()

           #data = curTableObj.find({"$and":[{"status":1},{"$or":[{"tags":{'$regex': word}},{"title":{'$regex': word}}]}]}).sort('_id', pymongo.ASCENDING).limit(curSize).skip(curBegin)      
        for v in data:              
            if v['ctitle']!='':
                 v['title'] = v['ctitle']
            v['vimg'] = scheme+'://'+curReqHost+'/pimg/'+str(v['id'] )+'/setThumbUrl.jpg'
            newData.append(v)
           #count = curTableObj.find({"status":0}).count()
        
        return {'message':0,"data":newData,"count":count,"endPage":self.page(count,page)}

    def getTagsFromK(self,k):
        tags = self.tags()
        data = tags['data']
        validTag = []
        for v in data:
           if v['cname']!='' and (k in v['cname']):
              validTag.append(v['name'])
        return validTag

    def tops(self):
        credis = Credis()
        _keyTag = 'tops'
        data = credis.get(_keyTag)
        if data != None:
            return {'message':0,"data":data}
        arr = [];
        curTableObj = self.__dbInfo('redios')
        #无搜索分页
        newData = []
        data = curTableObj.find({"_id":{"$gt": 1}}).sort('view_times', pymongo.DESCENDING).limit(20)
      
        for v in data:
          if v['ctitle']!='':
               v['title'] = v['ctitle']              
          newData.append(v)
        credis.set(_keyTag,newData,60*60*8)
        return {'message':0,"data":newData}

    def tags(self,type=0):
        credis = Credis()
        _keyTag = 'tags'
        if type == 1:
           _keyTag = 'category'
        elif type == 2:
           _keyTag = 'trends'
        data = credis.get(_keyTag)
        if data != None:
            return {'message':0,"data":data}
        arr = [];
        curTableObj = self.__dbInfo(_keyTag)
        #无搜索分页
        newData = []
        data = curTableObj.find({"_id":{"$gt": 1}})
      
        for v in data:              
              newData.append(v)
        credis.set(_keyTag,newData)
        return {'message':0,"data":newData}
    def related(self,_id,page=1):
        try:
          id = int(_id)
          page = int(page)
        except Exception as eo :
          return {'message':1}  
        arr = [];
        curTableObj = self.__dbInfo('redios')
        #无搜索分页
        newData = []
        if page <1:
           page = 1
        skip = (page-1)*30
        data = curTableObj.find_one({"id":str(_id)})
        if data is None:
            return {'message':1}  
        _tags = data['tags']
        scheme = self.request.protocol
        curReqHost = self.request.host
        _data=curTableObj.find({'tags':{'$in':_tags}}).limit(20)#.skip(skip)
      
        for v in _data:  
              if v['ctitle']!='':
                 v['title'] = v['ctitle']  
              v['vimg'] = scheme+'://'+curReqHost+'/pimg/'+str(v['id'] )+'/setThumbUrl.jpg'          
              newData.append(v)
        return {'message':0,"data":newData}

        # #tag分页
        # elif stype == 2:
        # #关键词分页
        # elif stype == 3:
    def page(self,count=1,curPage=1,showPage=36):
        #显示20页
        pageNum = self.pageNum
        if curPage<1:
           curPage = 1

        endPage = 1
        #endPage = curPage + showPage - 1
        TotalPage = math.ceil(count/pageNum)
        return TotalPage
        #if endPage > TotalPage:
        #   endPage = TotalPage
        # pageList = []
        # if curPage>1:
        #    pageList.append({"title":"首页","val":1})
        #    pageList.append({"title":"前一页","val":curPage-1})
        # for i in range(curPage,endPage):
        #     pageList.append({"title":i,"val":i})
        # return pageList




        
                

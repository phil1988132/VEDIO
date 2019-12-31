from videoDemo import videoDemo
from TxtDemo import TxtDemo 
import re

if __name__=='__main__':
    txt = 'D:\\wwwroot\\fym\\peizhi\\keyword\\a.txt'
    txtDemo = TxtDemo()
    lineCount = txtDemo.getTxtLineCount(txt)
    if int(lineCount) >4999:
        txtDemo.trancateText()
    _set = set()
    todayUrl = 'http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1_c513'
    inTimeUrl = 'http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b42_c513'
    sevenUrl = 'http://top.baidu.com/buzz?b=42&c=513&fr=topbuzz_b341_c513'
    inTimeSoso = 'http://top.sogou.com/hot/shishi_1.html'
    sevenUrlSoso = 'http://top.sogou.com/hot/sevendsnews_1.html'
    sosoArr = urlArr = []
    urlArr.append(todayUrl)
    urlArr.append(inTimeUrl)
    urlArr.append(sevenUrl)
    sosoArr.append(inTimeSoso)
    sosoArr.append(sevenUrlSoso)
    eobj = videoDemo()
    patternBd = '<a class="list-title"([.|\s|\S|\n]*?)>([.|\s|\S|\n]*?)</a>'
    patternSoSo = '<span class="s2"><p class="p1"><a([.|\s|\S|\n]*?)target="_blank">([.|\s|\S|\n]*?)</a></p>([.|\s|\S|\n]*?)</span>'
    for _u in urlArr:
        content = eobj.mainContent(_u)
        if content == None:
            j = 0;
            while j<3:
                content = eobj.mainContent(_u)
                if content != None:
                    break
                j +=1
        if content != None:
            _title = re.findall(patternBd,content)
            print(_title[1]);

            exit(5)
            if(len(_title)<0):
                break
            if len(_title[2])>0 and _title[2].strip() not in _set:
                    _set.add(_title[2])
    for _u in sosoArr:
        content = eobj.mainContent(_u)
        if content == None:
            j = 0;
            while j<3:
                content = eobj.mainContent(_u)
                if content != None:
                    break
                j +=1
        if content != None:
            _title = re.findall(patternSoSo,content)
            if(len(_title)<0):
                break
            if len(_title[1])>0 and _title[1].strip() not in _set:
                    _set.add(_title[1])
    if len(_set)>0:  
       with open(txt,"a+", encoding='utf-8') as f:
            for title in _set:
                if len(title)>0:
                    f.write(title+'\n')
            f.close()

    print(len(_set))

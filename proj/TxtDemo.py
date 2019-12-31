class TxtDemo:
    def getTxtLineCount(self,filepath):
        count = len(open(filepath, 'r').readlines())
        return count
    def trancateText(self,filepath):
        with open(filepath, "r+") as f:
            read_data = f.read()
            f.truncate()   #清空文件

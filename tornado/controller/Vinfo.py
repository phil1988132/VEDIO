import tornado.ioloop
import tornado.web
import sys
sys.path.append('D:\\wwwroot\\py\\tornado')
from videoDemo import videoDemo 

class Vinfo(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request)
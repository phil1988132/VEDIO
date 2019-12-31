import tornado.ioloop
import tornado.web
import sys
import tornado.autoreload
# sys.path.append('D:\\wwwroot\\py\\proj')
# from videoDemo import videoDemo 
from Vinfo import Vinfo 

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/info", Vinfo),
    ],debug=True)

if __name__ == "__main__":
    app = make_app()
    arg = sys.argv
    g = arg[1]
    g = int(g)
    app.listen(g)
    #app.listen(8885)
    tornado.ioloop.IOLoop.current().start()
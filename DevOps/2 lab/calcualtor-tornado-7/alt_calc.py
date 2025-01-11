from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from Calc_func import Schitator

class MainHandler(RequestHandler):
    def get(self):
        n1 = self.get_argument("n", None)
        n2 = self.get_argument("m", None)
        op = self.get_argument("op", None)
        if n1 and n2:
            self.write({"result":str(Schitator(n1, n2, op))})


def make_app():
    return Application([
    (r"/", MainHandler)
])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    IOLoop.current().start()
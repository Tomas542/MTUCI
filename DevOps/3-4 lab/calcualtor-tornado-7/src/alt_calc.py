import abc

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from src.Calc_func import schitator


class MainHandler(RequestHandler, abc.ABC):
    def get(self) -> None:
        n1 = self.get_argument("n", None)
        n2 = self.get_argument("m", None)
        op = self.get_argument("op", None)
        if n1 and n2:
            self.write({"result": str(schitator(float(n1),
                                                float(n2), str(op)))})


def make_app() -> Application:
    return Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("start")
    IOLoop.current().start()

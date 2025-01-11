from sys import float_repr_style
import tornado.web
import tornado.ioloop

class PageCalc(tornado.web.RequestHandler):
    def get(self):
        number1 = str(self.get_argument("num1", 0))
        number2 = str(self.get_argument("num2", 0))
        operator = self.get_argument("Option", "+")

        a, b = number1, number2
        a = a.replace(".", "")
        a = a.replace(",", "")
        b = b.replace(".", "")
        b = b.replace(",", "")

        if a.isdigit() and b.isdigit():
            sum = summator(number1, number2, operator)
        else:
            sum = "Error"
        self.render('Calculator.html', answer = sum)

def summator(number1, number2, operator):
    number1 = float(str(number1).replace(",", "."))
    number2 = float(str(number2).replace(",", "."))

    if operator == "+":
        buffer = number1 + number2
    elif operator == "-":
        buffer = number1 - number2    
    elif operator == "*":
        buffer = number1 * number2    
    elif operator == "/":        
        if number2 != 0:
            buffer = number1 / number2
        else:
            buffer = "Error"
    else:
        buffer = 'Unpredictable error'
    
    if type(buffer) == float:
        if buffer // 1 == buffer:
            buffer = int(buffer)
    
    return buffer

def make_app():
    return tornado.web.Application([
        (r"/", PageCalc),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

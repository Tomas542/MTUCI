import json
from tornado.testing import AsyncHTTPSTestCase

from alt_calc import make_app

class TestHandler(AsyncHTTPSTestCase):
    def get_app(self):
        return make_app()

    def test_calc(self):
        test_table = [
            (5,3,"add","8"),
            (6,2,"sub","4"),
            (7,4,"mul","28"),
            (18,3,"div","2"),
            (5,0,"div","Error")
        ]

        for test_case in test_table:
            responce = self.fetch(f"/?n={test_case[0]}&m={test_case[1]}&op={test_case[2]}")
            self.assertEqual(responce.code, 200)
            self.assertEqual(
                json.loads(responce.body)["result"],
                test_case[3]
            )
from public.login import login_in
import unittest
class Test_login(unittest.TestCase,login_in):
    def test_1(self):
        self.open_browser()
        self.login('测试','demo_test','yhl','123456')

if __name__ == "__main__":
    unittest.main()
import unittest,CCDoc.parse,CCDoc.render

class TestParser(unittest.TestCase):

    def test_modules(self):
        prsr = CCDoc.parse.Parser("testParse",["testme.lua"])
        self.assertIsNotNone(prsr.files["testme.lua"].modules["test"])
    def test_funcs(self):
        prsr = CCDoc.parse.Parser("testParse",["testme.lua"])
        self.assertGreaterEqual(len(prsr.files["testme.lua"].modules["test"].funcs),1)

class TestRender(unittest.TestCase):
    def test_output(self):
        prsr = CCDoc.parse.Parser("testParse",["testme.lua","testin.lua","prime.lua"])
        rndr = CCDoc.render.render("CCDoc test",prsr.files.values(),"testOut")
        self.assertIsNotNone(True)
    def test_render(self):
        prsr = CCDoc.parse.Parser("testParse",["testme.lua","testin.lua","prime.lua"])
        fc,mc,Fc = CCDoc.render.render("CCDoc test",prsr.files.values(),"testOut")
        self.assertEqual(fc,3)
        self.assertEqual(mc,5)
        self.assertEqual(Fc,6+22)

if __name__ == '__main__':
    unittest.main()
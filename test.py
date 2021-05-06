import unittest
from parse_log import readlog, temps_minutes

# v= """
# 11:00-11:30 Exercises
# 11:30-12:00 Break
# """
# r="""
# Break                     30 minutes    50%
# Exercises                 30 minutes    50%
# """
# class TestApp(unittest.TestCase):
#     def test_parse_log(self):
#         #TODO change functiun's name
#         self.assertEqual(toto(v), r)
#         self.assertEqual(toto(v)[-1], "%")
#         self.assertEqual(len(toto(v),43)

class TestApp(unittest.TestCase):
    def test_readlog(self):
        self.assertEqual(readlog('planning.log')[0],['Introduction', '09:20-11:00'])
        self.assertEqual(type(readlog('planning.log')),list)
        self.assertIsNotNone(readlog('planning.log'))
    def test_tempsminutes(self):
        self.assertEqual(temps_minutes('planning.log')[0],['Introduction', 100])
        self.assertEqual(type(temps_minutes('planning.log')), list)
        self.assertIsNotNone(temps_minutes('planning.log'))
    def test_totaltime(self):
        self.assertEqual(total_time('planning.log'),970)
        self.assertEqual(type(total_time('planning.log')), int)
        self.assertIsNotNone(total_time('planning.log'))
    def test_regroupement(self):
        #self.assertEqual()
        self.assertEqual(type)
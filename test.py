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
        self.assertEqual(readlog('planning.log')[0],['Exercises', '11:00-11:15'])
        self.assertEqual(type(readlog('planning.log')),list)
        self.assertIsNotNone(readlog('planning.log'))
    def test_tempsminutes(self):
        self.assertEqual(temps_minutes('planning.log')[0],['Exercises', 15])
        self.assertEqual(type(temps_minutes('planning.log')), list)
        self.assertIsNotNone(temps_minutes('planning.log'))

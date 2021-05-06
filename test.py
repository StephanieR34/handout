import unittest
from parse_log import readlog

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



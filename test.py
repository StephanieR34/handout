import unittest
from parse_log import readlog, temps_minutes, total_time, regroupement

# v= """
# 11:00-11:30 Exercises
# 11:30-12:00 Break
# """
l= [['Introduction', '09:20-11:00'], ['Exercises', '11:00-11:15'], ['Break', '11:15-11:35']]
t= [['Exercises', 105], ['Solutions', 15], ['Functions', 30], ['Exercises', 30]]

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
        self.assertEqual(temps_minutes(l)[1],['Exercises', 15])
        self.assertEqual(type(temps_minutes(l)), list)
        self.assertIsNotNone(temps_minutes(l))
        
    def test_totaltime(self):
        self.assertEqual(total_time(t),180)
        self.assertEqual(type(total_time(t)), int)
        self.assertIsNotNone(total_time(t))

    def test_regroupement(self):
        self.assertEqual(regroupement(t)['Exercises'],135)
        self.assertEqual(type(regroupement(t)), dict)
        self.assertEqual(len(regroupement(t)),3)
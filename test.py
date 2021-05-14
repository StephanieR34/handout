import unittest
import os
from liste import readlog, regroupement, temps_minutes
from dico import total_time, ordre, somme, change_values, pourcentage
from parse_log import main


class TestApp(unittest.TestCase):
    def test_readlog(self):
        self.assertEqual(
            readlog('planning.log')[0], ['Introduction', '09:20-11:00'])
        self.assertEqual(type(readlog('planning.log')), list)
        self.assertIsNotNone(readlog('planning.log'))

    def test_tempsminutes(self):
        r = [['Introduction', '09:20-11:00'], ['Exercises', '11:00-11:15']]
        self.assertEqual(
            temps_minutes(r), [['Introduction', [100]], ['Exercises', [15]]])
        self.assertEqual(type(temps_minutes(r)), list)
        self.assertIsNotNone(temps_minutes(r))

    def test_regroupement(self):
        t = [['Exercises', [15]], ['Break', [20]], ['Lunch Break', [60]], 
             ['Exercises', [40]], ['Break', [10]], ['Exercises', [80]]]
        self.assertEqual(
            regroupement(t), {'Exercises': [15, 40, 80], 'Break': [20, 10],
                              'Lunch Break': [60]})
        self.assertEqual(type(regroupement(t)), dict)
        self.assertEqual(len(regroupement(t)), 3)

    def test_ordre(self):
        t = {'Exercises': [15, 40, 80], 'Break': [20, 10], 'Lunch Break': [60]}
        self.assertEqual(ordre(t), {'Break':[20, 10], 'Exercises': [15, 40, 80],'Lunch Break': [60]})
        self.assertIs(type(somme(t)), dict)
        self.assertIsNotNone(somme(t))

    def test_somme(self):
        t = {'Break':[20, 10], 'Exercises': [15, 40, 80],'Lunch Break': [60]}
        self.assertEqual(
            somme(t), {'Break': [30], 'Exercises': [135], 'Lunch Break': [60]})
        self.assertIs(type(somme(t)), dict)
        self.assertIsNotNone(somme(t))

    def test_changevalues(self):
        t = {'Break': [30], 'Exercises': [135], 'Lunch Break': [60]}
        self.assertEqual(
            change_values(t), {'Break': ['30'], 'Exercises': ['135'],
                               'Lunch Break': ['60']})
        self.assertIs(type(change_values(t)), dict)
        self.assertIsNotNone(change_values(t))

    def test_totaltime(self):
        t = {'Break': ['30'], 'Exercises': ['135'], 'Lunch Break': ['60']}
        self.assertEqual(total_time(t), 225)
        self.assertEqual(type(total_time(t)), int)
        self.assertIsNotNone(total_time(t))

    def test_pourcentage(self):
        t = {'Introduction': ["75"], 'Exercises': ["40"]}
        self.assertEqual(
            pourcentage(t), {'Introduction': ['75', '65'],
                             'Exercises': ['40', '34']})
        self.assertIs(type(pourcentage(t)), dict)
        self.assertIsNotNone(pourcentage(t))

    def test_main(self):
        self.assertFalse(os.path.isfile("result.txt"))
        main("planning.log")
        self.assertTrue(os.path.isfile("result.txt"))


if __name__ == '__main__':
    unittest.main()

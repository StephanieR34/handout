import unittest
from parse_log import readlog, temps_minutes, total_time, regroupement
from parse_log import somme, change_values, pourcentage


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

    def test_somme(self):
        t = {'Exercises': [15, 40, 80], 'Break': [20, 10], 'Lunch Break': [60]}
        self.assertEqual(
            somme(t), {'Exercises': [135], 'Break': [30], 'Lunch Break': [60]})
        self.assertIs(type(somme(t)), dict)
        self.assertIsNotNone(somme(t))

    def test_changevalues(self):
        t = {'Exercises': [135], 'Break': [30], 'Lunch Break': [60]}
        self.assertEqual(
            change_values(t), {'Exercises': ['135'], 'Break': ['30'],
                               'Lunch Break': ['60']})
        self.assertIs(type(change_values(t)), dict)
        self.assertIsNotNone(change_values(t))

    def test_totaltime(self):
        t = {'Exercises': ['135'], 'Break': ['30'], 'Lunch Break': ['60']}
        self.assertEqual(total_time(t), 225)
        self.assertEqual(type(total_time(t)), int)
        self.assertIsNotNone(total_time(t))

    def test_pourcentage(self):
        t = {'Introduction': ["75"], 'Exercises': ["40"]}
        self.assertEqual(
            pourcentage(t), {'Introduction': ['75', '65'],
                             'Exercises': ['40', '35']})
        self.assertIs(type(pourcentage(t)), dict)
        self.assertIsNotNone(pourcentage(t))


if __name__ == '__main__':
    unittest.main()

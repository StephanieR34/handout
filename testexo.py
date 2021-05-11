# import unittest

# from exo import somme, change_values

# class TestExo(unittest.TestCase):
#     def test_somme(self):
#         t={'Exercises': [15, 40, 80], 'Break': [20, 10], 'Lunch Break': [60]}
#         self.assertEqual(somme(t),{'Exercises': [135], 'Break': [30], 'Lunch Break': [60]})
#         self.assertIs(type(somme(t)), dict)
#         self.assertIsNotNone(somme(t))
#     def test_changevalues(self):
#         t={'Exercises': [135], 'Break': [30], 'Lunch Break': [60]}
#         self.assertEqual(change_values(t), {'Exercises': ['135'], 'Break': ['30'], 'Lunch Break': ['60']})
#         self.assertIs(type(change_values(t)), dict)
#         self.assertIsNotNone(change_values(t))
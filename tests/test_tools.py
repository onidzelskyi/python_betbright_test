import unittest

from betbright_test.tools import *


class TestTools(unittest.TestCase):

    def test_calc_date(self):
        # next draw date
        curr_date = datetime.datetime.strptime('2017-04-11 21:00', '%Y-%m-%d %H:%M')
        draw_date = datetime.datetime.strptime('2017-04-12 20:00', '%Y-%m-%d %H:%M')
        self.assertEqual(calc_date(curr_date), draw_date)

        # next draw date is suggested date
        curr_date = datetime.datetime.strptime('2017-04-11 21:00', '%Y-%m-%d %H:%M')
        supply_date = datetime.datetime.strptime('2017-04-12 20:00', '%Y-%m-%d %H:%M')
        self.assertEqual(calc_date(curr_date, supply_date), supply_date)

        # next draw date day is current one but hours is over.
        curr_date = datetime.datetime.strptime('2017-04-12 21:00', '%Y-%m-%d %H:%M')
        draw_date = datetime.datetime.strptime('2017-04-15 20:00', '%Y-%m-%d %H:%M')
        self.assertEqual(calc_date(curr_date), draw_date)

    def test_get_lru(self):
        # For given sequence of memory cells and cache size check out final cache state
        mem_cells = [1, 2, 3, 4, 5, 4, 6]
        self.assertEqual(get_lru(mem_cells, max_size=4), [5, 6, 3, 4])

    def test_get_anagrams(self):
        # At least one anagram presented in the corpus
        self.assertEqual(get_anagrams('heart', ['test', 'earth', 'example']), ['earth'])

        # No anagrams founded in the corpus
        self.assertEqual(get_anagrams('heart', ['test', 'beast', 'example']), [])

        # Try find anagrams for an empty word in the corpus
        self.assertEqual(get_anagrams('', ['test', 'beast', 'example']), [])


if __name__ == '__main__':
    unittest.main()

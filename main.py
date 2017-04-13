"""Example of using tools from betbright_test module."""
import datetime
from betbright_test.tools import calc_date, get_lru, get_anagrams


def date_example():
    """Check out next draw date for given date."""
    curr_date = datetime.datetime.strptime('2017-04-11 21:00', '%Y-%m-%d %H:%M')
    print 'Next draw date for {} is {}'.format(curr_date, calc_date(curr_date))


def lru_example():
    # For given sequence of memory cells and cache size check out final cache state
    mem_cells = [1, 2, 3, 4, 5, 4, 6]
    print 'Final cache state for given sequence memory cells {} is {}'.format(mem_cells, get_lru(mem_cells, max_size=4))


def anagram_example():
    word = 'heart'
    corpus = ['test', 'earth', 'example']
    print 'For given word \'{}\' and corpus {} founded anagrams are: {}'.format(word, corpus, get_anagrams(word, corpus))


if __name__ == '__main__':
    date_example()
    lru_example()
    anagram_example()


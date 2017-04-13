"""This file contains implementation of test questions."""
import datetime


def calc_date(cur_date, supply_date=None):
    """Date Calculation.
    Draw date is Wednesday and a Saturday, e.g., second and fifth day of the week (dow) appropriately.
    If dow for cur_date lays in range from 0 to 2 inclusive then return Wednesday.
    If dow for cur_date lays in range from 3 to 6 inclusive then return Saturday.
    :param cur_date - current date and time, a datetime object.
    :param supply_date - an optional supplied date, a datetime object.
    :return next valid draw date, a datetime object."""
    # Check out if passed params are given type:
    assert isinstance(cur_date, datetime.datetime), 'cur_date not a datetime object.'
    if supply_date:
        assert isinstance(supply_date, datetime.datetime), 'supply_date not a datetime object.'

    # Check out if suggested draw date matched any allowable draw date, not limited to the nearest draw date.
    if supply_date and supply_date.hour == 20 and supply_date.weekday() in [2, 5]:
        return supply_date

    # Wind one day forward if hours above 20
    if cur_date.hour >= 20:
        cur_date = cur_date + datetime.timedelta(days=1)

    # Else calculate nearest draw date
    if cur_date.weekday() < 3:
        days = 2 - cur_date.weekday()
    else:
        days = 5 - cur_date.weekday()

    hours = 20 - cur_date.hour

    return cur_date + datetime.timedelta(hours=hours, days=days)


def get_lru(mem_cells, max_size=100):
    """Least recently used (LRU) cache mechanism.
    :param mem_cells - sequence of memory cells that should be placed in cache, list, in example, 1, 2, 3, 4, 5, 4, 6].
    :param max_size - cache size, generally in memory cells, usually in bytes, in example, 4.
    :return final cache state, list with memory cells; for given examples of mem_cells and max_size is [5, 6, 3, 4]."""
    cache = list()
    age_bits = dict()

    for order, i in enumerate(mem_cells):
        # Check out if memory cell is presented in the cache
        try:
            cell_index = cache.index(i)

        except ValueError:
            # Cell isn't presented in cache.
            if len(cache) == max_size:  # Memory cache is filled up; replace LRU cell
                # Find LRU cell index
                lru_index = sorted(age_bits.items(), key=lambda x: x[1])[0][0]
                # Replace LRU cell with new one.
                cache[lru_index] = i
            else:
                # Add cell in available cache slot.
                cache.append(i)
            # Update cell' age bit
            age_bits[cache.index(i)] = order

        else:
            # Cell already presented in cache. Updated age bit for that cell
            age_bits[cell_index] = order

    return cache


def get_anagrams(word, corpus):
    """Accepts a word (string) and a list of words (list or tuple of strings)
    and return back a list with the valid anagrams for the word inside the given words list.
    :param word - target word, a string.
    :param corpus - list of words to search in, a list.
    :return list of words, a list."""
    target = sorted((x for x in word.lower().strip()))
    return filter(lambda x: target == sorted((ch for ch in x.lower().strip())), corpus)

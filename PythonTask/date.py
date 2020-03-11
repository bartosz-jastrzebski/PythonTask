from datetime import date
import calendar
import itertools
import calendar
import sys


LOWER_LIMIT = date(2000, 1, 1)
UPPER_LIMIT = date(2999, 12, 31)

def converter(file_content: str) -> str:
    nums = [int(num) for num in file_content.split('/')]

    perms = itertools.permutations(nums)
    perms = filter(lambda x: 1 <= x[1] <= 12, perms)

    def validate_day(item):
        year, month, day = item
        if len(str(year)) != 4:
            year += 2000  
        max_day = calendar.monthrange(year, month)[1]
        if day <= max_day:
            return (year, month, day)
 
    results = map(validate_day, perms)
    results = list(filter(None, results))
    if not results:
        return file_content + ' is illegal'

    result = min(results)
    result = date(*result)
    if LOWER_LIMIT <= result <= UPPER_LIMIT:
        return str(result)
    else: 
        return file_content + ' is illegal'


if __name__ == "__main__":

    file_path = sys.argv[1]
    if not file_path.endswith('.txt'):
        print(converter(file_path))
    else:
        with open(file_path, 'r') as file:
            content = file.readline()
            print(converter(content))

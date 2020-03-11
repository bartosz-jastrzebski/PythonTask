import unittest
import random
from datetime import date
from PythonTask.date import converter

class TestConverter(unittest.TestCase):

    def test_example_dates(self):
        # Example:
        # 1/2/3 => 2001-2-3
        # 3/20/1 => 2001-3-20
        self.assertEqual(converter('1/2/3'),'2001-02-03')
        self.assertEqual(converter('3/20/1'), '2001-03-20')

    def test_four_digit_in_input(self):
        self.assertEqual(converter('30/2000/1'), '2000-01-30')
        self.assertEqual(converter('2567/20/12'), '2567-12-20')
        self.assertEqual(converter('05/06/2099'), '2099-05-06')

    def test_two_digits_only(self):
        self.assertEqual(converter('30/20/10'), '2020-10-30')
        self.assertEqual(converter('25/20/12'), '2020-12-25')
        self.assertEqual(converter('05/06/99'), '2099-05-06')


    def test_single_digits_only(self):
        self.assertEqual(converter('1/1/1'), '2001-01-01')
        self.assertEqual(converter('7/8/9'), '2007-08-09')
        self.assertEqual(converter('5/4/3'), '2003-04-05')

    def test_min_and_max_year(self):
        self.assertEqual(converter('00/01/01'), '2000-01-01')
        self.assertEqual(converter('2999/31/12'), '2999-12-31')

    def test_min_number_cannot_be_set_as_year(self):
        self.assertEqual(converter('1/31/30'), '2030-01-31')

    def test_duplicates_in_numbers(self):
        self.assertEqual(converter('1/31/31'), '2031-01-31')

    def test_all_number_equal(self):
        self.assertEqual(converter('12/12/12'), '2012-12-12')
        self.assertEqual(converter('1/1/1'), '2001-01-01')

    def test_year_too_high(self):
        self.assertEqual(converter('3001/1/1'), '3001/1/1 is illegal')

    def test_year_too_low(self):
        self.assertEqual(converter('1999/1/1'), '1999/1/1 is illegal')

    def test_illegal_date(self):
        self.assertEqual(converter('31/31/31'), '31/31/31 is illegal')
        self.assertEqual(converter('3000/3000/3000'), '3000/3000/3000 is illegal')

    def test_leap_year(self):
        self.assertEqual(converter('2000/02/29'), '2000-02-29')

    def test_non_leap_year(self):
        self.assertEqual(converter('2001/02/29'), '2001/02/29 is illegal')

    def test_random_safe_date(self):
        year = random.randint(2000, 2999)
        month = random.randint(1, 12)
        day = random.randint(13, 28)
        correct_test_date = date(year,month,day)
        int_list = [str(x) for x in (year,month,day)]
        random.shuffle(int_list)
        date_to_convert = '/'.join(int_list)        
        self.assertEqual(converter(date_to_convert), str(correct_test_date))


if __name__ == "__main__":
    unittest.main()

    
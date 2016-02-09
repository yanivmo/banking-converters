import unittest
import os
import csv
from cal import cal_conversion


class TestCal(unittest.TestCase):
    OUTPUT_FILE = 'tests/output.csv'

    def tearDown(self):
        if os.path.exists(TestCal.OUTPUT_FILE):
            os.unlink(TestCal.OUTPUT_FILE)

    def test_cal(self):
        cal_conversion('tests/test_cal.xls', TestCal.OUTPUT_FILE)

        expected = [['01/12/15', 'ניו פארם', '19.71'],
                    ['01/12/15', 'אפרודיטה', '50.00'],
                    ['01/12/15', 'הבית', '47.50'],
                    ['01/12/15', 'חומוס', '16.49'],
                    ['02/12/15', 'צומת ספרים', '125.00'],
                    ['02/12/15', 'ארומה', '75.60']]

        with open(TestCal.OUTPUT_FILE, 'r', encoding='utf-8') as f:
            actual = csv.reader(f, dialect=csv.unix_dialect)
            for actual_row, expected_row in zip(actual, expected):
                self.assertEqual(actual_row, expected_row)

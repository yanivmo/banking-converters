import unittest
import os
import csv

from discount_bank import discount_conversion


class TestDiscount(unittest.TestCase):
    OUTPUT_FILE = 'tests/output.csv'

    def tearDown(self):
        if os.path.exists(TestDiscount.OUTPUT_FILE):
            os.unlink(TestDiscount.OUTPUT_FILE)

    def test_discount(self):
        discount_conversion('tests/test_discount.xls', TestDiscount.OUTPUT_FILE)

        expected = [['01/02/2016', 'משיכת שיק', '-300.00'],
                    ['31/01/2016', 'משכורת', '988.00'],
                    ['31/01/2016', 'משכורת', '504.00'],
                    ['19/01/2016', 'ביטוח לאומי', '30.00'],
                    ['18/01/2016', 'משיכת שיק', '-140.00'],
                    ['07/01/2016', 'העברה', '31.00'],
                    ['07/01/2016', 'חיוב לכרטיס ויזה', '-7.00']]

        with open(TestDiscount.OUTPUT_FILE, 'r', encoding='utf-8') as f:
            actual = csv.reader(f, dialect=csv.unix_dialect)
            for actual_row, expected_row in zip(actual, expected):
                self.assertEqual(actual_row, expected_row)

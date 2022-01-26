import unittest

import Database
import VeltNest

class TestVeltNest(unittest.TestCase):

    def test_given_valid_number_of_elements_then_return_true(self):
        number_of_elements = '1'

        result = VeltNest.NestingApp.set_number_of_elements(number_of_elements)

        self.assertTrue(result)

    def test_given_non_valid_number_of_elements_then_return_false(self):
        number = 'sss'

        result = VeltNest.NestingApp.set_number_of_elements(number)

        self.assertFalse(result)

    def test_if_database_is_full(self):
        data_from_data_base = 'value from function'

        result = VeltNest.NestingApp.check_if_database_is_empty(VeltNest.NestingApp, data_from_data_base)

        self.assertFalse(result)

    def test_if_database_is_empty(self):
        data_from_data_base = 'DEFAULT'

        result = VeltNest.NestingApp.check_if_database_is_empty(VeltNest.NestingApp, data_from_data_base)

        self.assertTrue(result)

    def test_given_wrong_file_format_then_return_false(self):
        file_extension = "logo.png"

        result = VeltNest.NestingApp.check_file_format(VeltNest.NestingApp, file_extension)

        self.assertFalse(result)

    def test_given_valid_file_format_then_return_true(self):

        file_extension = "kwadrat.svg"

        result = VeltNest.NestingApp.check_file_format(VeltNest.NestingApp, file_extension)

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
    Database.clean_db()
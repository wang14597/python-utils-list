import unittest
from src.main.list.util_list import UtilsList


class UtilsListTest(unittest.TestCase):

    def test_should_print_each_when_use_foreach(self):
        test_list = UtilsList()
        expected_list = []
        test_list.append(1)
        test_list.append(2)
        test_list.append(3)
        test_list.foreach(expected_list.append)
        self.assertListEqual(test_list, expected_list)


if __name__ == '__main__':
    unittest.main()
import unittest

from src.main.list.util_list import UtilsList

test_list = UtilsList()
test_list.append(1)
test_list.append(2)
test_list.append(3)


class UtilsListTest(unittest.TestCase):

    def test_should_append_each_when_use_foreach(self):
        expected_list = []
        test_list.foreach(expected_list.append)
        self.assertListEqual(test_list, expected_list)

    def test_should_return_new_list_when_use_map(self):
        new_list = test_list.map(lambda x: x ** 2)
        self.assertListEqual(new_list, [1, 4, 9])


if __name__ == '__main__':
    unittest.main()

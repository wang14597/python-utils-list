class UtilsList(list):

    def foreach(self, function):
        for i in self:
            function(i)

    def map(self, function):
        return [function(i) for i in self]


if __name__ == '__main__':
    test_list = UtilsList()
    test_list.append(1)
    test_list.append(2)
    test_list.append(3)
    test_list.foreach(print)

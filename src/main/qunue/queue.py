from list.util_list import UtilsList


class Queue(object):

    def __init__(self, *args):
        self.__elements = [] if args is None else UtilsList(args)

    def __str__(self):
        return f"queue:{str(self.__elements)}"

    def __len__(self):
        return len(self.__elements)

    def __iter__(self):
        self.__count = len(self)
        return self

    def __next__(self):
        element = self.__elements[-self.__count]
        self.__count -= 1
        if self.__count < 0:
            raise StopIteration
        return element

    def enter(self, element):
        self.__elements.append(element)

    def pop(self):
        return self.__elements.pop(0)

    def __eq__(self, other):
        other_elements = getattr(other, "_Queue__elements", None)
        return self.__elements == other_elements

    def is_empty(self):
        return self.__len__() == 0


if __name__ == '__main__':
    q = Queue(1, 2, 3)
    for i in q:
        print(i)
    e = q.pop()
    print(e)
    print(q)
    q.enter(4)
    print(q)
    q2 = Queue(1, 2, 3)
    q3 = Queue(2, 3, 4)
    print(q == q2)
    print(q == q3)

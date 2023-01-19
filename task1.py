"""
Доработать класс FlatIterator в коде ниже. Должен получиться итератор,
который принимает список списков и возвращает их плоское представление,
т.е последовательность состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list_new = []
        for i in range(len(list_of_list)):
            text = list_of_list[i]
            self.list_of_list_new = self.list_of_list_new + text

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor == len(self.list_of_list_new):
            raise StopIteration
        result = self.list_of_list_new[self.cursor]
        self.cursor += 1
        return result


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list_new = []
        for i in range(len(list_of_list)):
            text = list_of_list[i]
            self.list_of_list_new = self.list_of_list_new + text
        self.list_new = []
        for j in range(len(self.list_of_list_new)):
            text1 = self.list_of_list_new[j]
            if type(text1) != list:
                self.list_new.append(text1)
            else:
                for t in text1:
                    while type(t) == list:
                        t = t[0]
                    self.list_new.append(t)

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor == len(self.list_new):
            raise StopIteration
        result = self.list_new[self.cursor]
        self.cursor += 1
        return result



def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
""""
(необязательное задание) Написать генератор аналогичный генератору из задания 2,
но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:

"""

import types


def flat_generator(list_of_list):
    list_of_list_new = []
    for i in range(len(list_of_list)):
        text = list_of_list[i]
        list_of_list_new = list_of_list_new + text
    list_new = []
    for j in range(len(list_of_list_new)):
        text1 = list_of_list_new[j]
        if type(text1) != list:
            list_new.append(text1)
        else:
            for t in text1:
                while type(t) == list:
                    t = t[0]
                list_new.append(t)

    for j in range(len(list_new)):
        yield list_new[j]
        j += 1

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
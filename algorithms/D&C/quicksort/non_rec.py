import random


def qsort(numbers):
    QUEUE, SORTED = [numbers], []
    while QUEUE:
        to_sort = QUEUE.pop()

        if not to_sort:
            continue
        elif len(to_sort) == 1:
            SORTED[:0] = to_sort
        else:
            pivot = to_sort.pop(len(to_sort) // 2)
            left, right = [], []
            for i in to_sort:
                if i <= pivot:
                    left += [i]
                else:
                    right +=[i]
            QUEUE += [left, [pivot], right]
    return SORTED


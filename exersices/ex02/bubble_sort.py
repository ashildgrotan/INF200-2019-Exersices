"""
ex02, task C. Bubble sort.
"""


def bubble_sort(data):
    """
    Takes a list or tuple of sortable elements and sorts it by the "Bubble sort" method.
    :param data: list or tuple
    :return: sorted list
    """
    if type(data) == tuple:
        data = list(data)

    sorted_data = data

    for i in range(len(sorted_data)-1):
        for j in range(len(sorted_data)-1-i):
            if sorted_data[j] > sorted_data[j+1]:
                sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]
    return sorted_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))

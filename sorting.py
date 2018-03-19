import random
import time


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                swapped = True
                temp = array[i]
                array[i] = array[i+1]
                array[i + 1] = temp

    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        compare = array[i]

        while array[j] > compare and j >= 0:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = compare

    return array


def selection_sort(array):
    smallest = array[0]
    key = 0
    swap_key = 0

    while key < len(array):
        for i in range(key, len(array)):
            if smallest > array[i] or smallest is None:
                smallest = array[i]
                swap_key = i

        array[swap_key] = array[key]
        array[key] = smallest
        key += 1
        smallest = None

    return array


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid_index = len(array)/2

    left_array, right_array = merge_sort(array[0:mid_index]), merge_sort(array[mid_index:])

    return merge(left_array, right_array)


def merge(left, right):
    array = []

    left_side_cursor, right_side_cursor = 0, 0

    while left_side_cursor < len(left) and right_side_cursor < len(right):
        if left[left_side_cursor] > right[right_side_cursor]:
            array.append(right[right_side_cursor])
            right_side_cursor += 1
        else:
            array.append(left[left_side_cursor])
            left_side_cursor += 1

    for i in range(left_side_cursor, len(left)):
        array.append(left[i])

    for j in range(right_side_cursor, len(right)):
        array.append(right[j])

    return array


numbers = []
for x in range(1000):
    num = random.randint(1, 100001)

    while num in numbers:
        num = random.randint(1, 101)

    numbers.append(num)

print numbers
print "---------------------------------------------------------------------------------------------"

b_number = list(numbers)
now = time.time()
print bubble_sort(b_number)
print "bubble spent: " + str(time.time()-now)

i_number = list(numbers)
now = time.time()
print insertion_sort(i_number)
print "insertion 1 spent: " + str(time.time()-now)

s_number = list(numbers)
now = time.time()
print selection_sort(s_number)
print "selection spent: " + str(time.time()-now)

m_number = list(numbers)
now = time.time()
print merge_sort(m_number)
print "merge spent: " + str(time.time()-now)

import random
import time


# compare with next element and switch position if next element is greater, repeat until no more swaps
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


# consider first element as sorted array, compare next element with elements inside sorted array and place it before smaller numbers
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        compare = array[i]

        while array[j] > compare and j >= 0:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = compare

    return array


# find smallest element and place it in front, repeat until no more element left
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


# break elements into arrays until only one element left inside each array, put smaller elements on the left and greater elements on the right
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


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left_array, right_array = [], []

        for item in array[1:]:
            if item <= pivot:
                left_array.append(item)
            else:
                right_array.append(item)

        return quick_sort(left_array) + [pivot] + quick_sort(right_array)


def shell_sort(array):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(array):
            temp = array[i]
            j = i

            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap
            array[j] = temp
            i += 1

    return array


def binary_search(array, element):
    middle_element = array[len(array)/2] if len(array) >= 1 else None

    while middle_element != element:
        middle_element = array[len(array) / 2] if len(array) >= 1 else None
        array = array[:len(array) / 2] if middle_element < element else array[len(array) / 2:]

        return binary_search(array, element)

    print "Found element on key: " + str(len(array)/2)


numbers = []
for x in range(1000):
    num = random.randint(1, 10000)

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
print "insertion spent: " + str(time.time()-now)

s_number = list(numbers)
now = time.time()
print selection_sort(s_number)
print "selection spent: " + str(time.time()-now)

m_number = list(numbers)
now = time.time()
print merge_sort(m_number)
print "merge spent: " + str(time.time()-now)

sp_number = list(numbers)
now = time.time()
print quick_sort(sp_number)
print "quick spent: " + str(time.time()-now)

sh_number = list(numbers)
now = time.time()
print shell_sort(sh_number)
print "shell spent: " + str(time.time()-now)

sh_number = list(numbers)
now = time.time()
print shell_sort(sh_number)
print "binary search: " + str(time.time()-now)

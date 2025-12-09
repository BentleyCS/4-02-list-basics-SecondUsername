import math


def bookends(li: list):
    return [li.pop(0), li.pop()]
    """
    Given a list of numbers remove the first and last elements from the list and
    return a new list of those two elements.
    You can assume any list given is at least 2 elements long.
    Example list of [1,5,7,3,2] the original list would become [5,7,3] and the new
    list would be [1,2]
    :param list:
    :return:
    """



def inOrder(li : list):
    previous_largest = -1 * math.inf
    for number in li:
        if number <= previous_largest:
            return False
        else:
            previous_largest = number
    return True

    """
    Given a list of numbers return true if the list is in ascending order.
    :param list:
    :return:
    """



def find(li: list, target : int):
    index = 0
    for item in li:
        if item == target:
            return index
        index += 1
    return -1
    """
    Given a list of numbers and a target value return the index location of the
    target value within the list.
    If the target value is not in the list return -1
    If multiple of the target value exist within the list you may return either
    index.
    You are not alowed to use the built-in index method from python.
    Example list [1,3,5,7,9] target = 3 returned value would be 1 because 3 can be
    found at the first index.
    Example list [3, 7, 8, 1, 0, 1, 12] target = 1 a return of either 3 or 5 would
    be valid.
    Example list [1,3,5,6,9] target 7 returns -1 because 7 is not within the list.
    :param list:
    :param target:
    :return:
    """


def removeLowest(li):
    lowest_num = math.inf
    lowest_num_index = 0
    index = 0
    for item in li:
        if item <= lowest_num:
            lowest_num = item
            lowest_num_index = index
        index += 1
    li.pop(lowest_num_index)

    """
    Given a list of numbers remove the lowest element from the list. You may assume the list is at least 1 element long.
    If there are multiple of the lowest number you just need to remove 1.
    Example list [3,6,7,2,12] would become [3,6,7,12]
    :param list:
    :return:
    """


def keepOrder(li: list, value):
    for index in range(0,len(li)-1):
        if value <= li[index] :
            li.insert(index, value)
            return
    li.append(value)
    """
    Given a list of numbers that is in order and a value. Place the value into the
    list such that the list is still in order.
    Example list=[1,3,5,6] value =4 the resulting list would be [1,3,4,5,6]
    :param list:
    :param value:
    :return:
    """


def merge(left :list, right :list):
    mergelist = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        left_item = left[l]
        right_item = right[r]
        if left_item < right_item:
            mergelist.append(left_item)
            l += 1
        else:
            mergelist.append(right_item)
            r+=1
    while l < len(left):
        mergelist.append(left[l])
        l += 1
    while r < len(right):
        mergelist.append(right[r])
        r += 1
    return mergelist

    # """
    # Given two lists that are in order. produce a new list that is the two lists merged together and in order.
    # Make sure to now modify either of the original lists.
    # Example l1 = [1,3,5] l2 = [2,4,6,8] -> [1,2,3,4,5,6,8]
    # :param l1:
    # :param l2:
    # :return:
    # """
    #
from typing import MutableSequence

def binary_insertion_sort(a:MutableSequence)->None:
    n = len(a)
    for i in range(1,n):
        key = a[i]
#!/usr/bin/env python3
"""Stuff"""


def add_arrays(arr1, arr2):
    """Stuff"""
    arr_final = []

    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(len(arr1)):
            arr_final.append(arr1[i] + arr2[i])
        return arr_final

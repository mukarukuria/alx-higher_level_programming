#!/usr/bin/python3


def remove_char_at(str, n):
    result = ""
    for i, ch in enumerate(str):
        if i == n:
            continue

        result += ch

    return result

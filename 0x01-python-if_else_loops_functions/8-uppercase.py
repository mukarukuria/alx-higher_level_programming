#!/usr/bin/python3
def uppercase(str):
    result = ""

    for ch in str:
        val = ord(ch)

        if val >= 97 and val <= 122:
            val -= 32

        result += chr(val)

    print(result)

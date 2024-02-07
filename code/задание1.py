#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = list(input('Напечатайте предложение: '))
    c = input('Какой символ проверить на вхождение: ')
    lin = []
    for i in range(len(s)):
        if s[i] == c:
            print("".join(lin))
            lin.clear()
        lin.append(s[i])
    print("".join(lin))

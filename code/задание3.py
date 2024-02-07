#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = list(input('Напечатайте предложение: '))
    c = ('о')
    lin = []
    for i in range(len(s)):
        if s[i] != c:
            lin.append(s[i])
        elif s[i] == c and i % 2 == 0:
            lin.append(s[i])
        else:
            continue
    print(''.join(lin))

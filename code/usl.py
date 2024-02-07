#!/usr/bin/env python3
# -- coding: utf-8 --


if __name__ == '__main__':
    s = list(input('Напечатайте 1-e слово: '))
    d = list(input('Напечатайте 2-e слово: '))
    s += d
    for i in s:
        if s.count(i) > 1:
            while i in s:
                s.remove(i)
    print(''.join(s))

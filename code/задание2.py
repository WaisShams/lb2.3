#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = list(input('Напечатайте предложение: '))
    k = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print(i, 'и', i+1)
            k = k+1
    if k == 0:
        print("таких нет")

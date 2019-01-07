#!/usr/bin/python3.6
import sys


def main(f):
    words = []
    d = {}

    with open(f) as f:

        for line in f:
            words_line = line.strip('\n').split()
            for word in words_line:
                words.append(word)

        for i in frozenset(words):
            d.update({i: words.count(i)})

    print(d)


if __name__ == "__main__":
    main(sys.argv[1])

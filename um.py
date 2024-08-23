import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s= s.lower()
    count=0
    matches = re.findall(r'\bum\b[.,]?', s)
    for _ in matches:
        count+=1
    return count



...


if __name__ == "__main__":
    main()

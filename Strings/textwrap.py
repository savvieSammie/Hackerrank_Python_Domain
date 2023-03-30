
"""
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Author    : Samuel Aderibigbe
Created   : 30 March 2023
Updated   : 30 March 2023
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
"""





import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
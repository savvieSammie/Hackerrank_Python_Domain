"""
Title     : Designer Door Mat
Subdomain : Strings
Domain    : Python
Author    : Samuel Aderibigbe
Created   : 13 April 2023
Updated   : 13 April 2023
Problem   : https://www.hackerrank.com/challenges/designer-door-mat/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = list(map(int,input().split()))

for i in range((n//2)+1):
    if((n//2)==i):
        print("WELCOME".center(m,'-'))
    else:
        print((".|."*(i*2+1)).center(m,'-'))

for i in range((n//2)-1,-1,-1):
    print((".|."*(i*2+1)).center(m,'-'))

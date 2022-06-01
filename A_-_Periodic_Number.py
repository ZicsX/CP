"""
For a positive integer n, let str(n) be the string representing n in decimal.
We say that a positive integer n is periodic when there exists a positive integer m such that str(n) is the concatenation of two or more copies of str(m). For example, 11, 1212, and 123123123 are periodic.
You are given a positive integer N at least 11. Find the greatest periodic number at most N. It can be proved that there is at least one periodic number at most N.
"""
def solve(n):
    m = 1
    while True:
        if m > n:
            break
        s = str(m)
        if len(s) % 2 == 0:
            s1 = s[:len(s) // 2]
            s2 = s[len(s) // 2:]
            if s1 == s2:
                print(m)
                return
        m += 1

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
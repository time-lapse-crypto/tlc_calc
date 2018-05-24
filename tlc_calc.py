#!/usr/bin/env python2.7

import sys

def tlc_calc(p, n, t):

    # Verify: 0 < t
    if (t <= 0):
        print ("t must be greater than zero")
        exit(1)

    # Verify: t <= n
    if (t > n):
        print ("t must be less than or equal to n")
        exit(1)

    # Verify: 0 <= p <= 1
    if (p < 0 or p > 1):
        print ("p must be between 0 and 1")
        exit(1)

    print ("p = " + str(p))
    print ("n = " + str(n))
    print ("t = " + str(t))

    q = 1 - p
    P = 0

    for i in range (n, t - 1, -1):
        P += (p**i) * (q**(n - i))

    print ("P(a >= t) = " + str(P))

    return P

if __name__ == "__main__":
    p = float(sys.argv[1])
    n = int(sys.argv[2])
    t = int(sys.argv[3])
    tlc_calc(p, n, t)